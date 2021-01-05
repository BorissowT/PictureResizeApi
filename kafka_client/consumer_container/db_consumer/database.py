import os

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import mysql.connector
from sqlalchemy import create_engine


db_user = os.environ.get("DB_MYSQL_USER")
db_pass = os.environ.get("DB_MYSQL_PASS")
db_port = 3306
db_host = "localhost"
db_name = "pictureapi_mydb"

connection = "mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}".format(db_user, db_pass, db_host, db_port, db_name)
engine = create_engine(connection)

Base = automap_base()
Base.prepare(engine, reflect=True)

Response = Base.classes.response
session = Session(engine)
