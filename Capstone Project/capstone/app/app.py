from urllib.parse import quote_plus
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from datetime import datetime,timedelta
import os


host = os.environ.get('localhost') 
port = os.environ.get('3306') 
username = os.environ.get('root') 
password = os.environ.get('Snehal@0202') 
database = os.environ.get('db1')


app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisarandomgeneratedstring"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:{}@localhost:3306/db1".format(quote_plus("Snehal@0202"))

db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    _tablename_ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(512))

class BookIssue(db.Model):
    _tablename_ = "book_issue"
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/')
def hello():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if len(password) < 4 or len(password) > 8:
            return jsonify({'error': 'Password must be between 4 and 8 characters long.'})
        if not password.isalnum():
            return jsonify({'error': 'Password must contain only letters and numbers.'})
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        session['username'] = username
        return render_template("book.html")

@app.route('/book', methods=['GET'])
def book():
    return render_template("book.html")

@app.route('/fiction', methods=['GET'])
def fiction():
    return render_template("fiction.html")

@app.route('/comics', methods=['GET'])
def comics():
    return render_template("comics.html")
    
@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        username = session.get('username')
        if not username:
            flash('User not logged in!')
            return redirect(url_for('login'))
        
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('User not found!')
            return redirect(url_for('login'))
        
        cart_items = request.form.getlist('books[]')
        
        for book_name in cart_items:
            start_date = request.form.get(f'start-{book_name}')
            end_date = request.form.get(f'end-{book_name}')
            if not start_date or not end_date:
                flash('Start date and end date are required for each book!')
                return redirect(url_for('cart'))
            
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            
            book_issue = BookIssue(
                book_name=book_name,
                start_date=start_date,
                end_date=end_date,
                user_id=user.id
            )
            db.session.add(book_issue)
        
        db.session.commit()
        return redirect(url_for("thank_you.html"))
    
    # Assuming you have a way to get books in the user's cart
    books = []  # Replace with actual query to get books in the cart
    return render_template("cart.html", books=books)

@app.route('/thank_you', methods=['GET'])
def thank_you():
    return render_template("thank_you.html")

@app.route('/user', methods=['GET'])
def user():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {'id': user.id, 'username': user.username}
        user_list.append(user_data)
    return jsonify({'users': user_list})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)