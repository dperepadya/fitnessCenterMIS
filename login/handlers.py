from database.sqlite_utils import SQLLiteDatabase
from utils.query_generators import QueryGenerator as qg


def authenticate(username, password):
    if username and password:
        user = get_user_from_db(username, password)
        # print(user['client_name'])
        return user
    else:
        return None


def get_user_from_db(username, password):
    # db command
    table = 'credentials'
    select_params = {'clients.id': 'client_id', 'name': 'client_name', 'funds': 'client_funds',
                     'clients.fitness_center_id': 'fitness_center_id'}
    join_tables = ['clients']
    join_params = {'client_id': 'id'}
    where_cond = {'credentials.login': username, 'credentials.password': password}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)

    with SQLLiteDatabase('fitnessdb.db') as db:
        user = db.fetch(query, False)
    if user:
        return user
    else:
        return None

