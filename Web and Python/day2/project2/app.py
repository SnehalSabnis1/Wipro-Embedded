import sys
import pymysql
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
conn = pymysql.connect(host="localhost",user="root",password="rps@123",db="demodb_1")

@app.route('/')
def hello():
    return render_template("index-validation.html")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/testcss')
def testcss():
    list_of_names = [
        {'name':'bob','age':13},        
        {'name':'john','age':17},
        {'name':'pat','age':15}
    ]
    return render_template('testcss.html',names=list_of_names)

@app.route('/getValues', methods = ['GET','POST'])
def getValues():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        #print(name, email, password)
        cur = conn.cursor()
        try:
            cur.execute("insert into loginusers(username,useremail,password) values('{}','{}','{}')".format(name,email,password))
            conn.commit()
        except pymysql.Error as e:
            print(e,sys.exc_info())
            return "error adding records"
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run()