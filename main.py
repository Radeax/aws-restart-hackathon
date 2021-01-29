# from Caculations import *
from Car import *
from Owner import *
from Calculations import *
from functions import *
import time
import os

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

    # ['Toyota', 'Honda', 'Mercedes', 'Dodge', 'BMW', 'Chevy', 'Ford', 'Tesla']
    makesLength = len(makes)
    for i in range(makesLength):
        print(f"{i+1}) {makes[i]}")

    makeID = int(input("Select a Manufacturer [#] >> "))
    make = makes[makeID-1]

    os.system('cls')

    year = input("Car Year >> ")

    os.system('cls')

    models = getModels(makeID)
    counter = 0
    for model in models:
        counter += 1
        modelName = model[1]
        manuID = model[3]
        manu = makes[manuID-1]

        print(f"{counter}){manu} {modelName}")

    modelID = int(input("Pick a Model: "))
    model = getModels(makeID)[modelID-1][1]

    os.system('cls')

    # Prints color options
    for i in range(len(colors)):
        print(f"{i+1}) {colors[i]}")

    colorSelection = int(input("Pick a Color: "))
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

    colorDiscount = colorldisc(msrp, color)
    tax = calcTax(msrp - vetDiscount - colorDiscount)
    total = msrp - vetDiscount - colorDiscount + tax

    print(f"Buying a {year} {color} {make} {model}" + "\n")

    print(f"        Subtotal:  ${msrp}")
    print(f"Veteran Discount: -${vetDiscount}")
    print(f" Other Discounts: -${colorDiscount}")
    print(f"        Est. Tax:  ${tax}")
    print(f"     Grand Total:  ${total}")

    confirm = input("Confirm Purchase? [Y/N] >> ")
    if (confirm == 'Y' or confirm == 'y'):
        addCars(year, color, ownerID, modelID)
        print("Enjoy your new car!")

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
select = input("Select from Menu >> ")
if (select == "1"):
    newCar = selectCar()
    checkout(newCar)
if (select == "2"):
    viewCars()
