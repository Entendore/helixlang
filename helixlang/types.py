"""HelixLang Strict Biological Type System"""
from __future__ import annotations
from typing import List, Dict, Set, Union

class BioTypeError(Exception): pass

class BioMolecule:
    alphabet: Set[str] = set()
    def __init__(self, seq: str):
        seq = seq.upper()
        for char in seq:
            if char not in self.alphabet:
                raise BioTypeError(f"Invalid char '{char}' for {self.__class__.__name__}.")
        self.seq = seq
    def __repr__(self): return f"{self.__class__.__name__}({self.seq[:15]}...)"
    def __eq__(self, other): return isinstance(other, self.__class__) and self.seq == other.seq

class DNA(BioMolecule): alphabet = set("ACGTNRYWSKMBDHV")
class RNA(BioMolecule): alphabet = set("ACGUNRYWSKMBDHV")
class Protein(BioMolecule): alphabet = set("ACDEFGHIKLMNPQRSTVWY*UOXZ")

class TopoDNA:
    def __init__(self, seq: str, sigma: float = 0.0):
        self.seq = seq.upper()
        self.sigma = sigma

class MethylDNA:
    def __init__(self, seq: str, cpg_methylation: float = 0.0):
        self.seq = seq.upper().replace('M', 'C')
        self.cpg_methylation = cpg_methylation

class CellularContext:
    def __init__(self, organism: str, growth_rate: float, phase: str):
        self.organism = organism
        self.growth_rate = growth_rate
        self.phase = phase
        self.ribosome_pool = 45000
        self.state = "normal"

class ThermoState:
    def __init__(self, Kd: float, temp: float, crowding: float):
        self.Kd = Kd
        self.temp = temp
        self.crowding = crowding
        self.eff_conc_multiplier = 1.0 / (1.0 - crowding) if crowding < 1.0 else 999.0

class Population:
    def __init__(self, OD600: float, AHL: float = 0.0):
        self.OD600 = OD600
        self.AHL = AHL

class RiboTrace:
    def __init__(self, density: List[float], burden: float = 0.0):
        self.density = density
        self.burden = burden

class OrthogonalContext:
    def __init__(self, codon: str, ncAA: str):
        self.codon = codon.replace('T', 'U')
        self.ncAA = ncAA

class miRNA:
    def __init__(self, target_seq: str, eff: float = 0.1):
        self.target_seq = target_seq.upper().replace('T', 'U')
        self.repression_factor = eff

class Drug:
    def __init__(self, name: str, target_motif: str):
        self.name = name
        self.target_motif = target_motif

class BindingAffinity:
    def __init__(self, drug: str, ic50: float):
        self.drug = drug
        self.ic50 = ic50

class Structure:
    def __init__(self, pdb_id: str = "stub", core_stability: float = 0.0):
        self.pdb_id = pdb_id
        self.core_stability = core_stability

class Complex:
    def __init__(self, proteins: List[Protein], affinity: float):
        self.proteins = proteins
        self.affinity = affinity
