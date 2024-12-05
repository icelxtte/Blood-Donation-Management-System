#Programmer:Sachorra Douglas
#Date: 11/28/2024


import mysql.connector
from datetime import datetime

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leavemealone45@",
    database="blood_donation_system"
)

# Create a cursor object
cursor = db_connection.cursor()


# Function to insert a new blood donor
def add_donor(name, age, gender, contact_number, blood_type):
    # Check if the blood type exists
    cursor.execute("SELECT id FROM Blood_Types WHERE blood_type = %s", (blood_type,))
    result = cursor.fetchone()

    if result is None:
        print(f"Error: Blood type '{blood_type}' not found in Blood_Types table. Please add it first.")
        return  # Exit the function if the blood type does not exist

    blood_type_id = result[0]

    # Insert the donor into the Donors table
    cursor.execute(
        "INSERT INTO Donors (name, age, gender, contact_number, blood_type_id) VALUES (%s, %s, %s, %s, %s)",
        (name, age, gender, contact_number, blood_type_id)
    )
    db_connection.commit()
    print("Donor added successfully.")


# Function to record a donation
def record_donation(donor_id, quantity):
    donation_date = datetime.today().strftime('%Y-%m-%d')

    # Insert the donation into the Donations table
    cursor.execute(
        "INSERT INTO Donations (donor_id, donation_date, quantity) VALUES (%s, %s, %s)",
        (donor_id, donation_date, quantity)
    )

    # Update the donor's history
    cursor.execute("SELECT total_donated FROM Donor_History WHERE donor_id = %s", (donor_id,))
    result = cursor.fetchone()

    if result:
        total_donated = result[0] + quantity
        cursor.execute(
            "UPDATE Donor_History SET total_donated = %s, last_donated = %s WHERE donor_id = %s",
            (total_donated, donation_date, donor_id)
        )
    else:
        cursor.execute(
            "INSERT INTO Donor_History (donor_id, total_donated, last_donated) VALUES (%s, %s, %s)",
            (donor_id, quantity, donation_date)
        )

    db_connection.commit()
    print("Donation recorded successfully.")


# Function to add a new blood type
def add_blood_type(blood_type):
    cursor.execute("SELECT id FROM Blood_Types WHERE blood_type = %s", (blood_type,))
    result = cursor.fetchone()

    if result:
        print(f"Blood type '{blood_type}' already exists in the table.")
    else:
        cursor.execute("INSERT INTO Blood_Types (blood_type) VALUES (%s)", (blood_type,))
        db_connection.commit()
        print(f"Blood type '{blood_type}' added successfully.")


# Example Usage
# Ensure the blood type exists before adding donors
add_blood_type('A+')

# Add a donor
add_donor('John Doe', 30, 'Male', '123-456-7890', 'A+')

# Record a donation
record_donation(1, 500)  # Donor ID 1 donated 500 ml of blood

# Close the database connection when done
cursor.close()
db_connection.close()
