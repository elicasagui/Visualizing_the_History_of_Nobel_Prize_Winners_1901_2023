# src/analyze.py
import pandas as pd

def most_common_gender_and_country(df: pd.DataFrame) -> tuple[str, str]:
    """
    Return the most common gender and birth country as a tuple (gender, country).
    """
    top_gender = df["sex"].mode()[0]
    top_country = df["birth_country"].mode()[0]
    return top_gender, top_country

def decade_us_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a DataFrame with columns 'decade' and the mean of the 'US_born' boolean flag.
    """
    return df.groupby("decade", as_index=False)["US_born"].mean()

def decade_category_female_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a DataFrame with columns 'decade', 'category', and the mean of the 'female' boolean flag.
    """
    return df.groupby(["decade", "category"], as_index=False)["female"].mean()

def multiple_winners(df: pd.DataFrame) -> pd.Series:
    """
    Return a pandas Series of counts for each 'full_name' that appears more than once.
    The Series index will be the laureate name and its name attribute set to 'full_name'.
    """
    counts = df["full_name"].value_counts()
    result = counts[counts > 1]
    # Ensure the Series index has no name and the Series is named 'full_name'
    result.index.name = None
    result.name = "full_name"
    return result

