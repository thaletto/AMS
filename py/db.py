import sqlite3
db = sqlite3.connect('ams.db')
cursor = db.cursor()

createUser = '''CREATE TABLE User (
                    UserID INT PRIMARY KEY,
                    UserName VARCHAR(255),
                    Password VARCHAR(255),
                    Role VARCHAR(50) CHECK (Role IN ('Admin', 'Customer')),
                    CustomerCategory VARCHAR(50) CHECK (CustomerCategory IN ('Silver', 'Gold', 'Platinum')),
                    Phone VARCHAR(20),
                    EmailId VARCHAR(255),
                    Address1 VARCHAR(255),
                    Address2 VARCHAR(255),
                    City VARCHAR(100),
                    State VARCHAR(100),
                    Country VARCHAR(100),
                    ZipCode INT,
                    DOB DATE
                )'''

createFlight = '''CREATE TABLE Flight (
                    FlightID INT PRIMARY KEY,
                    CarrierID INT,
                    Origin VARCHAR(100),
                    Destination VARCHAR(100),
                    AirFare INT,
                    SeatCapacityEconomyClass INT CHECK (SeatCapacityEconomyClass >= 20),
                    SeatCapacityBusinessClass INT CHECK (SeatCapacityBusinessClass >= 10),
                    SeatCapacityExecutiveClass INT CHECK (SeatCapacityExecutiveClass >= 10),
                    FOREIGN KEY (CarrierID) REFERENCES Carrier(CarrierID)
                );'''

createCarrier = '''CREATE TABLE Carrier (
                    CarrierID INT PRIMARY KEY,
                    CarrierName VARCHAR(255),
                    DiscountPercentageThirtyDaysAdvanceBooking INT,
                    DiscountPercentageSixtyDaysAdvanceBooking INT,
                    DiscountPercentageNinetyDaysAdvanceBooking INT,
                    BulkBookingDiscount INT,
                    RefundPercentageForTicketCancellation2DaysBeforeTravelDate INT,
                    RefundPercentageForTicketCancellation10DaysBeforeTravelDate INT,
                    RefundPercentageForTicketCancellation20DaysOrMoreBeforeTravelDate INT,
                    SilverUserDiscount INT,
                    GoldUserDiscount INT,
                    PlatinumUserDiscount INT
                );'''

createFlightSchedule = '''CREATE TABLE FlightSchedule (
                            FlightScheduleID INT PRIMARY KEY,
                            FlightID INT,
                            DateOfTravel DATE,
                            BusinessClassBookedCount INT,
                            EconomyClassBookedCount INT,
                            ExecutiveClassBookedCount INT,
                            FOREIGN KEY (FlightID) REFERENCES Flight(FlightID)
                        );'''

createFlightBooking = '''CREATE TABLE FlightBooking (
                            BookingID INT PRIMARY KEY,
                            FlightID INT,
                            UserID INT,
                            NoOfSeats INT,
                            SeatCategory VARCHAR(50) CHECK (SeatCategory IN ('Economy', 'Executive', 'Business')),
                            DateOfTravel DATE,
                            BookingStatus VARCHAR(50) CHECK (BookingStatus IN ('Booked', 'Travel Completed', 'Cancelled')),
                            BookingAmount INT,
                            FOREIGN KEY (FlightID) REFERENCES Flight(FlightID),
                            FOREIGN KEY (UserID) REFERENCES User(UserID)
                        );'''

cursor.execute(createUser);
cursor.execute(createCarrier);
cursor.execute(createFlight);
cursor.execute(createFlightSchedule);
cursor.execute(createFlightBooking);
db.commit()