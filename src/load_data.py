import pandas as pd

def load_nobel_data(path: str) -> pd.DataFrame:
    """
    Carga el CSV de Nobel Prize y devuelve un DataFrame de pandas.
    """
    return pd.read_csv(path)
