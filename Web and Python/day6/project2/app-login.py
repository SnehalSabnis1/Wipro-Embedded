import os
import time
from flask import Flask, abort, request, jsonify, g, url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import quote_plus

#Initialize variables
app = Flask(__name__)
app.config['SECRET_KEY'] = 'use a random string to construct the hash'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:{}@localhost:3306/demodb_3".format(quote_plus("rps@123"))

db = SQLAlchemy(app)  
auth = HTTPBasicAuth()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(200))

    def hash_password(self, password):
        self.password_hash =  generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    
@auth.verify_password
def verify_password(username_or_token, password):
    
    user = User.query.filter_by(username = username_or_token).first()
        
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

@app.route('/')
def hello():
    return render_template("index_with_authorization.html")

@app.route('/api/register', methods=['GET','POST'])
def register():
    username = request.json.get('username') 
    password = request.json.get('password')
    print(username,password)
    # Check for blank requests
    if username is None or password is None:
        abort(400)
    # Check for existing users
    if User.query.filter_by(username = username).first() is not None:
        abort(400)
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201)


@app.route('/api/dothis', methods=['GET','POST'])
@auth.login_required
def do_this():
    return jsonify({ 'message':'It is done {}'.format(g.user.username) })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()