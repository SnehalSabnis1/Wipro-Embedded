from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "helloworld"

if __name__ == "__main__":
    app.run(port=5500,host="0.0.0.0")
