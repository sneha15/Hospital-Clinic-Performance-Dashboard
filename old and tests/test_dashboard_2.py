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
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.max.time())
    mask = (
        (df["department"] == department)
        & (df["time_of_day"] >= start_datetime)
        & (df["time_of_day"] <= end_datetime)
    )
    return df[mask]

# Streamlit app setup
st.title("Clinic Dashboard")

department = st.selectbox("Select Department", df["department"].unique())
start_date = st.date_input("Start Date", df["time_of_day"].min().date())
end_date = st.date_input("End Date", df["time_of_day"].max().date())
filtered_df = filter_data(department, start_date, end_date)

# Line charts
st.subheader("Line Charts")
st.plotly_chart(px.line(df, x="time_of_day", y="wait_time", color="department", title="Wait Time Trend"))
st.plotly_chart(px.line(df, x="time_of_day", y="patients_waiting", color="department", title="Patients Waiting"))
st.plotly_chart(px.line(df, x="time_of_day", y="doctors_available", color="department", title="Doctors Available"))
st.plotly_chart(px.line(df, x="time_of_day", y="satisfaction_score", color="department", title="Satisfaction Scores"))

# Bar charts
st.subheader("Bar Charts")
st.plotly_chart(px.bar(df.groupby("department")["wait_time"].mean().reset_index(), x="department", y="wait_time", title="Average Wait Time by Department"))
st.plotly_chart(px.bar(df.groupby("department")["patients_waiting"].mean().reset_index(), x="department", y="patients_waiting", title="Average Patients Waiting by Department"))
st.plotly_chart(px.bar(df.groupby("department")["doctors_available"].mean().reset_index(), x="department", y="doctors_available", title="Average Doctors Available by Department"))
st.plotly_chart(px.bar(df.groupby("department")["satisfaction_score"].mean().reset_index(), x="department", y="satisfaction_score", title="Average Satisfaction Score by Department"))

# Key values
st.subheader("Key Metrics")
st.metric("Current Average Wait Time", round(filtered_df["wait_time"].mean(), 2))
st.metric("Current Average Patients Waiting", round(filtered_df["patients_waiting"].mean(), 2))
st.metric("Current Average Number of Doctors", round(filtered_df["doctors_available"].mean(), 2))
st.metric("Current Average Satisfaction Score", round(filtered_df["satisfaction_score"].mean(), 2))

# Heatmap
st.subheader("Heatmap")
heatmap_fig = px.density_heatmap(
    filtered_df,
    x="hour",
    y="wait_time",
    z="patients_waiting",
    color_continuous_scale="Viridis",
    title="Wait Time Heatmap",
)
st.plotly_chart(heatmap_fig)
