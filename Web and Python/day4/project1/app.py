from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/getValues', methods=(['get','post']))
def getValues():
    customername=request.form['customername']  #when method is post we use request.form
    customeremail=request.form['customeremail']
    print(customername,customeremail)
    return jsonify({'customername':customername},{"customeremail":customeremail})

@app.route('/userdetails',methods=(['get','post']))
def userdetails():
    customername=request.form['customername']  #when method is post we use request.form
    customeremail=request.form['customeremail']
    print(customername,customeremail)
    return jsonify({'customername':customername},{"customeremail":customeremail})
  
if __name__=="__main__":
    app.run()
