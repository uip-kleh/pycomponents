import os
import sys
sys.path.append(os.pardir)
from random import random
from pycomponents.io import IO

if __name__ == "__main__":
    io = IO()
    df_dict = io.load_csv_as_dict("test.csv")
    print(df_dict)
    io.save_obj_as_json(obj=df_dict, fname="test.json")