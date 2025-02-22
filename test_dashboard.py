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
    query = "SELECT * FROM synthetic_data_jan_2025"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Load data
clinic_data = load_data()

# Convert date column
clinic_data['time_of_day'] = pd.to_datetime(clinic_data['time_of_day'])
clinic_data["hour"] = clinic_data["time_of_day"].dt.hour 

# Sidebar filters
departments = clinic_data['department'].unique()
selected_department = st.sidebar.multiselect("Select Department", departments, default=departments)
date_range = st.sidebar.date_input("Select Date Range", [clinic_data['time_of_day'].min(), clinic_data['time_of_day'].max()])

# Filter data
filtered_data = clinic_data[(clinic_data['department'].isin(selected_department)) &
                            (clinic_data['time_of_day'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))]

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
st.subheader("📈 Wait Time Over Time")
fig1 = px.line(filtered_data, x='time_of_day', y='wait_time', color='department', title="Wait Time Trend")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("📊 Satisfaction Score Distribution")
fig2 = px.box(filtered_data, x='department', y='satisfaction_score', title="Satisfaction Score by Department")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🔍 Patients Waiting & Doctors Available")
fig3 = px.bar(filtered_data, x='time_of_day', y=['patients_waiting', 'doctors_available'], barmode='group', title="Patients vs Doctors Over Time")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("🕒 Heatmap of Wait Times")
fig4 = px.density_heatmap(filtered_data, x='hour', y='department', z='wait_time', histfunc='avg', title="Wait Time by Hour")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("📌 Scatter Plot: Wait Time vs Satisfaction Scores")
fig5 = px.scatter(filtered_data, x='wait_time', y='satisfaction_score', color='department', title="Wait Time vs Satisfaction")
st.plotly_chart(fig5, use_container_width=True)

st.subheader("📊 Patients Distribution Across Clinics")
fig6 = px.pie(filtered_data, names='department', values='patients_waiting', title="Patients Waiting per Clinic")
st.plotly_chart(fig6, use_container_width=True)
