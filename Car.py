class Car:
    def __init__(self, make=None, model=None, year=None, color=None, price=None):
        self.__make = make  # __ to make variable private. Cannot access directly
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setYear(self, year):
        self.__year = year

    def getYear(self):
        return self.__year

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price


# Class Car:
# Object: Audi, Mercedes, Toyota, BMW, Tesla
# Properties: make, model, year, color
