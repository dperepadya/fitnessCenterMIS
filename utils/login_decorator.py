from functools import wraps

from flask import session, redirect, url_for


def check_user_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = session.get('user')
        if user is None:
            # return jsonify({'message': 'User not logged in'}), 401
            return redirect(url_for('login.get_login_form'))
        return func(*args, **kwargs)
    return wrapper

