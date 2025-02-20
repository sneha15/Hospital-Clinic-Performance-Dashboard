# Import Relevant Librariess
import streamlit as st
import mysql.connector
import pandas as pd

st.title("Clinic Data")

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

# Remove index
clinic_data_df.reset_index(drop=True, inplace=True)

# Display the dataframe in Streamlit
st.dataframe(clinic_data_df.style.set_properties(**{'text-align': 'center'}), width = 1500, height=400)


# Close the connection
# cursor.close()
# conn.close()


