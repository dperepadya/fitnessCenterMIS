from flask import g

from database.database import db_session
from mappers.user_mappers import user_to_userdb


def insert_user_to_db(user):
    if user is None:
        return False
    client = user_to_userdb(user)
    if client is None:
        return False

    db_session.add(client)
    try:
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        print(f"Error inserting user: {e}")
        return False

