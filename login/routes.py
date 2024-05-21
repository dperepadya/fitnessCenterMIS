from flask import Blueprint, jsonify, request, session
import services as svs

login_bp = Blueprint('login', __name__)


# Get a Login form
@login_bp.get('/')
def get_login_form():
    params = {'Login', 'Password'}
    return jsonify(params)


# User authentication
@login_bp.post('/')
def login():
    login_data = request.json
    username = login_data['username']
    password = login_data['password']

    user = svs.authenticate(username, password)
    if user:
        session['user'] = user
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
