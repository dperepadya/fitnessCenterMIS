from flask import jsonify

from models.user import User


def get_user_from_db(user_id):
    # db command
    user = None
    if user:
        return user
    else:
        return None


def update_user_in_db(user):
    if user:
        # db command
        return True
    return False



