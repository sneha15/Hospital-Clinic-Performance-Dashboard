import streamlit as st
import pandas as pd
import sqlalchemy

try:
    engine = sqlalchemy.create_engine(
        "mysql+mysqlclient://root:@localhost/hospital_data"  # Correct connection string
    )

    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM synthetic_data_jan_2025", conn)  # Replace your_table
    st.dataframe(df)

except Exception as e:
    st.error(f"Error: {e}")