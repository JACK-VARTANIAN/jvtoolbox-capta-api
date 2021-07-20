from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy import create_engine 
import urllib
import os

from dotenv import load_dotenv
load_dotenv()

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
UID = os.getenv("UID")
PWD = os.getenv("PWDD")
params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=' + SERVER + ';'
                            'DATABASE=' + DATABASE + ';'
                            'UID=' + UID + ';'
                            'PWD=' + PWD + ';'
                            'MARS_Connection=Yes')
                            
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

db_session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))


