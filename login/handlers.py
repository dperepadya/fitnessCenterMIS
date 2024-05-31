import os
import sqlite3

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
    select_params = {'clients.id': 'client_id', 'name': 'client_name', 'funds': 'client_funds'}
    join_tables = ['clients']
    join_params = {'client_id': 'id'}
    where_cond = {'credentials.login': username, 'credentials.password': password}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    '''
    query = ("SELECT clients.id AS client_id, name AS client_name FROM credentials"
            " JOIN clients ON credentials.client_id = clients.id"
            " WHERE credentials.login = 'larry123' AND credentials.password = '12345'")
    query = 'select name from clients where id=1'
    conn = sqlite3.connect('fitnessdb.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query)
    print(query)
    res = cursor.fetchone()
    #conn.close()
    return res
    '''
    with SQLLiteDatabase('fitnessdb.db') as db:
        user = db.fetch(query, False)
    if user:
        return user
    else:
        return None

