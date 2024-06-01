from database.sqlite_utils import SQLLiteDatabase
from utils.query_generators import QueryGenerator as qg


def get_user_from_db(user_id):
    # db command
    user = None
    if user:
        return user
    else:
        return None


def update_user_in_db(user):
    if user:
        # db command
        return True
    return False


def get_user_cart_from_db(user):
    # db command
    cart = None
    return cart


def get_user_cart_item_from_db(user, item_id):
    item = None
    return item


def delete_user_cart_item_from_db(user, item_id):
    # db command
    return True


def edit_user_cart_item_in_db(user, item_id):
    # db command
    return True


def add_user_order_to_db(user):
    return True


def get_user_orders_from_db(user_id):
    # db command
    table = 'orders'
    select_params = {'orders.id': 'order_id', 'services.name': 'service_name',
                     'trainers.name': 'trainer_name'}
    join_tables = ['clients', 'services', 'trainers']
    join_params = {'client_id': 'id', 'service_id': 'id', 'trainer_id': 'id'}
    where_cond = {'clients.id': user_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        orders = db.fetch(query, True)
    return orders


def get_user_order_from_db(user_id, ord_id):
    # db command
    table = 'orders'
    select_params = {'services.name': 'service_name',
                     'trainers.name': 'trainer_name'}
    join_tables = ['clients', 'services', 'trainers']
    join_params = {'client_id': 'id', 'service_id': 'id', 'trainer_id': 'id'}
    where_cond = {'clients.id': user_id, 'orders.id': ord_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        order = db.fetch(query)
    return order


def edit_user_order_in_db(user):
    return True


def delete_user_order_from_db(user, ord_id):
    return True




