from flask import g

from database.sqlalchemy_utils import Session
from db_models.credentials import Credential
from db_models.user import Client
from mappers.user_mapper import client_to_user


def authenticate(username, password):
    if username and password:
        user = get_user_from_db(username, password)
        # print(user['client_name'])
        if user:
            return client_to_user(user)
        return user
    else:
        return None


def get_user_from_db(username, password):
    user = g.db.query(Client).join(Credential).filter(
        Credential.login == username, Credential.password == password
    ).first()

    if user:
        return user
    else:
        return None
