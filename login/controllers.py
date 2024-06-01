from flask import Blueprint, jsonify, request, session, render_template
from login import handlers as hndl

login_bp = Blueprint('login', __name__)


# Get a Login form
@login_bp.get('/')
def get_login_form():
    return render_template('client_login.html')


# User authentication
@login_bp.post('/')
def login():
    login_data = request.form
    username = login_data['login']
    password = login_data['password']
    # username = 'larry123'
    # password = '12345'
    user = hndl.authenticate(username, password)
    if user is not None:
        session['user'] = user
        return jsonify({'message': f"{user['client_name']}: Login successful"}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
