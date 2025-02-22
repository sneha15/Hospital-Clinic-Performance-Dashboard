import streamlit as st
import pandas as pd

try:
    conn = st.connection('mysql', type='sql')  # This SHOULD now use mysqlclient

    engine = conn._engine
    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM your_table", conn)
    st.dataframe(df)

except Exception as e:
    st.error(f"Error: {e}")