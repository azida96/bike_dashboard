import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("train.csv")

df["datetime"] = pd.to_datetime(df["datetime"])
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["hour"] = df["datetime"].dt.hour

# ===============================
# TITLE
# ===============================
st.title("Bike Rental Dashboard")

# ===============================
# ALL SLICERS (FILTERS)
# ===============================
st.sidebar.header("Filters")

year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["year"].unique())
)

month = st.sidebar.selectbox(
    "Select Month",
    sorted(df["month"].unique())
)

hour_range = st.sidebar.slider(
    "Select Hour Range",
    min_value=0,
    max_value=23,
    value=(0, 23)
)

working_day = st.sidebar.checkbox("Show only working days")
show_filtered = st.checkbox("Show filtered data (use slicers)")





# ===============================
# APPLY FILTERS
# ===============================
filtered_df = df[
    (df["year"] == year) &
    (df["month"] == month) &
    (df["hour"].between(hour_range[0], hour_range[1]))
]

if working_day:
    filtered_df = filtered_df[filtered_df["workingday"] == 1]
    plot_df = filtered_df if show_filtered else df


st.subheader("Bike rental dataset preview")
st.dataframe(plot_df.head(20))


# ===============================
# GRAPH 1 (INTERACTIVE)
# ===============================
st.subheader("Mean Rentals by Hour")

fig1, ax1 = plt.subplots()
plot_df.groupby("hour")["count"].mean().plot(ax=ax)
ax1.set_xlabel("Hour")
ax1.set_ylabel("Mean Rentals")
st.pyplot(fig1)

# ===============================
# GRAPH 2
# ===============================
st.subheader("Mean Rentals by Month")

fig2, ax2 = plt.subplots()
plot_df.groupby("month")["count"].mean().plot(marker="o", ax=ax2)
ax2.set_xlabel("Month")
ax2.set_ylabel("Mean Rentals")
st.pyplot(fig2)

# ===============================
# GRAPH 3
# ===============================
st.subheader("Mean Rentals by Weather")

fig3, ax3 = plt.subplots()
sns.barplot(data=plot_df, x="weather", y="count", ax=ax3)
st.pyplot(fig3)

# ===============================
# GRAPH 4
# ===============================
st.subheader("Correlation Heatmap")

fig4, ax4 = plt.subplots(figsize=(8, 6))
sns.heatmap(plot_df.corr(numeric_only=True), ax=ax4)
st.pyplot(fig4)
