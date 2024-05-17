from flask import Blueprint, jsonify, request, session
import services as svs
from models.user import User

user_bp = Blueprint('user', __name__)

# Get user info
@user_bp.get('/')
def get_user():
    user = session.get('user') # User is defined after Login
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not logged in'}), 401


# A user can be added with /register POST command, isn't it?
@user_bp.post('/')
def new_user():
    return None


# Update User info
@user_bp.put('/')
def update_user():
    user_data = request.json
    user = User(user_data['username'], user_data['date of birth'], user_data['address'], user_data['phone'], user_data['email'])
    if svs.update_user_in_db(user):
        return jsonify({'message': 'User info updated successfully'}), 201
    else:
        return jsonify({'message': 'Cannot update user'}), 404


# Get User balance
@user_bp.get('/funds')
def get_user():
    user = session.get('user') # User is defined after Login
    if user:
        return jsonify(user['funds']), 200
    else:
        return jsonify({'message': 'Cannot get user balance'}), 404


# Top up User balance
@user_bp.put('/funds')
def update_user():
    amount = request.json
    user = session.get('user')  # User is defined after Login
    if user and amount and amount > 0:
        user.funds += amount
        if svs.update_user_in_db(user):
            return jsonify({'message': 'User account was successfully funded'}), 200
        return jsonify({'message': 'Cannot top up User account'}), 400
    else:
        return jsonify({'message': 'Cannot top up User account'}), 400


# Get User cart information
@user_bp.get('/cart')
def get_user_cart():
    user = svs.get_user_from_db(user)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404
