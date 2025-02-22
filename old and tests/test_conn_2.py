import streamlit as st
import pandas as pd
import sqlalchemy

try:
    # Option 1: Try importing the dialect directly (more robust):
    from sqlalchemy.dialects import mysql

    # Option 2: Let SQLAlchemy find it (might be less robust):
    # engine = sqlalchemy.create_engine(
    #     "mysql+mysqlclient://your_user:your_password@your_host/your_database"
    # )

    engine = sqlalchemy.create_engine(
        "mysql+mysqlclient://root:@localhost/hospital_data"
    )


    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM synthetic_data_jan_2025", conn)
    st.dataframe(df)

except ImportError as e:
    st.error(f"ImportError: {e}. Please ensure mysqlclient and sqlalchemy are installed.")
except sqlalchemy.exc.OperationalError as e:  # Catch connection errors
    st.error(f"OperationalError: {e}. Check your connection details (user, password, host, database).")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")