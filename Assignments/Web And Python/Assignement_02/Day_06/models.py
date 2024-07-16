from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TransitRoute(db.Model):
    __tablename__ = 'transit_routes'
    id = db.Column(db.Integer, primary_key=True)
    route_name = db.Column(db.String(100), unique=True, nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)

    schedules = db.relationship('TransitSchedule', backref='route', lazy=True)

class TransitSchedule(db.Model):
    __tablename__ = 'transit_schedules'
    id = db.Column(db.Integer, primary_key=True)
    departure_time = db.Column(db.Time, nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('transit_routes.id'), nullable=False)

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(50), unique=True, nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

