import pandas as pd
import pytest
import numpy as np
from src.analyze import (
    most_common_gender_and_country,
    decade_us_ratio,
    decade_category_female_ratio,
    multiple_winners,
)

def test_most_common_gender_and_country():
    df = pd.DataFrame({
        "sex": ["Male", "Female", "Female", "Male", "Female"],
        "birth_country": ["USA", "France", "France", "USA", "France"],
    })
    top_gender, top_country = most_common_gender_and_country(df)
    assert top_gender == "Female"
    assert top_country == "France"

def test_decade_us_ratio():
    # prepare a df with known US_born proportions
    df = pd.DataFrame({
        "decade": [1900, 1900, 1910, 1910, 1910],
        "US_born": [True, False, True, True, False],
    })
    result = decade_us_ratio(df)
    expected = pd.DataFrame({
        "decade": [1900, 1910],
        "US_born": [0.5, 2/3],
    })
    pd.testing.assert_frame_equal(result, expected)

def test_decade_category_female_ratio():
    # prepare a df with known female proportions per (decade, category)
    df = pd.DataFrame({
        "decade":   [1900, 1900, 1900, 1910, 1910],
        "category": ["A",   "A",   "B",   "A",   "B"],
        "female":   [True,  False, True,  True,  False],
    })
    result = decade_category_female_ratio(df)
    expected = pd.DataFrame({
        "decade":   [1900, 1900, 1910, 1910],
        "category": ["A",   "B",   "A",   "B"],
        "female":   [0.5,   1.0,   1.0,   0.0],
    })
    pd.testing.assert_frame_equal(result, expected)

def test_multiple_winners():
    df = pd.DataFrame({
        "full_name": ["X", "Y", "X", "Z", "Z", "Z"]
    })
    result = multiple_winners(df)
    # expect only those with count > 1, preserving counts
    expected = pd.Series({"X": 2, "Z": 3}, name="full_name")
    # sort indices to ensure order consistency
    pd.testing.assert_series_equal(result.sort_index(), expected.sort_index())
