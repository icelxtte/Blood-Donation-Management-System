#Programmer:Sachorra Douglas
#Date: 11/28/2024

import mysql.connector
from random import randint
from datetime import datetime, timedelta

# Connect to the database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leavemealone45@",
    database="blood_donation_system"
)

cursor = db_connection.cursor()


# Insert random donor history data
def insert_random_donor_history():
    for donor_id in range(1, 21):  # For donor IDs 1 to 20
        total_donated = randint(1000, 5000)  # Random total donation between 1000ml and 5000ml
        last_donated = datetime.today() - timedelta(days=randint(0, 365))  # Random date in the last year
        last_donated_date = last_donated.strftime('%Y-%m-%d')

        cursor.execute(
            "INSERT INTO Donor_History (donor_id, total_donated, last_donated) VALUES (%s, %s, %s)",
            (donor_id, total_donated, last_donated_date)
        )

    db_connection.commit()
    print("Random donor history data inserted successfully.")


# Run the insertion function
insert_random_donor_history()

# Verify by fetching data from the Donor_History table
cursor.execute("SELECT * FROM Donor_History")
donor_history_data = cursor.fetchall()

# Display the results
for record in donor_history_data:
    print(record)

# Close the connection
cursor.close()
db_connection.close()
