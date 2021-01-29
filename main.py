# from Caculations import *
from Car import *
from Owner import *
from Calculations import *
from functions import *
import time
import os

############ FUNCTIONS ############


def mainMenu():
    menu = ["Buy Car", "View Purchased Cars", "Exit"]
    print(f"Welcome, {firstName} {lastName}!")
    print("")
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

    colors = ["white", "black", "silver", "red", "green", "blue", "yellow"]

    # ['Toyota', 'Honda', 'Mercedes', 'Dodge', 'BMW', 'Chevy', 'Ford', 'Tesla']
    makesLength = len(makes)
    for i in range(makesLength):
        print(f"{i+1}) {makes[i]}")

    print("")
    makeID = int(input("Select a Manufacturer [#] >> "))
    make = makes[makeID-1]

    os.system('cls')

    years = [2019, 2020, 2021]
    yearsLength = len(years)
    for i in range(yearsLength):
        print(f"{i+1}) {years[i]}")

    print("")
    inp = int(input("Select a Year [#] >> "))

    year = years[inp-1]

    os.system('cls')

    models = getModels(makeID)
    counter = 0
    for model in models:
        counter += 1
        modelName = model[1]
        manuID = model[3]
        manu = makes[manuID-1]

        print(f"{counter}){manu} {modelName}")

    print("")
    modelID = int(input("Select a Model [#]  >>"))
    model = getModels(makeID)[modelID-1][1]

    os.system('cls')

    # Prints color options
    print("We have specials today for black and white!")
    print("")
    for i in range(len(colors)):
        print(f"{i+1}) {colors[i].capitalize()}")

    print("")
    colorSelection = int(input("Select a Color [#] >> "))
    color = colors[colorSelection-1]

    price = getModelPrice(modelID)

    os.system('cls')

    return Car(make, model, year, color, price)


def checkout(car):
    color = car.getColor()
    msrp = car.getPrice()
    year = car.getYear()
    make = car.getMake()
    model = car.getModel()
    modelID = getModelId(model)

    vet = False

    inp = input("Are you a war veteran or disabled? [Y/N] >> ")
    if (inp == 'Y' or inp == 'y'):
        vet = True
        vetDiscount = calcVetDiscount(msrp)
    else:
        vetDiscount = 0
    os.system('cls')

    colorDiscount = colorldisc(msrp, color)
    tax = calcTax(msrp - vetDiscount - colorDiscount)
    total = msrp - vetDiscount - colorDiscount + tax

    print(
        f"You are about to buy a {year} {color.capitalize()} {make} {model}" + "\n")
    print(f"        Subtotal:  ${msrp:,}")
    print(f"Veteran Discount: -${vetDiscount:,}")
    print(f" Other Discounts: -${colorDiscount:,}")
    print(f"        Est. Tax:  ${tax}")
    print(f"     Grand Total:  ${total:,}")
    print("")
    confirm = input("Confirm Purchase? [Y/N] >> ")
    os.system('cls')
    if (confirm == 'Y' or confirm == 'y'):
        addCars(year, color, ownerID, modelID)
        print("Enjoy your new car!")
    else:
        print("Returning to Main Menu...")

    time.sleep(2)


def viewCars():
    allCars = (getOwnedCars(ownerID))

    print("Cars you have purchased:")
    for car in allCars:
        year = car[1]
        color = car[2]
        model = getModelName(car[4])

        makeID = getMakeId(car[4])
        make = getMakeName(makeID)

        print(f" - {year} {make} {model}, {color}")

    select = input("Press Enter to Continue >> ")


############### SCRIPT #################
print("Welcome to AWSome Dealership!")
print("")
email = input("Please enter your email to login >> ")

# Create user if not in database
if (checkEmail(email) == False):
    firstName = input("First Name >> ")
    lastName = input("Last Name >> ")
    addOwners(firstName, lastName, email)
else:
    firstName = getUser(email)[1]
    lastName = getUser(email)[2]

ownerID = getUser(email)[0]
firstName = getFirstName(ownerID)[0]
lastName = getLastName(ownerID)[0]

os.system('cls')

while (ownerID):
    mainMenu()
    print("")
    select = input("Select from Menu >> ")
    if (select == "1"):
        os.system('cls')
        newCar = selectCar()
        checkout(newCar)
    elif (select == "2"):
        os.system('cls')
        viewCars()
    elif (select == "3"):
        os.system('cls')
        print("Have a great day!")
        exit()
    else:
        os.system('cls')
        print("Invalid selection. Try again")
        time.sleep(2)
        os.system('cls')
    os.system('cls')
