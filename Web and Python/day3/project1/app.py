from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/getValues', methods =['GET','POST'])
def getValues():
    #print(request.form)
    #print(request.args)
    #username=request.args['username']
    #useremail=request.args['useremail']
    username=request.form['username']
    useremail=request.form['useremail']
    print(username,useremail)
    return jsonify({"message":"posted successfully"})

if __name__ == "__main__":
    app.run()
