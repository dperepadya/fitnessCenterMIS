from flask import Blueprint, jsonify, request, session
from login import handlers as hndl

login_bp = Blueprint('login', __name__)


# Get a Login form
@login_bp.get('/')
def get_login_form():
    form = """<form action="/login" method="post">
        <label for="username">Login:     </label>
        <input type="text" id="login" name="login" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>       
        <input type="submit" value="Submit">
        </form>"""
    return form


# User authentication
@login_bp.post('/')
def login():
    login_data = request.form
    username = login_data['login']
    password = login_data['password']
    # username = 'larry123'
    # password = '12345'
    user = hndl.authenticate(username, password)
    if user:
        session['user'] = user
        return jsonify({'message': f"{user['client_name']}: Login successful"}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
