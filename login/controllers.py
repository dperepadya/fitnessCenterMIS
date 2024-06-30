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
        return redirect("/login")
    session['user'] = user
    fc_id = user['fitness_center_id']
    # msg = f"{user['name']}: Login successful"
    # print(user['email'], msg)
    # return jsonify({'message': msg}), 200
    return redirect(f"/fitness_center/{fc_id}")



