import streamlit as st

def show_page():
    st.title("📊 Clinic Dashboard")
    st.write("Welcome to the Clinic Dashboard!")


# Sidebar Filtering
    with st.sidebar:
        st.header("🔍 Filter Options")
        department = st.selectbox("Select Department", ["All", "General", "Pediatrics", "Surgery"])
        date_range = st.date_input("Select Date Range", [])

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