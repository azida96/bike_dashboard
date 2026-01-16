# ===============================
# IMPORT LIBRARIES
# ===============================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# LOAD DATA (ONLY ONCE)
# ===============================
df = pd.read_csv("train.csv")

# Create required datetime features FIRST
df["datetime"] = pd.to_datetime(df["datetime"])
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["hour"] = df["datetime"].dt.hour

# ===============================
# APP TITLE
# ===============================
st.title("Bike Rental Dashboard")

st.write(
    "This interactive dashboard allows users to explore bike rental "
    "patterns by selecting different years."
)

# ===============================
# INTERACTIVE WIDGET (REQUIRED)
# ===============================
selected_year = st.selectbox(
    "Select Year",
    sorted(df["year"].unique())
)

# Filter data dynamically
filtered_df = df[df["year"] == selected_year]

# ===============================
# INTERACTIVE GRAPH (MAIN REQUIREMENT)
# ===============================
st.subheader("Mean Bike Rentals by Hour (Interactive)")

fig, ax = plt.subplots()
filtered_df.groupby("hour")["count"].mean().plot(ax=ax)
ax.
