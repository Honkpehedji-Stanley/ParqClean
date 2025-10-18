from typing import Dict
import pandas as pd

def check_required_columns(df: pd.DataFrame, schema: Dict[str,str]):
    missing = [c for c in schema if c not in df.columns]
    if missing:
        raise ValueError(f"Colonnes manquantes: {missing}")

def check_null_threshold(df: pd.DataFrame, threshold: float = 0.5):
    bad = df.isna().mean()
    over = bad[bad > threshold]
    if not over.empty:
        raise ValueError(f"Colonnes avec trop de nulls: {over.to_dict()}")
