from flask import request, session, Blueprint, render_template, redirect, url_for, jsonify
from login import orm_handlers as hndl

# from celery_tasks import send_mail

login_bp = Blueprint('login', __name__)


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
    msg = f"{user['name']}: Login successful"
    # send_mail.delay(user['email'], msg)
    print(user['email'], msg)
    return jsonify({'message': msg}), 200




