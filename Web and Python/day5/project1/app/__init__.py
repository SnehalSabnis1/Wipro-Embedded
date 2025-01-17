import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    from .models import Customer
    app = Flask(__name__, instance_path=os.getcwd(),instance_relative_config=True)
    app.config.from_pyfile('config.py')
    package_dir = os.path.dirname(
    os.path.abspath(__file__)
    )
    static = os.path.join(
    package_dir, "static"
    )
    app.static_folder=static
    db.init_app(app)
    Migrate(app,db)

    @app.route('/')
    def hello():
        return render_template("index.html")

    @app.route('/addcustomer', methods=['GET','POST'])
    def addcustomer():
        if request.method == "POST":
            customername = request.json['customername']
            customeremail = request.json['customeremail']
            if customername=="":
                return jsonify({"error":{"message":"customer name is blank"}})
            if customeremail=="":
                return jsonify({"error":{"message":"customer email is blank"}})
            exists = db.session.query(Customer).filter_by(customeremail=customeremail).scalar() is not None
            if exists:
                return jsonify({"error":{'message': "user already exists"}})

            customer = Customer(customername=customername,customeremail=customeremail)
            db.session.add(customer)
            db.session.commit()
            return jsonify({"success":{'message':'customer added successfully'}})
    
    return app
