from flask import g

from mappers.user_mappers import user_to_userdb


def insert_user_to_db(user):
    if user is None:
        return False
    client = user_to_userdb(user)
    if client is None:
        return False

    g.db.add(client)
    try:
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error inserting user: {e}")
        return False

