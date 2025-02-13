# create database
# CREATE DATABASE hospital_data;
USE hospital_data;

# display the data
SELECT *
FROM synthetic_data_jan_2025;

# add values to the data
# INSERT INTO synthetic_data_jan_2025 (time_of_day, department, wait_time, patients_waiting, doctors_available, satisfaction_score) 
# VALUES ('2025-01-31 01:00:00', 'Memory Clinic', 1.0, 0, 5, 4.9);  

# edit values in data
# UPDATE synthetic_data_jan_2025
# SET satisfaction_score = 1.0
# WHERE time_of_day = '2025-01-31 00:00:00' AND department = 'Memory Clinic';