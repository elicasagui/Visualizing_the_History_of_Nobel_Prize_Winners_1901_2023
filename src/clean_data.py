# src/clean_data.py
import pandas as pd
import numpy as np

def add_decade_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a 'decade' column by rounding down the 'year' to the nearest decade.
    """
    df = df.copy()
    df["decade"] = (np.floor(df["year"] / 10) * 10).astype(int)
    return df

def flag_us_born(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a boolean 'US_born' column indicating if birth_country is USA.
    """
    df = df.copy()
    df["US_born"] = df["birth_country"] == "United States of America"
    return df

def flag_female(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a boolean 'female' column based on 'sex'.
    """
    df = df.copy()
    df["female"] = df["sex"].str.lower() == "female"
    return df
