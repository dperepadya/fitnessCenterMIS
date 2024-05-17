from flask import Blueprint, jsonify, request
import services as svs
from models.user import User

fitness_center_bp = Blueprint('fitness_center', __name__)


@fitness_center_bp.get('/')
def get_fitness_center_info(fc_id):
    fc = svs.get_fitness_center_from_db(fc_id)
    if fc:
        return jsonify(fc)
    else:
        return jsonify({'message': 'Fitness center not found'}), 404


@fitness_center_bp.get('/<fc_id>')
def get_fitness_center_info(fc_id):
    fc = svs.get_fitness_center_from_db(fc_id)
    if fc:
        return jsonify(fc)
    else:
        return jsonify({'message': 'Fitness center not found'}), 404


@fitness_center_bp.post('/')
def create_user():
    user_data = request.json
    user = User(user_data['username'], user_data['email'])
    user.insert_to_db()
    return 'User created successfully', 201