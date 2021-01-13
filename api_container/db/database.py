import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from app import app

db_user = os.environ.get("DB_MYSQL_USER")
db_pass = os.environ.get("DB_MYSQL_PASS")
db_address = os.environ.get("DB_MYSQL_ADDRESS")
db_name = "pictureapi_mydb"
connection = "mysql+pymysql://{0}:{1}@{2}/{3}".format(db_user, db_pass, db_address, db_name)

app.config['SQLALCHEMY_DATABASE_URI'] = connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)

Response = Base.classes.response
session = Session(db.engine)
