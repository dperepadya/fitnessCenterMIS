from databases.sqlite_utils import SQLLiteDatabase
from models.user import User
from utils.query_generators import QueryGenerator as qg


def authenticate(username, password):
    if username and password:
        user = get_user_from_db(username, password)
        return user
    else:
        return None


def get_user_from_db(username, password):
    # db command
    with SQLLiteDatabase('fitnessdb.db') as db:
        table = 'credentials'
        select_params = {'clients.id': 'client_id', 'name': 'client_name'}
        join_tables = ['clients']
        join_params = {'client_id': 'id'}
        where_cond = {'credentials.login': username, 'credentials.password': password}
        query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
        user = db.fetch(query, False)
    if user:
        return user
    else:
        return None
