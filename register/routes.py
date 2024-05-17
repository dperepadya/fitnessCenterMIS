from flask import Blueprint, jsonify, request
import services as svs
from models.user import User

register_bp = Blueprint('register', __name__)


# Get a Registration form
@register_bp.get('/')
def get_registration_form():
    params = {'Name', 'Date of birth', 'Address', 'Phone', 'Email'}
    return jsonify(params)


# Add a user to DB
@register_bp.post('/')
def new_user():
    user_data = request.json
    user = User(user_data['username'], user_data['date of birth'], user_data['address'], user_data['phone'],
                user_data['email'])
    result = svs.insert_to_db(user)
    if result:
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'message': 'Cannot create new user '}), 400
