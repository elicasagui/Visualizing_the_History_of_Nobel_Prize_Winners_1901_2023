# test_clean_data.py

import pandas as pd
import numpy as np


def add_decade_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a 'decade' column by rounding down the 'year' to the nearest decade.
    """
    # Make a copy to avoid modifying the original DataFrame
    df = df.copy()
    # Calculate decade by dividing the year by 10, flooring, multiplying back, and converting to int
    df["decade"] = (np.floor(df["year"] / 10) * 10).astype(int)
    return df


def flag_us_born(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a boolean 'US_born' column indicating if birth_country is USA.
    """
    # Copy DataFrame to preserve original data
    df = df.copy()
    # Create a boolean column: True if birth_country equals 'United States of America'
    df["US_born"] = df["birth_country"] == "United States of America"
    return df


def flag_female(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a boolean 'female' column based on the 'sex' column.
    """
    # Duplicate DataFrame to prevent side-effects
    df = df.copy()
    # Compare lowercase of 'sex' to 'female' for a case-insensitive flag
    df["female"] = df["sex"].str.lower() == "female"
    return df
