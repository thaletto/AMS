# Code Documentation

## Database Schema

The database schema consists of several tables that are used to manage users, flights, carriers, flight schedules, and flight bookings. Below is a detailed description of each table:

### 1. User Table
- **Table Name**: User
- **Columns**:
  - `UserID`: INT, Primary Key
  - `UserName`: VARCHAR(255)
  - `Password`: VARCHAR(255)
  - `Role`: VARCHAR(50), CHECK (Role IN ('Admin', 'Customer'))
  - `CustomerCategory`: VARCHAR(50), CHECK (CustomerCategory IN ('Silver', 'Gold', 'Platinum'))
  - `Phone`: VARCHAR(20)
  - `EmailId`: VARCHAR(255)
  - `Address1`: VARCHAR(255)
  - `Address2`: VARCHAR(255)
  - `City`: VARCHAR(100)
  - `State`: VARCHAR(100)
  - `Country`: VARCHAR(100)
  - `ZipCode`: INT
  - `DOB`: DATE

### 2. Flight Table
- **Table Name**: Flight
- **Columns**:
  - `FlightID`: INT, Primary Key
  - `CarrierID`: INT, Foreign Key referencing Carrier(CarrierID)
  - `Origin`: VARCHAR(100)
  - `Destination`: VARCHAR(100)
  - `AirFare`: INT
  - `SeatCapacityEconomyClass`: INT, CHECK (>= 20)
  - `SeatCapacityBusinessClass`: INT, CHECK (>= 10)
  - `SeatCapacityExecutiveClass`: INT, CHECK (>= 10)

### 3. Carrier Table
- **Table Name**: Carrier
- **Columns**:
  - `CarrierID`: INT, Primary Key
  - `CarrierName`: VARCHAR(255)
  - `DiscountPercentageThirtyDaysAdvanceBooking`: INT
  - `DiscountPercentageSixtyDaysAdvanceBooking`: INT
  - `DiscountPercentageNinetyDaysAdvanceBooking`: INT
  - `BulkBookingDiscount`: INT
  - `RefundPercentageForTicketCancellation2DaysBeforeTravelDate`: INT
  - `RefundPercentageForTicketCancellation10DaysBeforeTravelDate`: INT
  - `RefundPercentageForTicketCancellation20DaysOrMoreBeforeTravelDate`: INT
  - `SilverUserDiscount`: INT
  - `GoldUserDiscount`: INT
  - `PlatinumUserDiscount`: INT

### 4. FlightSchedule Table
- **Table Name**: FlightSchedule
- **Columns**:
  - `FlightScheduleID`: INT, Primary Key
  - `FlightID`: INT, Foreign Key referencing Flight(FlightID)
  - `DateOfTravel`: DATE
  - `BusinessClassBookedCount`: INT
  - `EconomyClassBookedCount`: INT
  - `ExecutiveClassBookedCount`: INT

### 5. FlightBooking Table
- **Table Name**: FlightBooking
- **Columns**:
  - `BookingID`: INT, Primary Key
  - `FlightID`: INT, Foreign Key referencing Flight(FlightID)
  - `UserID`: INT, Foreign Key referencing User(UserID)
  - `NoOfSeats`: INT
  - `SeatCategory`: VARCHAR(50), CHECK (SeatCategory IN ('Economy', 'Executive', 'Business'))
  - `DateOfTravel`: DATE
  - `BookingStatus`: VARCHAR(50), CHECK (BookingStatus IN ('Booked', 'Travel Completed', 'Cancelled'))
  - `BookingAmount`: INT

## Class Structures and Methods

### 1. User Class
- **Inherits**: Address
- **Attributes**:
  - `UserId`
  - `UserName`
  - `Password`
  - `Role`
  - `Category`
  - `Phone`
  - `Email`
  - `Dob`
  - `Address` (instance of Address)

- **Methods**:
  - `registerUser()`: Registers the user in the database.
  - `setAsAdmin()`: Sets the user's role to Admin.

### 2. Address Class
- **Attributes**:
  - `Add1`
  - `Add2`
  - `City`
  - `State`
  - `Country`
  - `Zipcode`

### 3. Flight Class
- **Attributes**:
  - `FlightId`
  - `CarrierId`
  - `Name`
  - `Origin`
  - `Destination`
  - `CarrierName`
  - `TravelDate`
  - `AirFare`

- **Methods**:
  - `loadFlight(flight_id)`: Loads flight details from the database.
  - `save()`: Saves the flight to the database.
  - `update()`: Updates flight details in the database.
  - `delete(flight_id)`: Deletes a flight from the database.

### 4. Carrier Class
- **Attributes**:
  - `CarrierId`
  - `CarrierName`
  - Various discount attributes

- **Methods**:
  - `loadCarrier(carrier_id)`: Loads carrier details from the database.
  - `save()`: Saves the carrier to the database.
  - `update()`: Updates carrier details in the database.
  - `delete(carrier_id)`: Deletes a carrier from the database.

### 5. FlightSchedule Class
- **Attributes**:
  - `FlightScheduleID`
  - `FlightID`
  - `DateOfTravel`
  - `BusinessClassBookedCount`
  - `EconomyClassBookedCount`
  - `ExecutiveClassBookedCount`

- **Methods**:
  - `loadFlightSchedule(flight_schedule_id)`: Loads flight schedule details from the database.
  - `save()`: Saves the flight schedule to the database.
  - `update()`: Updates flight schedule details in the database.
  - `delete(flight_schedule_id)`: Deletes a flight schedule from the database.

### 6. FlightBooking Class
- **Attributes**:
  - `BookingID`
  - `FlightID`
  - `UserID`
  - `NoOfSeats`
  - `SeatCategory`
  - `DateOfTravel`
  - `BookingStatus`
  - `BookingAmount`

- **Methods**:
  - `loadBooking(booking_id)`: Loads booking details from the database.
  - `save()`: Saves the booking to the database.
  - `update()`: Updates booking details in the database.
  - `delete(booking_id)`: Deletes a booking from the database.

## Main Function
The main function serves as the entry point for the application. It provides a menu for users to either log in or register. Based on the user's choice, it directs them to the appropriate functions for customer or admin operations.

### Main Function Logic:
1. Display a welcome message and the main menu.
2. Accept user input for the choice of action (Login/Register/Exit).
3. Based on the choice:
   - If Login, call the login function.
   - If Register, call the register function.
   - If Exit, terminate the program.

## Functions in `utils.py`

### 1. `printTable(rows)`
- **Description**: This function takes a list of rows and prints them in a formatted table using the `Texttable` library.
- **Parameters**:
  - `rows`: A list of lists, where each inner list represents a row in the table.
- **Logic**:
  - Creates a `Texttable` object.
  - Adds the rows to the table.
  - Prints the formatted table.

### 2. `generateRandomId(n)`
- **Description**: Generates a random alphanumeric ID of length `n`.
- **Parameters**:
  - `n`: The length of the ID to be generated.
- **Logic**:
  - Uses `random.choices` to select random characters from a combination of ASCII letters and digits.
  - Joins the selected characters into a single string and returns it.

## General Logic
The application is designed to manage flight bookings, users, and carriers. It allows users to register, log in, book flights, and manage their bookings. Admins can manage carriers and flights. The database schema supports these functionalities by providing structured tables for storing relevant data. The utility functions enhance the code's readability and maintainability by providing common functionalities like printing tables and generating random IDs.
