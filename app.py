import streamlit as st
from streamlit_option_menu import option_menu

# Set Page Title
st.set_page_config(page_title="IMH Healthcare Dashboard", page_icon="🏥", layout="wide")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Home",
        options=["Clinic Dashboard", "Clinic Data", "Patient Dashboard", "Patient Data"],
        icons=["activity", "database", "clipboard-pulse", "table"],
        menu_icon="house",
        default_index=0
    )

# Dynamically load pages based on selection
if selected == "Clinic Dashboard":
    import clinic_dashboard
    clinic_dashboard.show_page()  # Call a function from the file

elif selected == "Clinic Data":
    import clinic_data
    clinic_data.show_page()

elif selected == "Patient Dashboard":
    import patient_dashboard
    patient_dashboard.show_page()

elif selected == "Patient Data":
    import patient_data
    patient_data.show_page()
