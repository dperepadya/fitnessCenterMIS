from flask import Blueprint, session, redirect, url_for

logout_bp = Blueprint('logout', __name__)


# Get a Login form
@logout_bp.get('/')
def user_logout():
    session.pop('user', None)
    return redirect(url_for('login.get_login_form'))


