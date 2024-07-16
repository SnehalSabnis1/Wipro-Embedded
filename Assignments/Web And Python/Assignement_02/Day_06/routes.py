from flask import Blueprint, request, jsonify
from models import db, TransitRoute, TransitSchedule, Vehicle

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return "Welcome to the Smart City Transportation Management System"

# CRUD operations for transit routes
@main_blueprint.route('/route', methods=['POST'])
def create_route():
    data = request.get_json()
    new_route = TransitRoute(
        route_name=data['route_name'],
        origin=data['origin'],
        destination=data['destination']
    )
    db.session.add(new_route)
    db.session.commit()
    return jsonify({'message': 'New route created'}), 201

@main_blueprint.route('/route/<int:id>', methods=['GET'])
def get_route(id):
    route = TransitRoute.query.get_or_404(id)
    return jsonify({
        'route_name': route.route_name,
        'origin': route.origin,
        'destination': route.destination
    })

@main_blueprint.route('/route/<int:id>', methods=['PUT'])
def update_route(id):
    data = request.get_json()
    route = TransitRoute.query.get_or_404(id)
    route.route_name = data['route_name']
    route.origin = data['origin']
    route.destination = data['destination']
    db.session.commit()
    return jsonify({'message': 'Route updated'})

@main_blueprint.route('/route/<int:id>', methods=['DELETE'])
def delete_route(id):
    route = TransitRoute.query.get_or_404(id)
    db.session.delete(route)
    db.session.commit()
    return jsonify({'message': 'Route deleted'})

# CRUD operations for transit schedules
@main_blueprint.route('/schedule', methods=['POST'])
def create_schedule():
    data = request.get_json()
    new_schedule = TransitSchedule(
        departure_time=data['departure_time'],
        arrival_time=data['arrival_time'],
        route_id=data['route_id']
    )
    db.session.add(new_schedule)
    db.session.commit()
    return jsonify({'message': 'New schedule created'}), 201

@main_blueprint.route('/schedule/<int:id>', methods=['GET'])
def get_schedule(id):
    schedule = TransitSchedule.query.get_or_404(id)
    return jsonify({
        'departure_time': schedule.departure_time.strftime('%H:%M:%S'),
        'arrival_time': schedule.arrival_time.strftime('%H:%M:%S'),
        'route_id': schedule.route_id
    })

@main_blueprint.route('/schedule/<int:id>', methods=['PUT'])
def update_schedule(id):
    data = request.get_json()
    schedule = TransitSchedule.query.get_or_404(id)
    schedule.departure_time = data['departure_time']
    schedule.arrival_time = data['arrival_time']
    schedule.route_id = data['route_id']
    db.session.commit()
    return jsonify({'message': 'Schedule updated'})

@main_blueprint.route('/schedule/<int:id>', methods=['DELETE'])
def delete_schedule(id):
    schedule = TransitSchedule.query.get_or_404(id)
    db.session.delete(schedule)
    db.session.commit()
    return jsonify({'message': 'Schedule deleted'})

# CRUD operations for vehicles
@main_blueprint.route('/vehicle', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    new_vehicle = Vehicle(
        vehicle_number=data['vehicle_number'],
        vehicle_type=data['vehicle_type'],
        capacity=data['capacity']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({'message': 'New vehicle created'}), 201

@main_blueprint.route('/vehicle/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    return jsonify({
        'vehicle_number': vehicle.vehicle_number,
        'vehicle_type': vehicle.vehicle_type,
        'capacity': vehicle.capacity
    })

@main_blueprint.route('/vehicle/<int:id>', methods=['PUT'])
def update_vehicle(id):
    data = request.get_json()
    vehicle = Vehicle.query.get_or_404(id)
    vehicle.vehicle_number = data['vehicle_number']
    vehicle.vehicle_type = data['vehicle_type']
    vehicle.capacity = data['capacity']
    db.session.commit()
    return jsonify({'message': 'Vehicle updated'})

@main_blueprint.route('/vehicle/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle deleted'})

# Advanced data retrieval and reporting
@main_blueprint.route('/route/<int:id>/schedules', methods=['GET'])
def get_route_schedules(id):
    schedules = TransitSchedule.query.filter_by(route_id=id).all()
    return jsonify([
        {
            'departure_time': schedule.departure_time.strftime('%H:%M:%S'),
            'arrival_time': schedule.arrival_time.strftime('%H:%M:%S'),
        } for schedule in schedules
    ])

@main_blueprint.route('/vehicles/report', methods=['GET'])
def get_vehicles_report():
    total_vehicles = db.session.query(db.func.count(Vehicle.id)).scalar()
    total_capacity = db.session.query(db.func.sum(Vehicle.capacity)).scalar()
    report = {
        'total_vehicles': total_vehicles,
        'total_capacity': total_capacity
    }
    return jsonify(report)
