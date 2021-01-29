import mysql.connector


def getConnection():
    return mysql.connector.connect(
        host="",  # HOSTNAME
        user="",
        passwd="",
        database=""
    )
