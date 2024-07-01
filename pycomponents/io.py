import os
import sys
import pandas as pd
import json

class IO:
    def __init__(self) -> None:
        pass

    def load_csv_as_dict(self, fname) -> dict:
        return pd.read_csv(fname).to_dict(orient="list")

    def save_dict_as_dataframe(self, obj: dict, fname):
        pd.DataFrame(obj).to_csv(fname, index_label=False)

    def save_obj_as_json(self, obj, fname) -> None:
        with open(fname, "w") as f:
            json.dump(obj, f, indent=2)

if __name__ == "__main__":
    io = IO()