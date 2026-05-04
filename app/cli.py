import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.tree import Tree
from rich.panel import Panel

import app.logic as logic
import app.storage as storage
from app.models import Competence

console = Console()

def cmd_status(args):
    profile = storage.load_profile()
    console.print(Panel(f"[bold gold1]Pièces: {profile.pieces}[/bold gold1] | [bold cyan]Missions actives: {len(profile.missions_actives)}[/bold cyan]", title="Profil", expand=False))

def cmd_import(args):
    succes, msg, mission, cout = logic.importer_mission(args.path)
    if not succes:
        console.print(f"[red]{msg}[/red]")
        return

    console.print(Panel(f"""
[bold]{mission.nom}[/bold]
{mission.objectif}
-------------------
[bold]Coût d'activation:[/bold] {cout} pièces
[bold]Récompenses:[/bold] {mission.recompenses.get('pieces', 0)} pièces, {mission.recompenses.get('xp', {})}
""", title="Mission Importée", expand=False))

    if args.yes:
        rep = "o"
    else:
        rep = console.input(f"Voulez-vous payer {cout} pièces pour l'activer ? (o/n) ").strip().lower()

    if rep == "o":
        succes, msg = logic.activer_mission(mission, cout)
        if succes:
            console.print(f"[green]{msg}[/green]")
        else:
            console.print(f"[red]{msg}[/red]")
    else:
        console.print("Importation annulée.")

def cmd_missions(args):
    profile = storage.load_profile()
    if not profile.missions_actives:
        console.print("Aucune mission active.")
        return

    for m in profile.missions_actives:
        table = Table(title=f"Mission: {m.nom} ({m.id})", show_header=True, header_style="bold magenta")
        table.add_column("ID Tâche", style="dim", width=15)
        table.add_column("Description")
        table.add_column("Statut", justify="center")

        for t in m.taches:
            status = "[green]✓[/green]" if t.terminee else "[red]✗[/red]"
            table.add_row(t.id, t.description, status)

        console.print(table)
        console.print()

def cmd_do(args):
    succes, msg = logic.terminer_tache(args.mission_id, args.tache_id)
    if succes:
        console.print(f"[green]{msg}[/green]")

        # Check if all tasks are done and suggest finishing
        profile = storage.load_profile()
        for m in profile.missions_actives:
            if m.id == args.mission_id:
                if all(t.terminee for t in m.taches):
                    console.print("[bold yellow]Toutes les tâches sont terminées ! Utilisez 'finish' pour valider la mission.[/bold yellow]")
    else:
        console.print(f"[red]{msg}[/red]")

def cmd_finish(args):
    succes, msg = logic.evaluer_mission(args.mission_id, not args.fail)
    if succes:
        console.print(f"[green]{msg}[/green]" if not args.fail else f"[yellow]{msg}[/yellow]")
    else:
        console.print(f"[red]{msg}[/red]")

def build_tree(competences: list[Competence]) -> Tree:
    root = Tree("Compétences")
    paths = {}

    for c in competences:
        parts = c.chemin.split("/")
        current = root
        current_path = ""
        # Create hierarchy based on chemin
        for part in parts:
            current_path += f"/{part}"
            if current_path not in paths:
                node = current.add(f"[bold]{part}[/bold]")
                paths[current_path] = node
            current = paths[current_path]

        # Append skill as leaf node
        xp_req = logic.xp_requis_pour_niveau(c.niveau + 1)
        current.add(f"[bold cyan]{c.nom}[/bold cyan] (Niv {c.niveau}, XP {c.xp}/{xp_req if xp_req != float('inf') else 'MAX'})")

    return root

def cmd_skills(args):
    competences = storage.load_competences()
    if not competences:
        console.print("Aucune compétence pour le moment.")
        return
    tree = build_tree(competences)
    console.print(tree)

def cmd_edit_skill(args):
    competences = storage.load_competences()
    for c in competences:
        if c.id == args.skill_id:
            if args.niveau is not None:
                c.niveau = args.niveau
            if args.coef is not None:
                c.coefficient = args.coef
            if args.xp is not None:
                c.xp = args.xp
            storage.save_competences(competences)
            console.print(f"[green]Compétence {c.id} mise à jour.[/green]")
            return
    console.print(f"[red]Compétence {args.skill_id} introuvable.[/red]")

def cmd_edit_mission(args):
    profile = storage.load_profile()
    for m in profile.missions_actives:
        if m.id == args.mission_id:
            if args.pieces is not None:
                m.recompenses['pieces'] = args.pieces
            if args.add_xp is not None:
                skill, xp = args.add_xp.split(':')
                if 'xp' not in m.recompenses:
                    m.recompenses['xp'] = {}
                m.recompenses['xp'][skill] = int(xp)
            storage.save_profile(profile)
            console.print(f"[green]Mission {m.id} mise à jour.[/green]")
            return
    console.print(f"[red]Mission {args.mission_id} introuvable ou non active.[/red]")

def cmd_report(args):
    profile = storage.load_profile()
    competences = storage.load_competences()

    table = Table(title="Rapport d'activité", show_header=True, header_style="bold yellow")
    table.add_column("Métrique")
    table.add_column("Valeur")

    table.add_row("Pièces actuelles", str(profile.pieces))
    table.add_row("Total des gains", str(profile.total_gains))
    table.add_row("Total des dépenses", str(profile.total_depenses))
    if profile.total_depenses > 0:
        rentabilite = (profile.total_gains / profile.total_depenses) * 100
        table.add_row("Rentabilité", f"{rentabilite:.1f}%")

    console.print(table)
    console.print("\n")

    if competences:
        console.print("[bold]Niveaux des compétences :[/bold]")
        skills_table = Table(show_header=True, header_style="bold cyan")
        skills_table.add_column("Compétence")
        skills_table.add_column("Niveau", justify="center")
        skills_table.add_column("XP")
        for c in sorted(competences, key=lambda x: x.niveau, reverse=True):
            xp_req = logic.xp_requis_pour_niveau(c.niveau + 1)
            skills_table.add_row(c.nom, str(c.niveau), f"{c.xp} / {xp_req if xp_req != float('inf') else 'MAX'}")
        console.print(skills_table)

def main():
    parser = argparse.ArgumentParser(description="Gestion de compétences et missions")
    subparsers = parser.add_subparsers(dest="command", help="Commandes disponibles")

    # status
    subparsers.add_parser("status", help="Affiche le statut actuel (pièces, missions actives)")

    # import
    p_import = subparsers.add_parser("import", help="Importe une mission")
    p_import.add_argument("path", help="Chemin vers le dossier de la mission")
    p_import.add_argument("-y", "--yes", action="store_true", help="Accepter automatiquement le coût")

    # missions
    subparsers.add_parser("missions", help="Liste les missions actives et leurs tâches")

    # do
    p_do = subparsers.add_parser("do", help="Marque une tâche comme terminée")
    p_do.add_argument("mission_id", help="ID de la mission")
    p_do.add_argument("tache_id", help="ID de la tâche")

    # finish
    p_finish = subparsers.add_parser("finish", help="Valide ou échoue une mission")
    p_finish.add_argument("mission_id", help="ID de la mission")
    p_finish.add_argument("--fail", action="store_true", help="Marquer la mission comme échouée")

    # skills
    subparsers.add_parser("skills", help="Affiche l'arbre des compétences")

    # edit-skill
    p_edit_skill = subparsers.add_parser("edit-skill", help="Modifie une compétence manuellement")
    p_edit_skill.add_argument("skill_id", help="ID de la compétence")
    p_edit_skill.add_argument("--niveau", type=int, help="Nouveau niveau")
    p_edit_skill.add_argument("--coef", type=float, help="Nouveau coefficient")
    p_edit_skill.add_argument("--xp", type=int, help="Nouvelle XP")

    # edit-mission
    p_edit_mission = subparsers.add_parser("edit-mission", help="Modifie une mission active manuellement")
    p_edit_mission.add_argument("mission_id", help="ID de la mission")
    p_edit_mission.add_argument("--pieces", type=int, help="Nouvelle récompense en pièces")
    p_edit_mission.add_argument("--add-xp", help="Ajouter/modifier XP pour une compétence (format: skill_id:amount)")

    # report
    subparsers.add_parser("report", help="Affiche un récapitulatif des gains, dépenses et compétences")

    args = parser.parse_args()

    if args.command == "status":
        cmd_status(args)
    elif args.command == "import":
        cmd_import(args)
    elif args.command == "missions":
        cmd_missions(args)
    elif args.command == "do":
        cmd_do(args)
    elif args.command == "finish":
        cmd_finish(args)
    elif args.command == "skills":
        cmd_skills(args)
    elif args.command == "edit-skill":
        cmd_edit_skill(args)
    elif args.command == "edit-mission":
        cmd_edit_mission(args)
    elif args.command == "report":
        cmd_report(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
