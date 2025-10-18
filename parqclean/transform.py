import pandas as pd
import re

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [re.sub(r'\W+', '_', c.strip()).lower() for c in df.columns]
    return df

def convert_dates(df: pd.DataFrame, date_cols):
    for c in date_cols:
        df[c] = pd.to_datetime(df[c], errors='coerce')
    return df

def drop_duplicates(df: pd.DataFrame, subset=None):
    return df.drop_duplicates(subset=subset)
