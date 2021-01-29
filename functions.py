import mysql.connector
from connection import getConnection


def checkEmail(email):
    connection = getConnection()
    cursor = connection.cursor()
    try:
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


def getFirstName(ownerID):
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"SELECT firstName FROM Owners WHERE owner_id='{ownerID}'")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result[0]


def getLastName(ownerID):
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"SELECT lastName FROM Owners WHERE owner_id='{ownerID}'")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result[0]


def getUser(email):
    connection = getConnection()
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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


# Cars
def getOwnedCars(ownerID):
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT * FROM Cars WHERE owner_id = {ownerID}")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def addCars(year, color, ownerID, modelID):
    connection = getConnection()
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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


def getMakeId(modelID):
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"SELECT make_id FROM Models WHERE model_id = {modelID}")
        result = cursor.fetchone()[0]
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def getMakeName(makeID):
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"SELECT manufacturer FROM Makes WHERE make_id = {makeID}")
        result = cursor.fetchone()[0]
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
    cursor = connection.cursor()
    try:
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
    cursor = connection.cursor()
    try:
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


def getModelName(modelID):
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"SELECT model_name FROM Models WHERE model_id = {modelID}")
        result = cursor.fetchone()[0]
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def getModelId(modelName):
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"SELECT model_id FROM Models WHERE model_name = '{modelName}'")
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
