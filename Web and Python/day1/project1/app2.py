from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    #message = "this the content from hello"
    #return render_template("hello.html",msg=message)
    #list_of_names = ['bob','pat','alice','sam']
    #return render_template("hello.html",names = list_of_names)
    list_of_names = [{'Name':'bob'},{'Name':'pat'},{'Name':'alice'},{'Name':'sam'}]
    return render_template("hello.html",names = list_of_names)


@app.route('/exampleUrl')
def example():
    return render_template("example.html")

if __name__ == '__main__':
    app.run()