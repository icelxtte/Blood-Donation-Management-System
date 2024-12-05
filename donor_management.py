#Programmer:Sachorra Douglas
#Date: 11/28/2024

import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leavemealone45@",
    database="blood_donation_system"
)

# Create a cursor object
cursor = db_connection.cursor()

# Function to update a donor
def update_donor(donor_id, name, age, gender, blood_type_id):
    cursor.execute(
        "UPDATE Donors SET name = %s, age = %s, gender = %s, blood_type_id = %s WHERE id = %s",
        (name, age, gender, blood_type_id, donor_id)
    )
    db_connection.commit()
    print(f"Donor with ID {donor_id} updated successfully.")

# Function to add new donors
def add_donor(name, age, gender, contact_number, blood_type_id):
    cursor.execute(
        "INSERT INTO Donors (name, age, gender, contact_number, blood_type_id) VALUES (%s, %s, %s, %s, %s)",
        (name, age, gender, contact_number, blood_type_id)
    )
    db_connection.commit()
    print(f"Donor {name} added successfully.")

# Update John Doe to Sachorra Douglas
update_donor(1, 'Sachorra Douglas', 20, 'Female', 9)

# Add 19 new donors with custom random names
donors = [
    ('John Doe', 25, 'Male', '555-1234', 1),   # A+
    ('Jane Smith', 29, 'Female', '555-5678', 2), # A-
    ('Michael Johnson', 35, 'Male', '555-8765', 3),   # B+
    ('Emily Davis', 40, 'Female', '555-2345', 4), # B-
    ('David Miller', 22, 'Male', '555-6789', 5),   # AB+
    ('Sarah Wilson', 27, 'Female', '555-3456', 6), # AB-
    ('Daniel Lee', 50, 'Male', '555-9876', 7),   # O+
    ('Olivia Clark', 38, 'Female', '555-4321', 8), # O-
    ('James Walker', 28, 'Male', '555-8765', 1),   # A+
    ('Sophia Hall', 33, 'Female', '555-1357', 2), # A-
    ('William Allen', 45, 'Male', '555-2468', 3),   # B+
    ('Mia Young', 31, 'Female', '555-3579', 4), # B-
    ('Joshua King', 26, 'Male', '555-3698', 5),   # AB+
    ('Isabella Wright', 37, 'Female', '555-7410', 6), # AB-
    ('Matthew Scott', 48, 'Male', '555-8520', 7),   # O+
    ('Charlotte Adams', 30, 'Female', '555-9631', 8), # O-
    ('Ethan Harris', 29, 'Male', '555-1847', 1),   # A+
    ('Amelia Robinson', 25, 'Female', '555-7159', 2), # A-
    ('Alexander Carter', 40, 'Male', '555-1236', 3),   # B+
    ('Madison Mitchell', 34, 'Female', '555-6543', 4), # B-
    ('Benjamin Perez', 20, 'Male', '555-1470', 5)    # AB+
]

# Loop through and add all new donors
for donor in donors:
    add_donor(*donor)

# Close the connection
cursor.close()
db_connection.close()
