import streamlit as st
# import sys

st.title("Hello World")
# st.header("This is my first app")
# st.markdown("This is what a markdown looks like")
# st.write("Now i am trying st.write. It looks the same as a markdown")

# st.write(sys.path)

# debug streamlit app

st.write(f"Streamlit version: {st.__version__}")  # Check version in app

try:
    conn = st.connection('mysql', type='sql')
    st.success("Connection successful (if you see this)")
except Exception as e:
    st.error(f"Connection error: {e}")

# Initialize connection.
# conn = st.connection('mysql', type='sql')

# Perform query.
# df = conn.query('SELECT * from synthetic_data_jan_2025;', ttl=600)
