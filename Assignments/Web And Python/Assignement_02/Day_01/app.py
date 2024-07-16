from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def route_planner():
    return render_template('route_planner.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Start the application on port 5001 with debug mode enabled

