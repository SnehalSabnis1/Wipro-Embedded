from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def transit_map():
    return render_template('transit_map.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Start the application on port 5001 with debug mode enabled

