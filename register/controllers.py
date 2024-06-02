from flask import Blueprint, jsonify, request, render_template
from register import handlers as hndl
from models.user import User

register_bp = Blueprint('register', __name__)


# Get a Registration form
@register_bp.get('/')
def get_user_registration_form():
    return render_template('client_register.html')


# Add a user to DB
@register_bp.post('/')
def add_user():
    user_data = request.form
    user = User(user_data['name'], user_data['date_of_birth'], user_data['address'], user_data['phone'],
                user_data['email'])
    result = hndl.insert_user_to_db(user)
    if result is not None:
        return jsonify({'message': f"New user {user.name}: created successfully"}), 201
    else:
        return jsonify({'message': 'Cannot create new user '}), 400
