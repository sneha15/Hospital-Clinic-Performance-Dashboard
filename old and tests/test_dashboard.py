import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Set page config
st.set_page_config(page_title="Clinic Dashboard", layout="wide")

# Set sidebar color and style using CSS
st.markdown(
    """
    <style>
        /* Sidebar text color and size */
        [data-testid="stSidebar"] div[role="radiogroup"], 
        [data-testid="stSidebar"] label {
            color: #000000 !important; /* Change text color (white) */
            font-size: 10px !important; /* Change font size */
        }

         /*Target slider labels*/
        [data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p{
            font-size: 20px !important;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Load data from MySQL
def load_data():
    db_config = st.secrets["mysql"]
    conn = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"]
    )
    query = "SELECT * FROM synthetic_data_jan_2025 ORDER BY time_of_day"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Load data
clinic_data = load_data()

# Convert date column
clinic_data['time_of_day'] = pd.to_datetime(clinic_data['time_of_day'])
clinic_data["hour"] = clinic_data["time_of_day"].dt.hour 
clinic_data["date"] = clinic_data["time_of_day"].dt.date

# Sidebar filters
departments = clinic_data['department'].unique()
selected_department = st.sidebar.multiselect("Select Department", departments, default=departments)
date_range = st.sidebar.date_input("Select Date Range", [clinic_data['time_of_day'].min(), clinic_data['time_of_day'].max()])

# Filter data
filtered_data = clinic_data[(clinic_data['department'].isin(selected_department)) &
                            (clinic_data['time_of_day'] >= pd.to_datetime(date_range[0])) &
                            (clinic_data['time_of_day'] < pd.to_datetime(date_range[1]))]
                             
# Layout
st.title("📊 Clinic Performance Dashboard")
st.markdown("---")

# Key Metrics
st.subheader("Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Avg Wait Time", f"{filtered_data['wait_time'].mean():.1f} min")
col2.metric("Avg Patients Waiting", f"{filtered_data['patients_waiting'].mean():.2f}")
col3.metric("Avg Doctors Available", f"{filtered_data['doctors_available'].mean():.2f}")
col4.metric("Avg Satisfaction Score", f"{filtered_data['satisfaction_score'].mean():.2f}")
col5.metric("Peak Wait Time", f"{filtered_data['wait_time'].max()} min")

# More insights
busiest_hour = filtered_data.groupby("hour")["patients_waiting"].sum().idxmax()
least_busy_hour = filtered_data.groupby("hour")["patients_waiting"].sum().idxmin()

st.subheader("Additional Insights")
st.write(f"**Busiest Hour:** {busiest_hour}:00")
st.write(f"**Least Busy Hour:** {least_busy_hour}:00")

st.markdown("---")

# Visualizations
# Line Chart: Wait Time Trend
st.subheader("📈 Wait Time Over Time")
fig1 = px.line(filtered_data, x='time_of_day', y='wait_time', color='department', title="Wait Time Trend")
st.plotly_chart(fig1, use_container_width=True)

# Bar Chart: Average Wait Time by Day
st.subheader("📊 Average Wait Time per day")
fig2 = px.bar(filtered_data.groupby("date")["wait_time"].mean().reset_index(), x="date", y="wait_time", title="Average Wait Time per Day")
st.plotly_chart(fig2, use_container_width=True)

# Line Chart: Satisfaction Score Trend
st.subheader("📈 Satisfaction Score Over Time")
fig3 = px.line(filtered_data, x='time_of_day', y='satisfaction_score', color='department', title="Satisfaction Score Trend")
st.plotly_chart(fig3, use_container_width=True)

# Box Plot: Satisfaction Score Distribution
st.subheader("📊 Satisfaction Score Distribution")
fig4 = px.box(filtered_data, x='department', y='satisfaction_score', title="Satisfaction Score by Department")
st.plotly_chart(fig4, use_container_width=True)

# Bar Chart: Patients Waiting and Doctor Availability
st.subheader("🔍 Patients Waiting & Doctors Available")
fig5 = px.bar(filtered_data, x='time_of_day', y=['patients_waiting', 'doctors_available'], barmode='group', title="Patients vs Doctors Over Time")
st.plotly_chart(fig5, use_container_width=True)

# Heatmap of wait times per hour per department
st.subheader("🕒 Heatmap of Wait Times")
fig6 = px.density_heatmap(filtered_data, x='hour', y='department', z='wait_time', histfunc='avg', color_continuous_scale="Hot", title="Wait Time by Hour")
st.plotly_chart(fig6, use_container_width=True)

# Scatter Plot: Wait Time vs Satisfaction Scores
st.subheader("📌 Scatter Plot: Wait Time vs Satisfaction Scores")
fig7 = px.scatter(filtered_data, x='wait_time', y='satisfaction_score', color='department', title="Wait Time vs Satisfaction")
st.plotly_chart(fig7, use_container_width=True)

# Pie chart of patient distribution across clinics
st.subheader("📊 Patients Distribution Across Clinics")
fig8 = px.pie(filtered_data, names='department', values='patients_waiting', title="Patients Waiting per Clinic")
st.plotly_chart(fig8, use_container_width=True)
