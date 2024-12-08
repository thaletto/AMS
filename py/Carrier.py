from random import randint
from utils import printTable
import sqlite3

db = sqlite3.connect('ams.db')

class Carrier:
    def __init__(self, carrier_id=None):
        if carrier_id:
            self.loadCarrier(carrier_id)
        else:
            self.CarrierId = randint(100, 999)
            self.CarrierName = 'Unnamed'
            self.DiscountPercentageThirtyDaysAdvanceBooking = 2
            self.DiscountPercentageSixtyDaysAdvanceBooking = 3
            self.DiscountPercentageNinetyDaysAdvanceBooking = 4
            self.BulkBookingDiscount = 2
            self.RefundPercentageForTicketCancellation2DaysBeforeTravelDate = 20
            self.RefundPercentageForTicketCancellation10DaysBeforeTravelDate = 25
            self.RefundPercentageForTicketCancellation20DaysOrMoreBeforeTravelDate = 30
            self.SilverUserDiscount = 1
            self.GoldUserDiscount = 2
            self.PlatinumUserDiscount = 4

    def loadCarrier(self, carrier_id):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Carrier WHERE CarrierID = ?', (carrier_id,))
        row = cursor.fetchone()
        if row:
            (self.CarrierId, self.CarrierName, 
             self.DiscountPercentageThirtyDaysAdvanceBooking, 
             self.DiscountPercentageSixtyDaysAdvanceBooking, 
             self.DiscountPercentageNinetyDaysAdvanceBooking, 
             self.BulkBookingDiscount, 
             self.RefundPercentageForTicketCancellation2DaysBeforeTravelDate, 
             self.RefundPercentageForTicketCancellation10DaysBeforeTravelDate, 
             self.RefundPercentageForTicketCancellation20DaysOrMoreBeforeTravelDate, 
             self.SilverUserDiscount, 
             self.GoldUserDiscount, 
             self.PlatinumUserDiscount) = row
        else:
            print('Carrier not found!')

    def save(self):
        cursor = db.cursor()
        insertQuery = '''INSERT INTO Carrier (CarrierID, CarrierName, DiscountPercentageThirtyDaysAdvanceBooking, DiscountPercentageSixtyDaysAdvanceBooking, DiscountPercentageNinetyDaysAdvanceBooking, BulkBookingDiscount, RefundPercentageForTicketCancellation2DaysBeforeTravelDate, RefundPercentageForTicketCancellation10DaysBeforeTravelDate, RefundPercentageForTicketCancellation20DaysOrMoreBeforeTravelDate, SilverUserDiscount, GoldUserDiscount, PlatinumUserDiscount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        
        cursor.execute(insertQuery, (self.CarrierId, self.CarrierName, self.DiscountPercentageThirtyDaysAdvanceBooking, self.DiscountPercentageSixtyDaysAdvanceBooking, self.DiscountPercentageNinetyDaysAdvanceBooking, self.BulkBookingDiscount, self.RefundPercentageForTicketCancellation2DaysBeforeTravelDate, self.RefundPercentageForTicketCancellation10DaysBeforeTravelDate, self.RefundPercentageForTicketCancellation20DaysOrMoreBeforeTravelDate, self.SilverUserDiscount, self.GoldUserDiscount, self.PlatinumUserDiscount))
        db.commit()
        cursor.close()
        print(f'Carrier created with Carrier Id {self.CarrierId}')

    def update(self):
        cursor = db.cursor()
        updateQuery = '''UPDATE Carrier SET CarrierName = ?, DiscountPercentageThirtyDaysAdvanceBooking = ?, DiscountPercentageSixtyDaysAdvanceBooking = ?, DiscountPercentageNinetyDaysAdvanceBooking = ?, BulkBookingDiscount = ?, RefundPercentageForTicketCancellation2DaysBeforeTravelDate = ?, RefundPercentageForTicketCancellation10DaysBeforeTravelDate = ?, RefundPercentageForTicketCancellation20DaysOrMoreBeforeTravelDate = ?, SilverUserDiscount = ?, GoldUserDiscount = ?, PlatinumUserDiscount = ? WHERE CarrierID = ?'''
        
        cursor.execute(updateQuery, (
            self.CarrierName, 
            self.DiscountPercentageThirtyDaysAdvanceBooking, 
            self.DiscountPercentageSixtyDaysAdvanceBooking, 
            self.DiscountPercentageNinetyDaysAdvanceBooking, 
            self.BulkBookingDiscount, 
            self.RefundPercentageForTicketCancellation2DaysBeforeTravelDate, 
            self.RefundPercentageForTicketCancellation10DaysBeforeTravelDate, 
            self.RefundPercentageForTicketCancellation20DaysOrMoreBeforeTravelDate, 
            self.SilverUserDiscount, 
            self.GoldUserDiscount, 
            self.PlatinumUserDiscount, 
            self.CarrierId
        ))
        db.commit()
        cursor.close()
        print('Carrier updated successfully...')

    @staticmethod
    def delete(carrier_id):
        cursor = db.cursor()
        deleteQuery = 'DELETE FROM Carrier WHERE CarrierID = ?'
        cursor.execute(deleteQuery, (carrier_id,))
        db.commit()
        cursor.close()
        print('Carrier removed successfully...')

class Carriers:
    def __init__(self):
        self.CarriersList = []

    def addCarrier(self):
        new_carrier = Carrier()
        new_carrier.save()
        self.CarriersList.append(new_carrier)

    def displayCarriers(self):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Carrier')
        rows = [['Carrier Id', 'Carrier Name', 'Discount30days', 'Discount60days', 'Discount90days', 'Bulk Discount', 'Refund 2 days', 'Refund 10 days', 'Refund 20 days', 'Silver Disc', 'Gold Disc', 'Platinum Disc']]
        for row in cursor.fetchall():
            rows.append(row)
        cursor.close()
        printTable(rows)

    def editCarrier(self):
        self.displayCarriers()
        CarrierId = int(input('Enter CarrierId to Edit: '))
        carrier = Carrier(carrier_id=CarrierId)
        if carrier.CarrierId:
            for attr, value in vars(carrier).items():
                if attr == 'CarrierId':
                    continue
                newValue = input(f'Enter new value for {attr} (current value: {value}): ')
                if newValue.strip():
                    if isinstance(value, int):
                        setattr(carrier, attr, int(newValue))
                    else:
                        setattr(carrier, attr, newValue)
            carrier.update()
        else:
            print('CarrierId not found!')

    def removeCarrier(self):
        self.displayCarriers()
        CarrierId = int(input('Enter Carrier Id to remove: '))
        Carrier.delete(CarrierId)

    def searchCarrier(self):
        CarrierId = int(input('Enter Carrier Id to search: '))
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Carrier WHERE CarrierID = ?', (CarrierId,))
        row = cursor.fetchone()
        if row:
            printTable([row])
        else:
            print('Carrier Id not found!')
        cursor.close()