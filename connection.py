# pip install python-dotenv
import mysql.connector
from dotenv import load_dotenv
import os
from os import getenv
load_dotenv()


def getConnection():
    return mysql.connector.connect(
        host=getenv('DB_URL'),
        user=getenv('DB_USER'),
        password=getenv('DB_PASSWORD'),
        database=getenv('DB_NAME')
    )
