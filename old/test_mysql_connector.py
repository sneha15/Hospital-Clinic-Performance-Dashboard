import streamlit as st
import mysql.connector

st.title("Hello World")

# Debugging Database connection

db_config = st.secrets["mysql"]

try:
    conn = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"]
    )
    cursor = conn.cursor()
    st.success("Connection successful!")
except Exception as e:
    st.error(f"Connection error: {e}")
