# from Caculations import *
from Car import *
from Owner import *
from Calculations import *
from functions import *

############ FUNCTIONS ############


def mainMenu():
    menu = ["Buy Car", "View Purchased Cars", "View Profile", "Exit"]
    print("Main Menu:")
    counter = 1
    for item in menu:
        print(f"{counter}) {item}")
        counter += 1


# Buy Car
#   'makes' array = [Fill from Database]
#   colors = ["red", "black", etc.]
#   List Makes (from database)
#   Ask for Year (simply assign to variable)
#   List Models based on Make
#   List Colors (based on colors array)
#   Insert car into database

def purchaseCar():
    makes = []

    for make in getAllMakes():
        makes.append(make[1])

    colors = ["white", "black", "red"]
    year = input("Car Year >> ")

    # ['Toyota', 'Honda', 'Mercedes', 'Dodge', 'BMW', 'Chevy', 'Ford', 'Tesla']
    print(makes)  # Prints the manufacturers
    manu = input("Pick a Manufacturer: ")

    print(getMakeModels(manu))  # Prints the Makes
    modelOption = int(input("Pick a Model: "))
    model = getMakeModels(manu)[modelOption][0]

    print(colors)  # Prints color options
    color = input("Pick a Color: ")

    addCars(year, color, ownerID, model)

########## SCRIPT ############


email = input("Please enter your email >> ")

# Create user if not in database
if (checkEmail(email) == False):
    firstName = input("First Name >> ")
    lastName = input("Last Name >> ")
    addOwners(firstName, lastName, email)
else:
    firstName = getUser(email)[1]
    lastName = getUser(email)[2]

ownerID = getUser(email)[0]

customer = Owner(ownerID, firstName, lastName, email)


# while (customer):


mainMenu()
option = input("Select from Menu >> ")
if (option == "1"):
    purchaseCar()


def viewCars():
    # [{},{},{}]
    # {"year": {year}, "make": {make}, "model": {model}, "color": {color}}
    cars = []

    for car in cars:
        print(f"{car.color} {car.year} {car.make} {car.model}")

# View Purchased Cars
#   1) Fill array of cars where owner_id = ownerID(variable)
#   2) Print cars (for loop)
#   3) Option to return to main menu
