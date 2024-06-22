from flask import Blueprint, jsonify, request, render_template
from register import orm_handlers as hndl
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
    user.fitness_center_id = int(user_data['fc_id'])
    result = hndl.insert_user_to_db(user)
    if result:
        msg = f"New user {user.name}: created successfully"

        # send_mail.apply_async(user_data['email'], msg)

        return jsonify({'message': msg}), 201
    else:
        return jsonify({'message': 'Cannot create new user '}), 400
