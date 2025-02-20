import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(initial_sidebar_state="collapsed")

st.title("Testing Streamlit Option Menu")

selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Dashboard", "Settings"],
    icons=["house", "bar-chart", "gear"],
    menu_icon="cast",
    default_index=0
)

st.write(f"Selected: {selected}")
