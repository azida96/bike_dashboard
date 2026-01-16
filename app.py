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

# Create datetime features FIRST
df["datetime"] = pd.to_datetime(df["datetime"])
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["hour"] = df["datetime"].dt.hour

# ===============================
# APP TITLE
# ===============================
st.title("Bike Rental Dashboard")

st.write(
    "This interactive Streamlit dashboard allows users to explore bike rental "
    "patterns dynamically by selecting a year."
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

st.write("Change the year to see the graphs update automatically.")

# ===============================
# INTERACTIVE GRAPH 1
# ===============================
st.subheader("Mean Bike Rentals by Hour (Interactive)")

fig1, ax1 = plt.subplots()
filtered_df.groupby("hour")["count"].mean().plot(ax=ax1)
ax1.set_xlabel("Hour of Day")
ax1.set_ylabel("Mean Rentals")
ax1.set_title(f"Year: {selected_year}")
st.pyplot(fig1)

# ===============================
# GRAPH 2
# ===============================
st.subheader("Mean Bike Rentals by Month")

fig2, ax2 = plt.subplots()
filtered_df.groupby("month")["count"].mean().plot(marker="o", ax=ax2)
ax2.set_xlabel("Month")
ax2.set_ylabel("Mean Rentals")
ax2.set_title(f"Year: {selected_year}")
st.pyplot(fig2)

# ===============================
# GRAPH 3
# ===============================
st.subheader("Mean Bike Rentals by Weather")

fig3, ax3 = plt.subplots()
sns.barplot(
    data=filtered_df,
    x="weather",
    y="count",
    errorbar=("ci", 95),
    ax=ax3
)
ax3.set_xlabel("Weather Category")
ax3.set_ylabel("Mean Rentals")
st.pyplot(fig3)

# ===============================
# GRAPH 4
# ===============================
st.subheader("Correlation Heatmap")

fig4, ax4 = plt.subplots(figsize=(8, 6))
sns.heatmap(
    filtered_df.corr(numeric_only=True),
    cmap="coolwarm",
    ax=ax4
)
st.pyplot(fig4)
