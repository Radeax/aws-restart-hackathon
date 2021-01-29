# ---- Class Owner ---------
# Object: owner
# Properties: ID, Fname, Lname, , Email
from os import system
import os


class Owner:

    def __init__(self, id=None, fName=None, lName=None, email=None):
        self.__id = id  # __ to make variable private. Cannot access directly
        self.__fName = fName
        self.__lName = lName
        self.__email = email

    def setid(self, id):
        self.__id = id

    def getid(self):
        return self.__id

    def setFname(self, fName):
        self.__fName = fName

    def getFname(self):
        return self.__fName

    def setLname(self, lName):
        self.__lName = lName

    def getLname(self):
        return self.__lName

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email
