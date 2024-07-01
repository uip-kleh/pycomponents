import os
import sys

class System:
    home_path = os.environ["HOME"]

    def __init__(self) -> None:
        pass

    def join_home_dir(self, fname: str):
        fname = os.path.join(self.home_path, fname)
        self.make_dir(fname)
        return fname

    def dir_exists(self, fname: str):
        if os.path.exists(fname): return True
        return False
    
    def make_dir(self, fname: str):
        if not self.dir_exists(fname):
            os.mkdir(fname)