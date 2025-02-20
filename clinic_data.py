# Import Relevant Librariess
import streamlit as st
import mysql.connector
import pandas as pd
import pyarrow as pa
import time


def show_page():
    st.title("Clinic Data")
    st.write("Welcome to the Clinic Data Page!")


    def get_clinic_data():

        # Database connection
        db_config = st.secrets["mysql"]
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"]
        )
        cursor = conn.cursor()

        # SQL Query
        query = "SELECT * FROM synthetic_data_jan_2025"  
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Get column names
        columns = cursor.column_names #[desc[0] for desc in cursor.description]

        # Convert to Pandas DataFrame
        clinic_data_df = pd.DataFrame(rows, columns=columns, index=None)

        # Convert to PyArrow for faster processing
        clinic_data_table = pa.Table.from_pandas(clinic_data_df)
        
        # Close the connection
        cursor.close()
        conn.close()

        return clinic_data_table

    while True:
        clinic_data_table = get_clinic_data()
        st.dataframe(clinic_data_table)
        
        # Wait 20 seconds before refreshing
        interval = 20
        time.sleep(interval)
        # Rerun the script to refresh the data
        st.rerun()
        # st.experimental_rerun()


