from database.sqlite_utils import SQLLiteDatabase
from models.user import User

from utils.query_generators import QueryGenerator as qg


def insert_to_db(user):
    with SQLLiteDatabase('fitnessdb.db') as db:

        query = qg.get_insert_sql_query('clients', {'name': user.name, 'address': user.address,
                                                    'date_of_birth': user.date_of_birth, 'phone': user.phone,
                                                    'email': user.email})
        print(query)
        result = db.commit(query, False)

    return result
