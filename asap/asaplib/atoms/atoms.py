"""
define the asap xyz class
"""

import math
import numpy as np
from ase import Atoms
from ase.io import read,write

zmap = {"H": 1,"He": 2,"Li": 3,"Be": 4,"B": 5,"C": 6,"N": 7,"O": 8,"F": 9,"Ne": 10,"Na": 11,"Mg": 12,"Al": 13,"Si": 14,"P": 15,"S": 16,"Cl": 17,"Ar": 18,"K": 19,"Ca": 20,"Sc": 21,"Ti": 22,"V": 23,"Cr": 24,"Mn": 25,"Fe": 26, "Ni": 28,"Ga": 31, "As":33}

class ASAPXYZ(Atoms):
    """
    TODO: class-level docstring
    """
    def __init__(self):
        pass

    def readxyz(self):
        return self

    def readmatrix(self):
        return self

    def write(self):

    def get_name(self):
        return type(self).__name__
