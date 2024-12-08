from random import randint
from utils import printTable
import sqlite3

db = sqlite3.connect('ams.db')

class FlightSchedule:
    def __init__(self, flight_schedule_id=None):
        if flight_schedule_id:
            self.loadFlightSchedule(flight_schedule_id)
        else:
            self.FlightScheduleID = randint(1000, 9999)
            self.FlightID = 0
            self.DateOfTravel = ''
            self.BusinessClassBookedCount = 0
            self.EconomyClassBookedCount = 0
            self.ExecutiveClassBookedCount = 0

    def loadFlightSchedule(self, flight_schedule_id):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM FlightSchedule WHERE FlightScheduleID = ?', (flight_schedule_id,))
        row = cursor.fetchone()
        if row:
            (self.FlightScheduleID, self.FlightID, self.DateOfTravel, 
             self.BusinessClassBookedCount, self.EconomyClassBookedCount, 
             self.ExecutiveClassBookedCount) = row
        else:
            print('Flight Schedule not found!')

    def save(self):
        cursor = db.cursor()
        insertQuery = '''INSERT INTO FlightSchedule (FlightScheduleID, FlightID, DateOfTravel, BusinessClassBookedCount, EconomyClassBookedCount, ExecutiveClassBookedCount) VALUES (?, ?, ?, ?, ?, ?)'''
        
        cursor.execute(insertQuery, (self.FlightScheduleID, self.FlightID, self.DateOfTravel, self.BusinessClassBookedCount, self.EconomyClassBookedCount, self.ExecutiveClassBookedCount))
        db.commit()
        cursor.close()
        print(f'Flight Schedule created with ID {self.FlightScheduleID}')

    def update(self):
        cursor = db.cursor()
        updateQuery = '''UPDATE FlightSchedule SET FlightID = ?, DateOfTravel = ?, BusinessClassBookedCount = ?, EconomyClassBookedCount = ?, ExecutiveClassBookedCount = ? WHERE FlightScheduleID = ?'''
        
        cursor.execute(updateQuery, (self.FlightID, self.DateOfTravel, self.BusinessClassBookedCount, self.EconomyClassBookedCount, self.ExecutiveClassBookedCount, self.FlightScheduleID))
        db.commit()
        cursor.close()
        print('Flight Schedule updated successfully...')

    @staticmethod
    def delete(flight_schedule_id):
        cursor = db.cursor()
        deleteQuery = 'DELETE FROM FlightSchedule WHERE FlightScheduleID = ?'
        cursor.execute(deleteQuery, (flight_schedule_id,))
        db.commit()
        cursor.close()
        print('Flight Schedule removed successfully...')

class FlightSchedules:
    def __init__(self):
        self.FlightSchedulesList = []

    def addFlightSchedule(self):
        new_schedule = FlightSchedule()
        new_schedule.FlightID = int(input('Enter Flight ID: '))
        new_schedule.DateOfTravel = input('Enter Date of Travel (YYYY-MM-DD): ')
        new_schedule.BusinessClassBookedCount = int(input('Enter Business Class Booked Count: '))
        new_schedule.EconomyClassBookedCount = int(input('Enter Economy Class Booked Count: '))
        new_schedule.ExecutiveClassBookedCount = int(input('Enter Executive Class Booked Count: '))
        new_schedule.save()
        self.FlightSchedulesList.append(new_schedule)

    def displayFlightSchedules(self):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM FlightSchedule')
        rows = [['Flight Schedule ID', 'Flight ID', 'Date of Travel', 'Business Class Booked', 'Economy Class Booked', 'Executive Class Booked']]
        for row in cursor.fetchall():
            rows.append(row)
        cursor.close()
        printTable(rows)

    def editFlightSchedule(self):
        self.displayFlightSchedules()
        FlightScheduleID = int(input('Enter Flight Schedule ID to Edit: '))
        schedule = FlightSchedule(flight_schedule_id=FlightScheduleID)
        if schedule.FlightScheduleID:
            schedule.FlightID = int(input('Enter new Flight ID: '))
            schedule.DateOfTravel = input('Enter new Date of Travel (YYYY-MM-DD): ')
            schedule.BusinessClassBookedCount = int(input('Enter new Business Class Booked Count: '))
            schedule.EconomyClassBookedCount = int(input('Enter new Economy Class Booked Count: '))
            schedule.ExecutiveClassBookedCount = int(input('Enter new Executive Class Booked Count: '))
            schedule.update()
        else:
            print('Flight Schedule ID not found!')

    def removeFlightSchedule(self):
        self.displayFlightSchedules()
        FlightScheduleID = int(input('Enter Flight Schedule ID to remove: '))
        FlightSchedule.delete(FlightScheduleID)

    def searchFlightSchedule(self):
        FlightScheduleID = int(input('Enter Flight Schedule ID to search: '))
        cursor = db.cursor()
        cursor.execute('SELECT * FROM FlightSchedule WHERE FlightScheduleID = ?', (FlightScheduleID,))
        row = cursor.fetchone()
        if row:
            printTable([row])
        else:
            print('Flight Schedule ID not found!')
        cursor.close()
