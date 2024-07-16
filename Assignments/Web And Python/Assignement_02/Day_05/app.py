from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from models import Route, Schedule

# Create tables if they don't exist
with app.app_context():
    db.create_all()

