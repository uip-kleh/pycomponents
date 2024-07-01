import os
import sys
sys.path.append(os.pardir)
from random import random
from pycomponents.system import System

if __name__ == "__main__":
    system = System()
    test_path = system.join_home_dir(fname="test")
    print(test_path)