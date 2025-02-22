import streamlit as st
import pandas as pd
import time
from clinic_data import get_clinic_data # Import the data fetching function


def show_page():
    st.title("📊 Clinic Dashboard")
    st.write("Welcome to the Clinic Dashboard!")

    # Live update section
    while True:
        # Fetch the latest data
        (clinic_data_table, clinic_data_df) = get_clinic_data()

        # Display key metrics
        #total_patients = clinic_data_df["patients_waiting"].sum()
        #avg_wait_time = clinic_data_df["wait_time"].mean()
        #avg_satisfaction = clinic_data_df["satisfaction_score"].mean()

        # Create a metric display
        #col1, col2, col3 = st.columns(3)
        #col1.metric("Total Patients Waiting", total_patients)
        #col2.metric("Avg. Wait Time (mins)", f"{avg_wait_time:.2f}")
        #col3.metric("Avg. Satisfaction Score", f"{avg_satisfaction:.1f}")

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