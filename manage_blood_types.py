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


# Function to add all blood types to the Blood_Types table
def add_all_blood_types():
    blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

    for blood_type in blood_types:
        cursor.execute("SELECT id FROM Blood_Types WHERE blood_type = %s", (blood_type,))
        existing = cursor.fetchall()  # Fetch all results to clear the buffer
        if not existing:
            cursor.execute("INSERT INTO Blood_Types (blood_type) VALUES (%s)", (blood_type,))
            db_connection.commit()
            print(f"Blood type '{blood_type}' added successfully.")
        else:
            print(f"Blood type '{blood_type}' already exists.")


# Function to assign unique blood types to existing donors
def assign_unique_blood_types_to_donors():
    # Fetch all blood type IDs
    cursor.execute("SELECT id, blood_type FROM Blood_Types")
    blood_types = cursor.fetchall()  # List of tuples [(1, 'A+'), (2, 'A-'), ...]

    # Fetch all donors
    cursor.execute("SELECT id, name FROM Donors")
    donors = cursor.fetchall()  # List of donors [(1, 'John Doe'), ...]

    # Check if we have enough blood types for the donors
    if len(donors) > len(blood_types):
        print("Not enough blood types to assign unique ones to all donors.")
        return

    # Assign unique blood types to donors
    for i, donor in enumerate(donors):
        donor_id, donor_name = donor
        blood_type_id, blood_type = blood_types[i]  # Get a unique blood type
        cursor.execute(
            "UPDATE Donors SET blood_type_id = %s WHERE id = %s", (blood_type_id, donor_id)
        )
        print(f"Assigned blood type '{blood_type}' to donor '{donor_name}'.")
        db_connection.commit()


# Add all blood types
add_all_blood_types()

# Assign unique blood types to donors
assign_unique_blood_types_to_donors()
