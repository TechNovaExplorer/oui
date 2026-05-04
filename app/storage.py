import json
import yaml
import os
from pathlib import Path
from typing import List, Dict, Optional

from app.models import Competence, Profile, Mission

DATA_DIR = Path("app/data")
COMPETENCES_FILE = DATA_DIR / "competences.json"
PROFILE_FILE = DATA_DIR / "profile.json"

def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not COMPETENCES_FILE.exists():
        _save_competences_internal([])
    if not PROFILE_FILE.exists():
        _save_profile_internal(Profile())

def _save_competences_internal(competences: List[Competence]):
    with open(COMPETENCES_FILE, 'w', encoding='utf-8') as f:
        json.dump({"competences": [c.to_dict() for c in competences]}, f, indent=2, ensure_ascii=False)

def _save_profile_internal(profile: Profile):
    with open(PROFILE_FILE, 'w', encoding='utf-8') as f:
        json.dump(profile.to_dict(), f, indent=2, ensure_ascii=False)

def load_competences() -> List[Competence]:
    ensure_data_dir()
    with open(COMPETENCES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [Competence.from_dict(c) for c in data.get("competences", [])]

def save_competences(competences: List[Competence]):
    ensure_data_dir()
    _save_competences_internal(competences)

def load_profile() -> Profile:
    ensure_data_dir()
    with open(PROFILE_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return Profile.from_dict(data)

def save_profile(profile: Profile):
    ensure_data_dir()
    _save_profile_internal(profile)

def load_mission_manifest(folder_path: str) -> Optional[Mission]:
    manifest_path = Path(folder_path) / "manifest.yaml"
    if not manifest_path.exists():
        return None
    with open(manifest_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        # Add terminee=False for tasks that don't have it
        if "taches" in data:
            for t in data["taches"]:
                if "terminee" not in t:
                    t["terminee"] = False
        return Mission.from_dict(data)
