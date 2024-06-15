from flask import g

from database.sqlalchemy_utils import Session
from db_models.credentials import Credential
from db_models.client import Client
from mappers.user_mappers import userdb_to_userdict


def authenticate(username, password):
    if username and password:
        user = get_user_from_db(username, password)
        # print(user['client_name'])
        if user:
            return userdb_to_userdict(user)
        return user
    else:
        return None


def get_user_from_db(username, password):
    try:
        user = g.db.query(Client).join(Credential).filter(
            Credential.login == username, Credential.password == password
        ).first()
        return user
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
