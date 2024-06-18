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
        'client_id': user.id,
        'client_name': user.name,
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
    client.id = user.id
    return client


def user_to_userdb(existing_user, user):
    if existing_user is None or user is None:
        return None
    existing_user.name = user.name,
    existing_user.date_of_birth = user.date_of_birth,
    existing_user.address = user.address,
    existing_user.phone = user.phone,
    existing_user.email = user.email,
    existing_user.funds = user.funds
    existing_user.id = user.id
    return existing_user
