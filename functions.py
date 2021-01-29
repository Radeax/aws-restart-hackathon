import mysql.connector
from connection import getConnection


def checkEmail(email):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Owners WHERE email='{email}'")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def checkEmail(email):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Owners WHERE email='{email}'")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    if (result):
        return True
    else:
        return False


def getUser(email):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Owners WHERE email='{email}'")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result[0]


def addOwners(fname, lname, email):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO Owners(firstName, lastName, email) VALUES ('{fname}', '{lname}', '{email}')")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def removeOwners(id):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM Owners WHERE Owners_id={id}")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def updateFirstName(id, fname):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE Owners SET fname = '{fname}' WHERE person_id={id}")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def updateLastName(id, lname):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE Owners SET lname = '{lname}' WHERE person_id={id}")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def selectAll():
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Owners")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def printAll():
    for Owners in selectAll():
        print(Owners)

# addPerson('John', 'Wick')
# removePerson(2)
# updateFirstName(3, "HI")


# print(printAll())
# print(selectAll())

# Cars


def addCars(year, color, ownerID, modelID):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO Cars (car_year, car_color, owner_id, model_id) VALUES ('{year}', '{color}', '{ownerID}', '{modelID}')")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def removeCars(id):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM Cars WHERE car_id={id}")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def selectAll():
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Cars")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def getAllMakes():
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Makes")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def getModels(makeID):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Models WHERE make_id = {makeID}")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def getModelPrice(modelID):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT car_price FROM Models WHERE model_id = {modelID}")
        result = cursor.fetchone()[0]
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def printAll():
    for Cars in selectAll():
        print(Cars)


# addOwners("Jo", "Po", "jo@mail.com")
# print(checkEmail("jo@mail.com"))
# print(getUser("jo@mail.com")[3])
