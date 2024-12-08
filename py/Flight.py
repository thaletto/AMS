from random import randint
from utils import printTable
import sqlite3

db = sqlite3.connect('ams.db')

class Flight:
    def __init__(self, flight_id=None):
        if flight_id:
            self.loadFlight(flight_id)
        else:
            self.FlightId = randint(10000, 99999)
            self.CarrierId = 0
            self.Name = 'Unnamed'
            self.Orgin = ''
            self.Destination = ''
            self.CarrierName = 'Unnamed'
            self.TravelDate = ''
            self.AirFare = 0

    def loadFlight(self, flight_id):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Flight WHERE FlightID = ?', (flight_id,))
        row = cursor.fetchone()
        if row:
            (self.FlightId, self.CarrierId, self.Name, self.Orgin, self.Destination, self.CarrierName, self.TravelDate, self.AirFare) = row
        else:
            print('Flight not found!')

    def save(self):
        cursor = db.cursor()
        insertQuery = '''INSERT INTO Flight (FlightID, CarrierID, Name, Orgin, Destination, CarrierName, TravelDate, AirFare) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        
        cursor.execute(insertQuery, (self.FlightId, self.CarrierId, self.Name, self.Orgin, self.Destination, self.CarrierName, self.TravelDate, self.AirFare))
        db.commit()
        cursor.close()
        print(f'Flight created with Flight Id {self.FlightId}')

    def update(self):
        cursor = db.cursor()
        updateQuery = '''UPDATE Flight SET CarrierID = ?, Name = ?, Orgin = ?, Destination = ?, CarrierName = ?, TravelDate = ?, AirFare = ? WHERE FlightID = ?'''
        
        cursor.execute(updateQuery, (self.CarrierId, self.Name, self.Orgin, self.Destination, self.CarrierName, self.TravelDate, self.AirFare, self.FlightId))
        db.commit()
        cursor.close()
        print('Flight updated successfully...')

    @staticmethod
    def delete(flight_id):
        cursor = db.cursor()
        deleteQuery = 'DELETE FROM Flight WHERE FlightID = ?'
        cursor.execute(deleteQuery, (flight_id,))
        db.commit()
        cursor.close()
        print('Flight removed successfully...')

class Flights:
    def __init__(self):
        self.FlightsList = []

    def addFlight(self):
        new_flight = Flight()
        for attr, value in vars(new_flight).items():
            if attr == 'FlightId':
                continue
            newValue = input(f'Enter {attr} value (default value: {value}): ')
            if newValue.strip():
                if isinstance(value, int):
                    setattr(new_flight, attr, int(newValue))
                else:
                    setattr(new_flight, attr, newValue)
        new_flight.save()
        self.FlightsList.append(new_flight)

    def displayFlights(self):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Flight')
        rows = [['Flight Id', 'Carrier Id', 'Name', 'Orgin', 'Destination', 'Carrier Name', 'Travel Date', 'Air Fare']]
        for row in cursor.fetchall():
            rows.append(row)
        cursor.close()
        printTable(rows)

    def editFlight(self):
        self.displayFlights()
        FlightId = int(input('Enter Flight Id to Edit: '))
        flight = Flight(flight_id=FlightId)
        if flight.FlightId:
            for attr, value in vars(flight).items():
                if attr == 'FlightId':
                    continue
                newValue = input(f'Enter new value for {attr} (current value: {value}): ')
                if newValue.strip():
                    if isinstance(value, int):
                        setattr(flight, attr, int(newValue))
                    else:
                        setattr(flight, attr, newValue)
            flight.update()
        else:
            print('FlightId not found!')

    def removeFlight(self):
        self.displayFlights()
        FlightId = int(input('Enter Flight Id to remove: '))
        Flight.delete(FlightId)

    def searchFlight(self):
        FlightId = int(input('Enter Flight Id to search: '))
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Flight WHERE FlightID = ?', (FlightId,))
        row = cursor.fetchone()
        if row:
            printTable([row])
        else:
            print('Flight Id not found!')
        cursor.close()