# src/load_data.py

import pandas as pd

def load_nobel_data(path: str) -> pd.DataFrame:
    """
    Carga el CSV de Nobel Prize y devuelve un DataFrame de pandas.
    Lanza ValueError si faltan columnas obligatorias.
    """
    df = pd.read_csv(path)
    required_cols = ["year", "category", "full_name", "birth_country", "sex"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df
