from utils import generateRandomId
import sqlite3

MASTER_PASSWORD = '@irDeCcAn'
db = sqlite3.connect('ams.db')
cursor = db.cursor()

class Address:
    def __init__(self):
        self.Add1 = input('Enter Add1: ')
        self.Add2 = input('Enter Add2: ')
        self.City = input('Enter City: ')
        self.State = input('Enter State: ')
        self.Country = input('Enter Country: ')
        self.Zipcode = input('Enter Zipcode: ')

class User(Address):
    def __init__(self):
        self.UserId = generateRandomId(6)
        self.UserName = input('Enter Username: ')
        self.Password = input('Enter Password: ')
        self.Role = 'Customer'
        self.Category = 'Silver'
        self.Phone = input('Enter Phone: ')
        self.Email = input('Enter Email: ')
        self.Dob = input('Enter DOB: ')
        self.Address = Address()
        self.registerUser()  # Register user in the database
        print(f'{self.UserName} is registered with user id {self.UserId}')
    
    def registerUser(self):
        cursor.execute('''INSERT INTO User (UserID, UserName, Password, Role, CustomerCategory, Phone, EmailId, Address1, Address2, City, State, Country, ZipCode, DOB) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (self.UserId, self.UserName, self.Password, self.Role, self.Category, self.Phone, self.Email, 
                        self.Address.Add1, self.Address.Add2, self.Address.City, self.Address.State, self.Address.Country, 
                        self.Address.Zipcode, self.Dob))
        db.commit()

    def setAsAdmin(self):
        self.Role = 'Admin'
        print(f'{self.UserName} is given admin privilege')
        return

class Users(User):
    def __init__(self):
        self.UsersList = []
    
    def addCustomer(self):
        Customer = User()
        self.UsersList.append(Customer)
        return True
    
    def addAdmin(self):
        masterPassword = input('Enter Master Password to register Admin: ')
        if masterPassword == MASTER_PASSWORD:
            Admin = User()
            Admin.setAsAdmin()
            self.UsersList.append(Admin)
            return True
        print('Wrong Master Password')
        return False
    
    def editUser(self):
        UserName = input('Enter UserName to Edit: ')
        for user in self.UsersList:
            if user.UserName == UserName:
                for attr, value in vars(user).items():
                    if attr == 'UserId':
                        continue
                    newValue = input(f'Enter new value for {attr} (current value: {value}): ')

                    if newValue.strip():
                        if isinstance(value, int):
                            setattr(user, attr, int(newValue))
                        else:
                            setattr(user, attr, newValue)
                self.updateUserInDB(user)  # Update user in the database
                print('User Details Updated...')
                return
        print('UserName not found!')

    def updateUserInDB(self, user):
        cursor.execute('''UPDATE User SET UserName=?, Password=?, Role=?, CustomerCategory=?, Phone=?, EmailId=?, 
                          Address1=?, Address2=?, City=?, State=?, Country=?, ZipCode=?, DOB=? WHERE UserID=?''',
                       (user.UserName, user.Password, user.Role, user.Category, user.Phone, user.Email, 
                        user.Address.Add1, user.Address.Add2, user.Address.City, user.Address.State, 
                        user.Address.Country, user.Address.Zipcode, user.UserId))
        db.commit()

    def login(self):
        UserName = input('Enter UserName: ')
        Password = input('Enter Password: ')
        cursor.execute('SELECT * FROM User WHERE UserName=?', (UserName,))
        user = cursor.fetchone()
        if user:
            if user[2] == Password:  # Assuming Password is the third column
                print('Logging in...')
                return True
            else:
                print('Wrong Password!')
                self.login()
        print(f'No UserName {UserName} found!')
        return False
    
    def bookTicket(self):
        flight_id = input('Enter Flight ID: ')
        no_of_seats = int(input('Enter Number of Seats: '))
        seat_category = input('Enter Seat Category (Economy, Executive, Business): ')
        date_of_travel = input('Enter Date of Travel (YYYY-MM-DD): ')

        cursor.execute('''INSERT INTO FlightBooking (FlightID, UserID, NoOfSeats, SeatCategory, DateOfTravel, BookingStatus, BookingAmount) 
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (flight_id, self.UserId, no_of_seats, seat_category, date_of_travel, 'Booked', 0))  # BookingAmount can be calculated based on fare
        db.commit()
        print('Ticket booked successfully!')

    def cancelTicket(self):
        booking_id = input('Enter Booking ID to cancel: ')
        cursor.execute('SELECT * FROM FlightBooking WHERE BookingID=? AND UserID=?', (booking_id, self.UserId))
        booking = cursor.fetchone()
        if booking:
            cursor.execute('DELETE FROM FlightBooking WHERE BookingID=?', (booking_id,))
            db.commit()
            print('Ticket canceled successfully!')
        else:
            print('Booking ID not found or does not belong to you.')