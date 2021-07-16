import pyodbc
import os

from dotenv import load_dotenv
load_dotenv()

def connection():
    SERVER = os.getenv("SERVER")
    DATABASE = os.getenv("DATABASE")
    UID = os.getenv("UID")
    PWD = os.getenv("PWDD")

    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=' + SERVER + ';'
                            'DATABASE=' + DATABASE + ';'
                            'UID=' + UID + ';'
                            'PWD=' + PWD + ';'
                            'MARS_Connection=Yes')
    return conn
