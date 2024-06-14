from db_models.user import Client
from models.user import User


def client_to_user(client):
    return User(
        name=client.name,
        date_of_birth=client.date_of_birth,
        address=client.address,
        phone=client.phone,
        email=client.email
    )


def user_to_client(user):
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
