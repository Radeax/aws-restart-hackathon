import mysql.connector


def getConnection():
    return mysql.connector.connect(
        host="nci-cohort2-db.cjrtg2jq0iab.us-east-2.rds.amazonaws.com",
        user="admin",
        passwd="dragonite",
        database="hackathon"
    )
