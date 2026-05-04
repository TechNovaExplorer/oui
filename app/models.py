from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

@dataclass
class Competence:
    id: str
    nom: str
    niveau: int = 0
    coefficient: float = 1.0
    chemin: str = "Général"
    xp: int = 0  # To track current XP

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "niveau": self.niveau,
            "coefficient": self.coefficient,
            "chemin": self.chemin,
            "xp": self.xp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

@dataclass
class Tache:
    id: str
    description: str
    terminee: bool = False

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "terminee": self.terminee
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

@dataclass
class Mission:
    id: str
    nom: str
    objectif: str
    statut: str = "ouverte" # "ouverte", "active", "terminee", "echec"
    condition_terminaison: Dict = field(default_factory=dict)
    competences_requises: List[Dict] = field(default_factory=list)
    recompenses: Dict = field(default_factory=dict)
    taches: List[Tache] = field(default_factory=list)
    dependances: List[str] = field(default_factory=list)
    date_creation: str = ""
    tags: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "objectif": self.objectif,
            "statut": self.statut,
            "condition_terminaison": self.condition_terminaison,
            "competences_requises": self.competences_requises,
            "recompenses": self.recompenses,
            "taches": [t.to_dict() for t in self.taches],
            "dependances": self.dependances,
            "date_creation": self.date_creation,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data):
        d = dict(data)
        if "taches" in d:
            d["taches"] = [Tache.from_dict(t) if isinstance(t, dict) else t for t in d["taches"]]
        return cls(**d)

@dataclass
class Profile:
    pieces: int = 0
    missions_actives: List[Mission] = field(default_factory=list)
    total_gains: int = 0
    total_depenses: int = 0

    def to_dict(self):
        return {
            "pieces": self.pieces,
            "missions_actives": [m.to_dict() for m in self.missions_actives],
            "total_gains": self.total_gains,
            "total_depenses": self.total_depenses
        }

    @classmethod
    def from_dict(cls, data):
        d = dict(data)
        if "missions_actives" in d:
            d["missions_actives"] = [Mission.from_dict(m) for m in d["missions_actives"]]
        return cls(**d)
