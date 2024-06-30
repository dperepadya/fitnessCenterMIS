from functools import wraps

from flask import session, redirect, url_for


def user_is_logged_in():
    return session.get('user') is not None


def check_user_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # user = session.get('user')
        if not user_is_logged_in():
            # return jsonify({'message': 'User not logged in'}), 401
            return redirect("/login")
        return func(*args, **kwargs)
    return wrapper


def user_is_admin():
    user = session.get('user')
    if user is None:
        return False
    user_name = user['name']
    return user_name is not None and user_name == 'Administrator'


def check_admin_rights(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not user_is_admin():
            return redirect("login/")
        return func(*args, **kwargs)
    return wrapper
