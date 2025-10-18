import pandas as pd
from pathlib import Path
from typing import List

def read_csv_files(paths: List[str]) -> pd.DataFrame:
    dfs = []
    for p in paths:
        df = pd.read_csv(p, low_memory=False)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)
