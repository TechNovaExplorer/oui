import math
from typing import List, Dict, Tuple, Optional

from app.models import Mission, Competence, Profile
import app.storage as storage

def calculer_cout_mission(mission: Mission, competences: List[Competence]) -> int:
    """Calcule le coût en pièces pour activer une mission."""
    comp_dict = {c.id: c for c in competences}
    cout_total = 0.0
    for req in mission.competences_requises:
        cid = req.get("id")
        niveau_requis = req.get("niveau_requis", 0)
        c = comp_dict.get(cid)
        if not c:
            # Si compétence inconnue, on l'estime à niveau 0 avec coef 1.0
            niveau_actuel = 0
            coef = 1.0
        else:
            niveau_actuel = c.niveau
            coef = c.coefficient

        diff = max(0, niveau_requis - niveau_actuel)
        cout = (diff ** 2) * coef
        cout_total += cout
    return math.ceil(cout_total)

def xp_requis_pour_niveau(niveau: int) -> int:
    """Retourne l'XP requise pour atteindre le niveau donné."""
    seuils = {
        1: 100,
        2: 300,
        3: 600,
        4: 1000,
        5: 1500
    }
    return seuils.get(niveau, float('inf'))

def ajouter_xp_et_verifier_niveau(competence: Competence, xp_gagne: int) -> bool:
    """Ajoute de l'XP à une compétence et vérifie si elle monte de niveau.
    Retourne True si le niveau a augmenté."""
    competence.xp += xp_gagne
    level_up = False
    while competence.niveau < 5:
        xp_requis = xp_requis_pour_niveau(competence.niveau + 1)
        if competence.xp >= xp_requis:
            competence.xp -= xp_requis
            competence.niveau += 1
            level_up = True
        else:
            break
    return level_up

def importer_mission(folder_path: str) -> Tuple[bool, str, Optional[Mission], int]:
    """Importe une mission depuis un dossier. Retourne (succès, message, mission, cout)."""
    mission = storage.load_mission_manifest(folder_path)
    if not mission:
        return False, "Dossier ou manifest.yaml introuvable.", None, 0

    competences = storage.load_competences()
    comp_dict = {c.id: c for c in competences}
    competences_modifiees = False

    # Créer les compétences manquantes
    for req in mission.competences_requises:
        cid = req.get("id")
        if cid not in comp_dict:
            nom = cid.replace("_", " ").title()
            nouvelle_comp = Competence(id=cid, nom=nom)
            competences.append(nouvelle_comp)
            comp_dict[cid] = nouvelle_comp
            competences_modifiees = True

    if competences_modifiees:
        storage.save_competences(competences)

    # Si la mission est déjà active
    profile = storage.load_profile()
    if any(m.id == mission.id for m in profile.missions_actives):
        return False, f"La mission {mission.id} est déjà active.", None, 0

    cout = calculer_cout_mission(mission, competences)
    return True, "Mission prête à être importée.", mission, cout

def activer_mission(mission: Mission, cout: int) -> Tuple[bool, str]:
    """Active une mission en payant le coût."""
    profile = storage.load_profile()
    if profile.pieces < cout:
        return False, f"Fonds insuffisants. Vous avez {profile.pieces} pièces, la mission coûte {cout}."

    profile.pieces -= cout
    profile.total_depenses += cout
    mission.statut = "active"
    profile.missions_actives.append(mission)
    storage.save_profile(profile)
    return True, f"Mission '{mission.nom}' activée avec succès !"

def terminer_tache(mission_id: str, tache_id: str) -> Tuple[bool, str]:
    profile = storage.load_profile()
    for mission in profile.missions_actives:
        if mission.id == mission_id:
            for tache in mission.taches:
                if tache.id == tache_id:
                    if tache.terminee:
                        return False, "La tâche est déjà terminée."
                    tache.terminee = True
                    storage.save_profile(profile)
                    return True, "Tâche marquée comme terminée."
            return False, "Tâche introuvable dans cette mission."
    return False, "Mission introuvable ou non active."

def evaluer_mission(mission_id: str, succes: bool) -> Tuple[bool, str]:
    profile = storage.load_profile()
    mission_idx = -1
    for i, m in enumerate(profile.missions_actives):
        if m.id == mission_id:
            mission_idx = i
            break

    if mission_idx == -1:
        return False, "Mission introuvable ou non active."

    mission = profile.missions_actives.pop(mission_idx)

    if not succes:
        storage.save_profile(profile)
        return True, f"Mission '{mission.nom}' marquée comme échouée. Pas de récompense."

    # Validation du succès
    if mission.condition_terminaison.get("toutes_les_taches_requises"):
        if not all(t.terminee for t in mission.taches):
            # Rollback
            profile.missions_actives.append(mission)
            return False, "Toutes les tâches doivent être terminées pour valider la mission."

    # Succès
    recompenses_pieces = mission.recompenses.get("pieces", 0)
    profile.pieces += recompenses_pieces
    profile.total_gains += recompenses_pieces

    competences = storage.load_competences()
    comp_dict = {c.id: c for c in competences}

    xp_gains = mission.recompenses.get("xp", {})
    messages = [f"Mission '{mission.nom}' accomplie !"]
    messages.append(f"+{recompenses_pieces} pièces.")

    for cid, xp in xp_gains.items():
        if cid in comp_dict:
            c = comp_dict[cid]
            lvl_up = ajouter_xp_et_verifier_niveau(c, xp)
            messages.append(f"+{xp} XP pour {c.nom}.")
            if lvl_up:
                messages.append(f"🎉 Niveau supérieur pour {c.nom} ! Niveau actuel : {c.niveau}")

    storage.save_competences(competences)
    storage.save_profile(profile)

    return True, "\n".join(messages)
