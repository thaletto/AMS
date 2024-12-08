from random import randint
from utils import printTable
import sqlite3

db = sqlite3.connect('ams.db')

class FlightBooking:
    def __init__(self, booking_id=None):
        if booking_id:
            self.loadBooking(booking_id)
        else:
            self.BookingID = randint(1000, 9999)
            self.FlightID = 0
            self.UserID = 0
            self.NoOfSeats = 0
            self.SeatCategory = 'Economy'
            self.DateOfTravel = ''
            self.BookingStatus = 'Booked'
            self.BookingAmount = 0

    def loadBooking(self, booking_id):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM FlightBooking WHERE BookingID = ?', (booking_id,))
        row = cursor.fetchone()
        if row:
            (self.BookingID, self.FlightID, self.UserID, self.NoOfSeats, 
             self.SeatCategory, self.DateOfTravel, self.BookingStatus, 
             self.BookingAmount) = row
        else:
            print('Booking not found!')

    def save(self):
        cursor = db.cursor()
        insertQuery = '''INSERT INTO FlightBooking (BookingID, FlightID, UserID, NoOfSeats, SeatCategory, DateOfTravel, BookingStatus, BookingAmount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        
        cursor.execute(insertQuery, (self.BookingID, self.FlightID, self.UserID, self.NoOfSeats, self.SeatCategory, self.DateOfTravel, self.BookingStatus, self.BookingAmount))
        db.commit()
        cursor.close()
        print(f'Booking created with Booking ID {self.BookingID}')

    def update(self):
        cursor = db.cursor()
        updateQuery = '''UPDATE FlightBooking SET FlightID = ?, UserID = ?, NoOfSeats = ?, SeatCategory = ?, DateOfTravel = ?, BookingStatus = ?, BookingAmount = ? WHERE BookingID = ?'''
        
        cursor.execute(updateQuery, (self.FlightID, self.UserID, self.NoOfSeats, self.SeatCategory, self.DateOfTravel, self.BookingStatus, self.BookingAmount, self.BookingID))
        db.commit()
        cursor.close()
        print('Booking updated successfully...')

    @staticmethod
    def delete(booking_id):
        cursor = db.cursor()
        deleteQuery = 'DELETE FROM FlightBooking WHERE BookingID = ?'
        cursor.execute(deleteQuery, (booking_id,))
        db.commit()
        cursor.close()
        print('Booking removed successfully...')

class FlightBookings:
    def __init__(self):
        self.BookingsList = []

    def addBooking(self):
        new_booking = FlightBooking()
        new_booking.FlightID = int(input('Enter Flight ID: '))
        new_booking.UserID = int(input('Enter User ID: '))
        new_booking.NoOfSeats = int(input('Enter Number of Seats: '))
        new_booking.SeatCategory = input('Enter Seat Category (Economy/Business/Executive): ')
        new_booking.DateOfTravel = input('Enter Date of Travel (YYYY-MM-DD): ')
        new_booking.BookingStatus = input('Enter Booking Status (Booked/Travel Completed/Cancelled): ')
        new_booking.BookingAmount = int(input('Enter Booking Amount: '))
        new_booking.save()
        self.BookingsList.append(new_booking)

    def displayBookings(self):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM FlightBooking')
        rows = [['Booking ID', 'Flight ID', 'User ID', 'No Of Seats', 'Seat Category', 'Date Of Travel', 'Booking Status', 'Booking Amount']]
        for row in cursor.fetchall():
            rows.append(row)
        cursor.close()
        printTable(rows)

    def editBooking(self):
        self.displayBookings()
        BookingID = int(input('Enter Booking ID to Edit: '))
        booking = FlightBooking(booking_id=BookingID)
        if booking.BookingID:
            booking.FlightID = int(input('Enter new Flight ID: '))
            booking.UserID = int(input('Enter new User ID: '))
            booking.NoOfSeats = int(input('Enter new Number of Seats: '))
            booking.SeatCategory = input('Enter new Seat Category (Economy/Business/Executive): ')
            booking.DateOfTravel = input('Enter new Date of Travel (YYYY-MM-DD): ')
            booking.BookingStatus = input('Enter new Booking Status (Booked/Travel Completed/Cancelled): ')
            booking.BookingAmount = int(input('Enter new Booking Amount: '))
            booking.update()
        else:
            print('Booking ID not found!')

    def removeBooking(self):
        self.displayBookings()
        BookingID = int(input('Enter Booking ID to remove: '))
        FlightBooking.delete(BookingID)

    def searchBooking(self):
        BookingID = int(input('Enter Booking ID to search: '))
        cursor = db.cursor()
        cursor.execute('SELECT * FROM FlightBooking WHERE BookingID = ?', (BookingID,))
        row = cursor.fetchone()
        if row:
            printTable([row])
        else:
            print('Booking ID not found!')
        cursor.close()
