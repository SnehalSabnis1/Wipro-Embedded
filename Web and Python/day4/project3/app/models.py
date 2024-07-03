from app import db

class Product(db.Model):
    __tablename__="products"
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(50))
    productunit = db.Column(db.String(50))