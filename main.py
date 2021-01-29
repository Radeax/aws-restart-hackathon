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

# Select Car
#   'makes' array = [Fill from Database]
#   colors = ["red", "black", etc.]
#   List Makes (from database)
#   Ask for Year (simply assign to variable)
#   List Models based on Make
#   List Colors (based on colors array)
#   Insert car into database


def selectCar():
    makes = []

    for make in getAllMakes():
        makes.append(make[1])

    colors = ["white", "black", "red"]
    year = input("Car Year >> ")

    # ['Toyota', 'Honda', 'Mercedes', 'Dodge', 'BMW', 'Chevy', 'Ford', 'Tesla']
    makesLength = len(makes)
    for i in range(makesLength):
        print(f"{i+1}) {makes[i]}")

    # print(makes)  # Prints the manufacturers
    manu = int(input("Pick a Manufacturer: "))

    models = getMakeModels(manu)
    counter = 0
    for model in models:
        counter += 1
        modelName = model[1]
        makeID = model[3]
        make = makes[makeID-1]

        print(f"{counter}){make} {modelName}")

    modelOption = int(input("Pick a Model: "))
    model = getMakeModels(manu)[modelOption-1][0]

    # Prints color options
    for i in range(len(colors)):
        print(f"{i+1}) {colors[i]}")

    colorSelection = int(input("Pick a Color: "))
    color = colors[colorSelection-1]

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


# while (customer):


mainMenu()
option = input("Select from Menu >> ")
if (option == "1"):
    selectCar()


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
