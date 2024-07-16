from flask import Flask, render_template, request, redirect, url_for, flash
from models import TrafficData, UserPreference
from forms import TrafficQueryForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route for displaying traffic information
@app.route('/', methods=['GET', 'POST'])
def traffic_info():
    form = TrafficQueryForm()
    if form.validate_on_submit():
        user_location = form.user_location.data
        destination = form.destination.data
        
        # Fetch real-time traffic data (pseudo code)
        traffic_data = TrafficData.get_traffic_info(user_location, destination)
        alternative_routes = TrafficData.get_alternative_routes(user_location, destination)
        
        return render_template('traffic_info.html', form=form, traffic_data=traffic_data, alternative_routes=alternative_routes)
    return render_template('traffic_info.html', form=form, traffic_data=None, alternative_routes=None)

# Route for displaying alternative routes
@app.route('/alternative-routes')
def alternative_routes():
    return render_template('alternative_routes.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Start the application on port 5001 with debug mode enabled
