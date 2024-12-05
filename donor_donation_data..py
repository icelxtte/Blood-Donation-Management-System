#Programmer:Sachorra Douglas
#Date: 11/28/2024

import mysql.connector
from random import randint, choice
from datetime import datetime, timedelta

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leavemealone45@",
    database="blood_donation_system"
)

# Create a cursor object
cursor = db_connection.cursor()

# Function to generate random donation dates
def random_date():
    today = datetime.today()
    random_days = randint(1, 180)  # Random days within the last 6 months
    random_date = today - timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')

# Function to generate random donation quantity
def random_quantity():
    return randint(200, 500)  # Donation quantity in ml

# Function to record random donations for existing donors
def create_random_donations():
    donor_ids = range(1, 21)  # Assuming you have donor IDs from 1 to 20
    for donor_id in donor_ids:
        donation_date = random_date()
        quantity = random_quantity()

        cursor.execute(
            "INSERT INTO Donations (donor_id, donation_date, quantity) VALUES (%s, %s, %s)",
            (donor_id, donation_date, quantity)
        )
        db_connection.commit()
        print(f"Donation recorded for Donor ID {donor_id}: {quantity} ml on {donation_date}")

# Call the function to create 15 random donations
create_random_donations()

# Close the database connection
cursor.close()
db_connection.close()
