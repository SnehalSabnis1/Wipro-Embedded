from urllib.parse import quote_plus

SECRET_KEY="thisisarandomgeneratedstring"
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:{}@localhost:3306/demodb_1".format(quote_plus("rps@123"))