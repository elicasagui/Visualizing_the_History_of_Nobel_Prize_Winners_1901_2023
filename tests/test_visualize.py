import matplotlib
matplotlib.use("Agg")  # use non-interactive backend for testing

import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.visualize import (
    plot_gender_count,
    plot_us_ratio,
    plot_female_ratio,
    plot_multiple_winners,
)

@pytest.fixture(autouse=True)
def close_figures():
    # close any existing figures before each test
    plt.close("all")
    yield
    plt.close("all")

def test_plot_gender_count_creates_figure():
    df = pd.DataFrame({"sex": ["Male", "Female", "Female", "Male"]})
    # no exception
    plot_gender_count(df)
    # one new figure should exist
    figs = plt.get_fignums()
    assert len(figs) == 1

def test_plot_us_ratio_creates_lineplot():
    decade_df = pd.DataFrame({
        "decade": [1900, 1910, 1920],
        "US_born": [0.2, 0.5, 0.8],
    })
    plot_us_ratio(decade_df)
    figs = plt.get_fignums()
    assert len(figs) == 1
    ax = plt.gca()
    # check that there is exactly one line in the axes
    lines = ax.get_lines()
    assert len(lines) == 1
    # check that markers are present
    assert all(line.get_marker() != "" for line in lines)

def test_plot_female_ratio_creates_multiple_lines():
    female_df = pd.DataFrame({
        "decade":   [1900, 1900, 1910, 1910],
        "category": ["A",   "B",   "A",   "B"],
        "female":   [0.1,   0.2,   0.3,   0.4],
    })
    plot_female_ratio(female_df)
    figs = plt.get_fignums()
    assert len(figs) == 1
    ax = plt.gca()
    # there should be one Line2D per category
    lines = ax.get_lines()
    assert len(lines) == female_df["category"].nunique()
    # legend should show both categories
    labels = [t.get_text() for t in ax.get_legend().get_texts()]
    assert set(labels) == set(female_df["category"].unique())

def test_plot_multiple_winners_creates_bar_chart():
    repeat_series = pd.Series({"Alice": 2, "Bob": 3, "Carol": 1})
    # ensure we only plot those >1 if user-selected, but function will plot all
    plot_multiple_winners(repeat_series)
    figs = plt.get_fignums()
    assert len(figs) == 1
    ax = plt.gca()
    # bars should match length of the series
    bars = ax.patches
    assert len(bars) == len(repeat_series)
    # x-tick labels should match series index
    xticks = [t.get_text() for t in ax.get_xticklabels()]
    assert set(xticks) == set(repeat_series.index.astype(str))
