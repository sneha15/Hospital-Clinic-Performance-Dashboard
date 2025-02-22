# Create database
# CREATE DATABASE hospital_data;

# Use the database
USE hospital_data;

# Add an index column to the database to make it easier to access
ALTER TABLE synthetic_data_jan_2025 ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;

# Make the id column the first column
ALTER TABLE synthetic_data_jan_2025 MODIFY COLUMN id INT AUTO_INCREMENT FIRST;


# Display the data
SELECT *
FROM synthetic_data_jan_2025;

# Add values to the data
INSERT INTO synthetic_data_jan_2025 (id, time_of_day, department, wait_time, patients_waiting, doctors_available, satisfaction_score) 
VALUES (2164, '2025-01-31 01:00:00', 'Memory Clinic', 1.0, 0, 5, 4.9);  

# Delete values from the data
DELETE FROM synthetic_data_jan_2025
WHERE id = 2164;

# Edit values in data
UPDATE synthetic_data_jan_2025
SET satisfaction_score = 4.3
WHERE id = 1;
# WHERE time_of_day = '2025-01-31 00:00:00' AND department = 'Memory Clinic';