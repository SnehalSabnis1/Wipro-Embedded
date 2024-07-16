from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Policy(db.Model):
    __tablename__ = 'policies'
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(50), unique=True, nullable=False)
    policy_holder_name = db.Column(db.String(100), nullable=False)
    policy_start_date = db.Column(db.Date, nullable=False)
    policy_end_date = db.Column(db.Date, nullable=False)
    premium_amount = db.Column(db.Float, nullable=False)

    claims = db.relationship('Claim', backref='policy', lazy=True)

class Claim(db.Model):
    __tablename__ = 'claims'
    id = db.Column(db.Integer, primary_key=True)
    claim_number = db.Column(db.String(50), unique=True, nullable=False)
    claim_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    claim_amount = db.Column(db.Float, nullable=False)
    claim_status = db.Column(db.String(50), nullable=False)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'), nullable=False)
