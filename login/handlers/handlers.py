from models.user import User


def authenticate(username, password):
    if username and password:
        user = get_user_from_db(username, password)
        return user
    else:
        return None


def get_user_from_db(username, password):
    # db command
    user = User.empty()
    if user:
        return user
    else:
        return None
