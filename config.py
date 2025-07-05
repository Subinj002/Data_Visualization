import os

DB_NAME = "wms_db"
DB_USER = "postgres"
DB_PASS = "yourpassword"
DB_HOST = "localhost"
DB_PORT = "5432"

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
