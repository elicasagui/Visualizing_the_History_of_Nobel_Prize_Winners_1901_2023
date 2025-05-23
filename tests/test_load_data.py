# tests/test_load_data.py
import pytest
import pandas as pd
from src.load_data import load_nobel_data

def test_load_success(tmp_path):
    # Crea un CSV temporal válido
    data = {
        "year": [1901],
        "category": ["Physics"],
        "full_name": ["Wilhelm Röntgen"],
        "sex": ["Male"],
        "birth_country": ["Germany"]
    }
    file = tmp_path / "nobel_test.csv"
    pd.DataFrame(data).to_csv(file, index=False)

    df = load_nobel_data(str(file))
    assert df.shape[0] == 1
    assert set(["year","category","full_name","sex","birth_country"]).issubset(df.columns)

def test_missing_columns(tmp_path):
    # CSV sin la columna 'sex'
    data = {
        "year": [1901],
        "category": ["Physics"],
        "full_name": ["Wilhelm Röntgen"],
        "birth_country": ["Germany"]
    }
    file = tmp_path / "bad.csv"
    pd.DataFrame(data).to_csv(file, index=False)

    with pytest.raises(ValueError):
        load_nobel_data(str(file))
