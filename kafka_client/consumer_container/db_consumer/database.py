import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import mysql.connector
from sqlalchemy import create_engine

import time

db_user = os.environ.get("DB_MYSQL_USER")
db_pass = os.environ.get("DB_MYSQL_PASS")
db_address = os.environ.get("DB_MYSQL_ADDRESS")
db_name = "pictureapi_mydb"
flag = True
while flag:
    try:
        connection = "mysql+mysqlconnector://{0}:{1}@{2}/{3}".format(db_user, db_pass, db_address, db_name)
        engine = create_engine(connection)

        Base = automap_base()
        Base.prepare(engine, reflect=True)

        Response = Base.classes.response
        session = Session(engine)
    except Exception as e:
        print(e)
        time.sleep(1.5)
    else:
        flag = False
