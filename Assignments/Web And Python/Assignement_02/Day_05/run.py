
from app import app, db
from flask import render_template, redirect, url_for, flash
from forms import RouteForm, ScheduleForm
from models import Route, Schedule

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manage_routes', methods=['GET', 'POST'])
def manage_routes():
    form = RouteForm()
    if form.validate_on_submit():
        route = Route(name=form.name.data, start_location=form.start_location.data, end_location=form.end_location.data)
        db.session.add(route)
        db.session.commit()
        flash('Route added successfully!')
        return redirect(url_for('manage_routes'))
    routes = Route.query.all()
    return render_template('manage_routes.html', form=form, routes=routes)

@app.route('/manage_schedules', methods=['GET', 'POST'])
def manage_schedules():
    form = ScheduleForm()
    if form.validate_on_submit():
        schedule = Schedule(route_id=form.route_id.data, departure_time=form.departure_time.data, arrival_time=form.arrival_time.data)
        db.session.add(schedule)
        db.session.commit()
        flash('Schedule added successfully!')
        return redirect(url_for('manage_schedules'))
    schedules = Schedule.query.all()
    return render_template('manage_schedules.html', form=form, schedules=schedules)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)



