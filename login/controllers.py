from flask import Blueprint, jsonify, request, session, render_template, redirect, url_for
from login import orm_handlers as hndl

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
    user = hndl.authenticate(username, password)
    if user is None:
        return redirect(url_for('login.get_login_form'))
    session['user'] = user
    return jsonify({'message': f"{user['name']}: Login successful"}), 200

