# Hospital Clinic Performance Dashboard for IMH

This repository contains the files for a Streamlit-based hospital clinic performance dashboard designed for IMH.  The dashboard visualizes key metrics and data related to clinic operations, patient wait times, and satisfaction.

## Table of Contents

- [Overview](#overview)
- [Files](#files)
- [Deployment](#deployment)
- [Data](#data)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The dashboard provides insights into clinic performance using interactive visualizations and key metrics.  It is built using Streamlit, allowing for easy deployment and a user-friendly interface. The data used is synthetic, generated using a cyclical cosine function with added noise.

## Files

-   **`app.py`:** The main Streamlit application file. This file orchestrates the dashboard's layout, navigation, and imports other modules.
-   **`clinic_dashboard.py`:** Contains the code for generating the plots and displaying key metrics within the "Clinic Dashboard" section of the app.
-   **`clinic_data.py`:** Handles the display of the raw synthetic data used in the dashboard within the "Clinic Data" section.
-   **`create_synthetic_data.ipynb`:** A Jupyter Notebook used to generate the synthetic data. This notebook implements the cyclical cosine function with added random noise.
-   **`synthetic_data.csv`:** The CSV file storing the generated synthetic data. Columns include `id`, `time_of_day`, `department`, `wait_time`, `patients_waiting`, `doctors_available`, and `satisfaction_score`.
-   **`Create_database_tables.sql`:** SQL script containing the commands to create the database and table, import data, and perform updates (INSERT/UPDATE).

## Deployment

To run this application locally, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/sneha15/Hospital-Clinic-Performance-Dashboard.git](https://github.com/sneha15/Hospital-Clinic-Performance-Dashboard.git)
    cd Hospital-Clinic-Performance-Dashboard
    ```

2.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a secrets.toml file:**
   In .streamlit folder:
    ```# .streamlit/secrets.toml
    [mysql]
    host = "localhost"
    user = "root"
    password = "your_password"
    database = "hospital_data"
    ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## Data

The data used in this dashboard is synthetic and is stored in `synthetic_data.csv`.  It is generated using a cyclical cosine function with added random noise, simulating realistic patterns in hospital data.  The data can be recreated using the provided Jupyter Notebook (`create_synthetic_data.ipynb`), but it may look different as there is random noise.

To use this data with the dashboard:

1.  Download `synthetic_data.csv`.
2.  Import the data into a MySQL database:
    *   Open MySQL Workbench and connect to your local MySQL server.
    *   Open the `create_database_tables.sql` file.
    *   Create a database named `hospital_data`.
    *   Within `hospital_data`, import `synthetic_data.csv` as a table named `synthetic_data_jan_2025`.
    *   Execute the `ALTER TABLE` commands in the SQL file to modify the table structure to add an id column.

## Usage

The dashboard provides interactive visualizations and tables that update dynamically.  Changes made to the MySQL database will be reflected in the dashboard with a refresh rate of approximately every 20 seconds.

To edit or add data to the database, use the `INSERT INTO` or `UPDATE` commands within the `create_database_tables.sql` file in MySQL Workbench.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.
