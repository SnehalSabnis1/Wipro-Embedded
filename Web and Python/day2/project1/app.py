from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "index method"

@app.route('/hello')
def hello():
    #list_of_names = ['bob','pat','sam'] 
    list_of_names = [
        {'name':'bob','age':12},
        {'name':'pat','age':10},
        {'name':'sam','age':13},
        ]
    return render_template('hello.html', names= list_of_names)

if __name__ == '__main__':
    app.run()