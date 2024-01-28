from dotenv import load_dotenv
import os
load_dotenv()

# CLIENT_ID = os.environ.get("CLIENT_ID")
# CLIENT_SECRET = os.environ.get("CLIENT_SECRET")



## db config 

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")



SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://" + DB_USER + ":" + DB_PASS + "@" + DB_HOST + ":" + DB_PORT + "/" + DB_NAME
