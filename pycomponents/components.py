import os
import sys
sys.path.append(os.pardir)
from pycomponents.system import System
from pycomponents.io import IO
from pycomponents.draw import Draw 

class Componetns(System, IO, Draw):
    def __init__(self) -> None:
        super().__init__()

if __name__ == "__main__":
    componetns = Componetns()