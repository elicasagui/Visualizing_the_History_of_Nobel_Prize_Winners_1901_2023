# src/visualize.py
import matplotlib
# use non-interactive backend to prevent show warnings
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_gender_count(df: pd.DataFrame):
    """Countplot of laureates by gender."""
    plt.figure()
    sns.countplot(data=df, x="sex")
    plt.title("Count of Laureates by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Laureates")
    plt.tight_layout()


def plot_us_ratio(decade_df: pd.DataFrame):
    """Line plot of US-born laureate ratio by decade."""
    plt.figure()
    sns.lineplot(data=decade_df, x="decade", y="US_born", marker="o")
    plt.title("Proportion of US-born Laureates by Decade")
    plt.xlabel("Decade")
    plt.ylabel("Proportion US-born")
    plt.tight_layout()


def plot_female_ratio(female_df: pd.DataFrame):
    """Multi-line plot of female laureate ratio by decade & category."""
    plt.figure(figsize=(8, 5))
    categories = female_df["category"].unique()
    for cat in categories:
        subset = female_df[female_df["category"] == cat]
        sns.lineplot(data=subset, x="decade", y="female", label=cat, marker="o")
    plt.title("Proportion of Female Laureates by Decade & Category")
    plt.xlabel("Decade")
    plt.ylabel("Proportion Female")
    plt.legend()
    plt.tight_layout()


def plot_multiple_winners(repeat_series: pd.Series):
    """Bar chart of individuals/organizations with >1 Nobel Prizes."""
    plt.figure(figsize=(6,4))
    repeat_series.plot(kind='bar')
    plt.title("Multiple Nobel Prize Winners")
    plt.xlabel("Name")
    plt.ylabel("Prize Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()


