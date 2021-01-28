# ---- Class Owner ---------
# Object: owner
# Properties: ID, Fname, Lname, , Email
from os import system
import os


class Owner:

    def __init__(self, id=None, fName=None, lName=None, email=None):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.email = email

    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def setFname(self, fName):
        self.fName = fName

    def getFname(self):
        return self.fName

    def setLname(self, lName):
        self.lName = lName

    def getLname(self):
        return self.lName

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email
