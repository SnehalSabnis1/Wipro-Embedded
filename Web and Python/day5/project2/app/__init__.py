import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # new
from flask_marshmallow import Marshmallow # new
from flask_restful import Api, Resource # new
from flask_migrate import Migrate
from flask_cors import CORS
	
db = SQLAlchemy() 
ma = Marshmallow()

def create_app():
    from .models import Book
    app = Flask(__name__,instance_path=os.getcwd(),instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    ma.init_app(app)
    CORS(app)
    Migrate(app,db)

    return app
