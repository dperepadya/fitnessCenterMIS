from db_models.client import Client
from models.user import User


def userdb_to_user(user):
    user = User(
        name=user.name,
        date_of_birth=user.date_of_birth,
        address=user.address,
        phone=user.phone,
        email=user.email,
    )
    user.fitness_center_id = user.fitness_center_id
    return user


def userdb_to_userdict(user):
    return {
        'id': user.id,
        'name': user.name,
        'funds': user.funds,
        'fitness_center_id': user.fitness_center_id
    }


def user_to_userdb(user):
    client = Client(
        name=user.name,
        date_of_birth=user.date_of_birth,
        address=user.address,
        phone=user.phone,
        email=user.email,
        funds=user.funds,
        fitness_center_id=user.fitness_center_id
    )
    return client


def existing_user_to_userdb(existing_user, user):
    if existing_user is None or user is None:
        return None
    existing_user.name = user.name,
    existing_user.date_of_birth = user.date_of_birth,
    existing_user.address = user.address,
    existing_user.phone = user.phone,
    existing_user.email = user.email,
    existing_user.funds = user.funds
    existing_user.fitness_center_id = user.fitness_center_id

