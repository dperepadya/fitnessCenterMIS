from db_models.client import Client
from models.user import User


def userdb_to_user(client):
    return User(
        name=client.name,
        date_of_birth=client.date_of_birth,
        address=client.address,
        phone=client.phone,
        email=client.email
    )


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
        funds=user.funds
    )
    client.id = user.id
    return client
