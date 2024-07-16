import os
from urllib.parse import quote_plus
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:{}@localhost:3306/sample_db2".format(quote_plus("rps@123"))


    SQLALCHEMY_TRACK_MODIFICATIONS = False

