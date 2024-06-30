from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from register import orm_handlers as hndl
from models.user import User
from celery_tasks import send_mail

register_bp = Blueprint('register', __name__)


# Get a Registration form
@register_bp.get('/')
def get_user_registration_form():
    return render_template('client_register.html')


# Add a user to DB
@register_bp.post('/')
def add_user():
    user_data = request.form
    # noinspection PyBroadException
    try:
        if user_data['fc_id'] is None:
            redirect("/register")
        user = User(user_data['name'], user_data['date_of_birth'], user_data['address'], user_data['phone'],
                    user_data['email'])
        user.fitness_center_id = int(user_data['fc_id'])
    except Exception:
        return redirect("/register")
    result = hndl.insert_user_to_db(user)
    if result:
        msg = f"New client {user.name}: successfully registered"
        # print(user_data['email'], msg)
        subject = 'Successful registration at fitness center'
        send_mail.delay(user_data['email'], subject, msg)
        # return jsonify({'message': msg}), 201
        return redirect("/login")
    else:
        # return jsonify({'message': 'Cannot create new user '}), 400
        return redirect("/register")
