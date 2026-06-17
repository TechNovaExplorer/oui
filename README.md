# Assistant de Compétences et Missions

Un logiciel en ligne de commande pour transformer vos objectifs réels (ex: construire une fusée, apprendre la pâtisserie) en missions, tout en suivant un arbre de compétences évolutif.

## Prérequis

- **Python 3.8+** doit être installé sur votre machine.

## Installation

1. Clonez ce dossier ou téléchargez-le.
2. Ouvrez un terminal dans ce dossier.
3. Installez les dépendances nécessaires en tapant :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Vous pouvez interagir avec l'assistant via les scripts d'exécution fournis.

**Sur Windows (Invite de commandes / PowerShell) :**
```cmd
run.bat <commande>
```

**Sur Mac / Linux :**
```bash
./run.sh <commande>
```

### Commandes disponibles :

- `status` : Affiche votre nombre de pièces et vos missions actives.
- `import <chemin_du_dossier>` : Importe une nouvelle mission depuis son fichier `manifest.yaml` (ex: `./run.sh import missions/gateau`).
- `missions` : Liste vos missions en cours et leurs tâches.
- `do <id_mission> <id_tache>` : Marque une tâche comme terminée.
- `finish <id_mission>` : Valide une mission terminée pour recevoir vos récompenses (XP, pièces). Utilisez `--fail` pour abandonner la mission.
- `skills` : Affiche votre arbre de compétences actuel.
- `report` : Affiche un résumé de vos dépenses, gains globaux et l'évolution de vos niveaux.

## Exemple d'utilisation

1. Regardez votre statut actuel :
   ```bash
   ./run.sh status
   ```
2. Importez la mission d'exemple :
   ```bash
   ./run.sh import missions/gateau
   ```
3. Affichez la liste des tâches :
   ```bash
   ./run.sh missions
   ```
4. Faites la première tâche de la mission :
   ```bash
   ./run.sh do mission_gateau_001 tache_1
   ```
5. Regardez comment vos compétences évoluent !
   ```bash
   ./run.sh skills
   ```
