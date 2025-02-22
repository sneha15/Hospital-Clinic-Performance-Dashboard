import streamlit as st
import pandas as pd
import time
from clinic_data import get_clinic_data # Import the data fetching function


def show_page():
    #st.title("📊 Clinic Dashboard")

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

    # Live update section
    while True:

        # Fetch the latest data
        (clinic_data_table, clinic_data) = get_clinic_data()

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
        st.write("Welcome to the Clinic Dashboard!")
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

        # Wait 20 seconds before refreshing
        interval = 20
        time.sleep(interval)
        st.rerun()


# Sidebar Filtering

    # with st.sidebar:
      #  st.header("🔍 Filter Options")
       # department = st.selectbox("Select Department", ["All", "General", "Pediatrics", "Surgery"])
       # date_range = st.date_input("Select Date Range", [])

# Display Filtered Data
#st.write(f"Showing results for Department: `{department}`")
# st.write("Dashboard content will be here...")

# min_wait_time = st.slider("Minimum Wait Time", 0, 120, 10)
# filtered_data = data[data["Wait Time"] >= min_wait_time]

# age_group = st.radio("Select Age Group", ["All", "0-18", "19-40", "40+"])
# gender = st.radio("Select Gender", ["All", "Male", "Female"])

# Display Dashboard Data
# st.write(f"Filtering for Age Group: `{age_group}`, Gender: `{gender}`")
# st.write("Patient data visualization will go here...")