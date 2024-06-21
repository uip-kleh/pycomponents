import os
import sys
sys.path.append(os.pardir)
from pycomponents.draw import Draw 

class Componetns(Draw):
    def __init__(self) -> None:
        super().__init__()

if __name__ == "__main__":
    componetns = Componetns()