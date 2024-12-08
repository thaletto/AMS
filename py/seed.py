import sqlite3

db = sqlite3.connect('ams.db')
cursor = db.cursor()

users = [
    (1, 'laxman', 'laxman123', 'Admin', 'Gold', '7448657412', 'laxman@airdeccan.com', '123 Admin St', '', 'Chennai', 'Tamil Nadu', 'India', 600001, '2003-08-19'),
    (2, 'ram', 'ram123', 'Customer', 'Silver', '8765432109', 'ram@gmail.com', '456 Customer Rd', 'Apt 1', 'Bangalore', 'Karnataka', 'India', 560001, '2002-05-20')
]

carriers = [
    (1, 'IndiGo', 10, 15, 20, 5, 50, 75, 100, 5, 10, 15),
    (2, 'Air India', 12, 18, 25, 7, 60, 80, 120, 6, 11, 16)
]

flights = [
    (1, 1, 'Chennai', 'Delhi', 2000, 100, 50, 30),
    (2, 2, 'Bangalore', 'Mumbai', 3000, 150, 70, 40)
]

flight_schedules = [
    (1, 1, '2024-12-07', 0, 0, 0),
    (2, 2, '2024-12-08', 0, 0, 0)
]

bookings = [
    (1, 1, 2, 2, 'Economy', '2024-12-07', 'Booked', 4000),
    (2, 2, 1, 1, 'Business', '2024-12-08', 'Booked', 6000)
]

cursor.executemany('INSERT INTO User VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', users)
cursor.executemany('INSERT INTO Carrier VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', carriers)
cursor.executemany('INSERT INTO Flight VALUES (?, ?, ?, ?, ?, ?, ?, ?)', flights)
cursor.executemany('INSERT INTO FlightSchedule VALUES (?, ?, ?, ?, ?, ?)', flight_schedules)
cursor.executemany('INSERT INTO FlightBooking VALUES (?, ?, ?, ?, ?, ?, ?, ?)', bookings)

db.commit()
db.close()