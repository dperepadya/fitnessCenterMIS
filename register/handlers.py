from database.sqlite_utils import SQLLiteDatabase

from utils.query_generators import QueryGenerator as qg


def insert_user_to_db(user):
    if user is None:
        return False

    query = qg.get_insert_sql_query('clients', {'date': user.name, 'address': user.address,
                                                'date_of_birth': user.date_of_birth, 'phone': user.phone,
                                                'email': user.email, 'funds': user.funds,
                                                'fitness_center_id': user.fitness_center_id})
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result
