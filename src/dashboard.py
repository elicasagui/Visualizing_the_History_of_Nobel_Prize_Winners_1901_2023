import os
import sys

# ─── Fix import path so that 'src' is on sys.path ─────────────────────────
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path[0] = project_root

import streamlit as st
import pandas as pd
from src.load_data import load_nobel_data
from src.clean_data import add_decade_column, flag_us_born, flag_female
from src.analyze import (decade_us_ratio, decade_category_female_ratio,
                         multiple_winners, most_common_gender_and_country)
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Nobel Prize Interactive Dashboard")

# Cargar y preparar los datos
data = load_nobel_data("data/nobel.csv")
data = add_decade_column(data)
data = flag_us_born(data)
data = flag_female(data)

# Sidebar filters
st.sidebar.header("Filters")
selected_decades = st.sidebar.multiselect(
    "Select Decades:",
    options=sorted(data["decade"].unique()),
    default=sorted(data["decade"].unique())
)

selected_categories = st.sidebar.multiselect(
    "Select Categories:",
    options=data["category"].unique(),
    default=data["category"].unique()
)

selected_gender = st.sidebar.radio(
    "Select Gender:",
    options=["All", "Male", "Female"],
    index=0
)

filtered_data = data[
    (data["decade"].isin(selected_decades)) &
    (data["category"].isin(selected_categories))
]

if selected_gender != "All":
    filtered_data = filtered_data[filtered_data["sex"] == selected_gender]

# Gráficos interactivos
st.header("Distribution of Nobel Laureates by Gender")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_data, x="sex", ax=ax1)
st.pyplot(fig1)

st.header("US-born Laureates Ratio Over Decades")
us_ratio_df = decade_us_ratio(filtered_data)
fig2, ax2 = plt.subplots()
sns.lineplot(data=us_ratio_df, x="decade", y="US_born", marker='o', ax=ax2)
st.pyplot(fig2)

st.header("Female Laureates by Decade & Category")
female_ratio_df = decade_category_female_ratio(filtered_data)
fig3, ax3 = plt.subplots(figsize=(8,5))
sns.lineplot(data=female_ratio_df, x="decade", y="female", hue="category", marker='o', ax=ax3)
st.pyplot(fig3)

st.header("Multiple Nobel Prize Winners")
repeat_series = multiple_winners(filtered_data)
fig4, ax4 = plt.subplots(figsize=(6,4))
repeat_series.plot(kind='bar', ax=ax4)
st.pyplot(fig4)

# Información adicional
top_gender, top_country = most_common_gender_and_country(filtered_data)
st.subheader(f"Most Common Gender: {top_gender}")
st.subheader(f"Most Common Birth Country: {top_country}")
