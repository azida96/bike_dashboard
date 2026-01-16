import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

df["datetime"] = pd.to_datetime(df["datetime"])
df["year"] = df["datetime"].dt.year
df["hour"] = df["datetime"].dt.hour
df["month"] = df["datetime"].dt.month


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
st.subheader("Mean Bike Rentals by Month")

fig2, ax2 = plt.subplots()
filtered_df.groupby("month")["count"].mean().plot(marker="o", ax=ax2)
ax2.set_xlabel("Month")
ax2.set_ylabel("Mean Rentals")
ax2.set_title(f"Year: {year}")

st.pyplot(fig2)
st.subheader("Mean Bike Rentals by Weather")

fig3, ax3 = plt.subplots()
sns.barplot(
    data=filtered_df,
    x="weather",
    y="count",
    errorbar=("ci", 95),
    ax=ax3
)
ax3.set_xlabel("Weather")
ax3.set_ylabel("Mean Rentals")

st.pyplot(fig3)
st.subheader("Correlation Heatmap")

fig4, ax4 = plt.subplots(figsize=(8, 6))
sns.heatmap(
    filtered_df.corr(numeric_only=True),
    cmap="coolwarm",
    ax=ax4
)
st.pyplot(fig4)
