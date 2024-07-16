from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy data store
users = {}

@app.route('/')
def home():
    return 'Welcome to the Insurance Claim Processing System!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if username in users:
            flash('Username already exists.')
            return redirect(url_for('register'))

        users[username] = {
            'email': email,
            'password': generate_password_hash(password)
        }

        flash('Registration successful!')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)

        if user and check_password_hash(user['password'], password):
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
   app.run(port=5001, debug=True)  # Start the application on port 5001 with debug mode enabled


