import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'thisisarandomgeneratedstring')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:{}@localhost:3306/sample_db".format(quote_plus("rps@123"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
