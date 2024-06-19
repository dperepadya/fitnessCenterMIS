from flask import g
import logging
from database.database import db_session
from db_models.credentials import Credentials
from db_models.client import Client
from mappers.user_mappers import userdb_to_userdict


def authenticate(username, password):
    if username is None or password is None:
        return False
    user = get_user_from_db(username, password)
    # print(user.name)
    if user is None:
        return None
    return userdb_to_userdict(user)


def get_user_from_db(username, password):
    try:
        user = (db_session.query(Client)
                .join(Credentials)
                .filter(Credentials.login == username, Credentials.password == password).first())
        return user
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
