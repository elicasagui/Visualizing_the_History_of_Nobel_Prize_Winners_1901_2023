# src/analyze.py
import pandas as pd

def most_common_gender_and_country(df: pd.DataFrame) -> tuple[str, str]:
    """
    Return (top_gender, top_birth_country) by mode.
    """
    top_gender = df["sex"].mode()[0]
    top_country = df["birth_country"].mode()[0]
    return top_gender, top_country

def decade_us_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a DataFrame with 'decade' and mean of 'US_born'.
    """
    return df.groupby("decade", as_index=False)["US_born"].mean()

def decade_category_female_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a DataFrame with 'decade', 'category', and mean of 'female'.
    """
    return df.groupby(["decade","category"], as_index=False)["female"].mean()

def multiple_winners(df: pd.DataFrame) -> pd.Series:
    """
    Return a Series of full_name counts where count > 1.
    """
    counts = df["full_name"].value_counts()
    return counts[counts > 1]
