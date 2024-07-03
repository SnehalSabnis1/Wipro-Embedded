from flask import Flask

#create an flask instance
app = Flask(__name__)

#flask will by default start at port 5000
#http://127.0.0.1:5000  - / ('/' is the top level url of the application)
#create a route for '/'
@app.route('/')
def hello():
    return "<h1>helloworld</h1>"

@app.route('/exampleUrl')
def example():
    return "<h1>from example url</h1>"

if __name__ == '__main__':
    app.run()  #starts the application at port 5000