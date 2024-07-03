from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("hello.html")

@app.route('/getValues', methods = ['GET','POST'])
def getValues():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        print(username)
        print(email)
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run()