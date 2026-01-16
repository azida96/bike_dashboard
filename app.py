import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

df["datetime"] = pd.to_datetime(df["datetime"])
df["year"] = df["datetime"].dt.year
df["hour"] = df["datetime"].dt.hour

st.title("Bike Rental Dashboard")

year = st.selectbox(
    "Select Year",
    sorted(df["year"].unique())
)

filtered_df = df[df["year"] == year]

fig, ax = plt.subplots()
filtered_df.groupby("hour")["count"].mean().plot(ax=ax)
ax.set_xlabel("Hour")
ax.set_ylabel("Mean Rentals")
ax.set_title(f"Year: {year}")

st.pyplot(fig)
