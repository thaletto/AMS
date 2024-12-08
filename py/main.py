from User import Users
from Flight import Flights
from Carrier import Carriers

User = Users()
Flight = Flights()
Carrier = Carriers()

def carrierFunctions():
    def carrierMenu():
        print('1: Add Carrier')
        print('2: Edit Carrier')
        print('3: Remove Carrier')
        print('4: Search Carrier')
        print('5: Display Carriers')
        print('0: Exit')

    print('-'*40)
    print('CARRIER')
    print('-'*40)
    carrierMenu()
    ch = int(input('Enter choice: '))
    while ch:
        match ch:
            case 1:
                Carrier.addCarrier()
                carrierMenu()
                ch = int(input('Enter choice: '))
            case 2:
                Carrier.editCarrier()
                carrierMenu()
                ch = int(input('Enter choice: '))
            case 3:
                Carrier.removeCarrier()
                carrierMenu()
                ch = int(input('Enter choice: '))
            case 4:
                Carrier.searchCarrier()
                carrierMenu()
                ch = int(input('Enter choice: '))
            case 5:
                Carrier.displayCarriers()
                carrierMenu()
                ch = int(input('Enter choice: '))
            case 0:
                print('Exiting Carrier Functions')
                return

def flightFunctions():
    def flightMenu():
        print('1: Add Flight')
        print('2: Edit Flight')
        print('3: Remove Flight')
        print('4: Search Flight')
        print('5: Display Flights')
        print('0: Exit')

    print('-'*40)
    print('FLIGHT')
    print('-'*40)
    flightMenu()
    ch = int(input('Enter choice: '))
    while ch:
        match ch:
            case 1:
                Flight.addFlight()
                flightMenu()
                ch = int(input('Enter choice: '))
            case 2:
                Flight.editFlight()
                flightMenu()
                ch = int(input('Enter choice: '))
            case 3:
                Flight.removeFlight()
                flightMenu()
                ch = int(input('Enter choice: '))
            case 4:
                Flight.searchFlight()
                flightMenu()
                ch = int(input('Enter choice: '))
            case 5:
                Flight.displayFlights()
                flightMenu()
                ch = int(input('Enter choice: '))
            case 0:
                print('Exiting Flight Functions...')
                return

def customerFunctions():
    def customerMenu():
        print('1: Search Flight')
        print('2: Book Ticket')
        print('3: Cancel Ticket')
        print('4: Edit Customer Details')
        print('0: Exit')
    
    print('-'*40)
    print('Customer Functions')
    print('-'*40)
    
    customerMenu()
    ch = int(input('Enter choice: '))
    while ch:
        match ch:
            case 1:
                print('-'*40)
                print('Search Flight')
                print('-'*40)
                Flight.searchFlight()
                customerMenu()
                ch = int(input('Enter choice: '))
            case 2:
                print('-'*40)
                print('Book Ticket')
                print('-'*40)
                User.bookTicket()
                customerMenu()
                ch = int(input('Enter choice: '))
            case 3:
                print('-'*40)
                print('Cancel Ticket')
                print('-'*40)
                User.cancelTicket()
                customerMenu()
                ch = int(input('Enter choice: '))
            case 4:
                User.editUser()
                customerMenu()
                ch = int(input('Enter choice: '))
            case 0:
                print('Exiting Customer Functions...')
                return

def adminFunctions():
    def adminMenu():
        print('1: Add/Edit/Remove Carrier')
        print('2: Add/Edit/Remove Flight')
        print('0: Exit')

    print('-'*40)
    print('Admin Functions')
    print('-'*40)
    
    adminMenu()
    ch = int(input('Enter choice: '))
    while ch:
        match ch:
            case 1:
                carrierFunctions()
                adminMenu()
                ch = int(input('Enter choice: '))
            case 2:
                flightFunctions()
                adminMenu()
                ch = int(input('Enter choice: '))
            case 0:
                print('Exiting Admin Functions...')
                return 

def login():
    def loginMenu():
        print('1: Customer')
        print('2: Admin')
        print('0: Exit')

    print('-'*40)
    print('LOGIN')
    print('-'*40)

    loginMenu()
    ch = int(input('Enter choice: '))
    while ch:
        match ch:
            case 1:
                print('Selected Customer...')
                User.login()
                customerFunctions()
                loginMenu()
                ch = int(input('Enter choice: '))
            case 2:
                print('Selected Admin...')
                User.login()
                adminFunctions()
                loginMenu()
                ch = int(input('Enter choice: '))
            case 0:
                print('Exiting Login...')
                return          

def register():
    def registerMenu():
        print('1: Customer')
        print('2: Admin')
        print('0: Exit')
 
    print('-'*40)
    print('REGISTER')
    print('-'*40)

    registerMenu()
    ch = int(input('Enter choice: '))
    while ch:
        match ch:
            case 1:
                print('Selected Customer...')
                User.addCustomer()
                customerFunctions()
                registerMenu()
                ch = int(input('Enter choice: '))
            case 2:
                print('Selected Admin...')
                User.addAdmin()
                adminFunctions()
                registerMenu()
                ch = int(input('Enter choice: '))
            case 0:
                print('Exiting Registration...')
                return

def main():
    def menu():
        print('1: Login')
        print('2: Register')
        print('0: Exit')

    print('Welcome to Air Deccan')
    menu()
    ch = int(input('Enter choice: '))
    while ch:   
        match ch:
            case 1:
                login()
                menu()
                ch = int(input('Enter choice: '))
            case 2:
                register()
                menu()
                ch = int(input('Enter choice: '))
            case 0:
                return


if __name__ == "__main__":
    main()