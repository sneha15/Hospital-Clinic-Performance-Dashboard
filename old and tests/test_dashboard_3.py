import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load data
df = pd.read_csv("synthetic_data.csv")
df["time_of_day"] = pd.to_datetime(df["time_of_day"])
df["hour"] = df["time_of_day"].dt.hour
df["date"] = df["time_of_day"].dt.date

def filter_data(department, start_date, end_date):
    mask = (
        (df["department"] == department)
        & (df["time_of_day"] >= pd.to_datetime(start_date))
        & (df["time_of_day"] <= pd.to_datetime(end_date))
    )
    return df[mask]

# Streamlit app setup
st.set_page_config(page_title="Clinic Dashboard", layout="wide")
st.title("Clinic Dashboard")

# Sidebar filters
department = st.sidebar.selectbox("Select Department", df["department"].unique())
start_date = st.sidebar.date_input("Start Date", df["time_of_day"].min().date())
end_date = st.sidebar.date_input("End Date", df["time_of_day"].max().date())
filtered_df = filter_data(department, start_date, end_date)

# Key Metrics
st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Average Wait Time", round(filtered_df["wait_time"].mean(), 2))
col2.metric("Total Patients Seen", len(filtered_df))
col3.metric("Average Doctors Available", round(filtered_df["doctors_available"].mean(), 2))
col4.metric("Peak Wait Time", filtered_df["wait_time"].max())

# More insights
busiest_hour = filtered_df.groupby("hour")["patients_waiting"].sum().idxmax()
least_busy_hour = filtered_df.groupby("hour")["patients_waiting"].sum().idxmin()
worst_satisfaction = filtered_df.groupby("department")["satisfaction_score"].mean().idxmin()
best_satisfaction = filtered_df.groupby("department")["satisfaction_score"].mean().idxmax()
correlation = round(filtered_df["wait_time"].corr(filtered_df["satisfaction_score"]), 2)

st.subheader("Additional Insights")
st.write(f"**Busiest Hour:** {busiest_hour}:00")
st.write(f"**Least Busy Hour:** {least_busy_hour}:00")
st.write(f"**Best Satisfaction Clinic:** {best_satisfaction}")
st.write(f"**Worst Satisfaction Clinic:** {worst_satisfaction}")
st.write(f"**Correlation Between Wait Time & Satisfaction:** {correlation}")

# Visualizations
st.subheader("Visualizations")

# Line Chart: Wait Time Trend
fig1 = px.line(filtered_df, x="time_of_day", y="wait_time", color="department", title="Wait Time Trend")
st.plotly_chart(fig1, use_container_width=True)

# Bar Chart: Average Wait Time by Day
fig2 = px.bar(filtered_df.groupby("date")["wait_time"].mean().reset_index(), x="date", y="wait_time", title="Average Wait Time per Day")
st.plotly_chart(fig2, use_container_width=True)

# Heatmap: Average Wait Time by Hour
heatmap_fig = px.density_heatmap(filtered_df, x="hour", y="wait_time", z="patients_waiting", color_continuous_scale="Viridis", title="Wait Time Heatmap")
st.plotly_chart(heatmap_fig, use_container_width=True)

# Scatter Plot: Wait Time vs. Satisfaction
fig3 = px.scatter(filtered_df, x="wait_time", y="satisfaction_score", color="department", title="Wait Time vs. Satisfaction Score")
st.plotly_chart(fig3, use_container_width=True)
