from database.sqlite_utils import SQLLiteDatabase
from utils.query_generators import QueryGenerator as qg


def get_user_from_db(user_id):
    # db command
    table = 'clients'
    params = None
    where_conditions = {'id': user_id}
    query = qg.get_select_sql_query(table, params, where_conditions)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        user = db.fetch(query, False)
    if user:
        return user
    else:
        return None


def update_user_in_db(user):
    if user is None:
        return False
    # db command
    query = qg.get_update_sql_query('clients',
                                    {'name': user.name, 'date_of_birth': user.date_of_birth,
                                     'address': user.address, 'phone': user.phone, 'email': user.email,
                                     'funds': user.funds},
                                    {"id": user.id})
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


def update_user_funds_in_db(user_id, funds):
    if funds == 0:
        return True
    # db command
    query = qg.get_update_sql_query('clients',
                                    {'funds': funds},
                                    {"id": user_id})
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


def add_user_order_to_db(user):
    return True


def get_user_orders_from_db(user_id):
    # db command
    table = 'orders'
    select_params = {'orders.id': 'order_id', 'services.name': 'service_name', 'trainers.name': 'trainer_name',
                     'orders.service_id': 'service_id', 'orders.trainer_id': 'trainer_id',
                     'orders.date': 'date', 'orders.time': 'time'}
    join_tables = ['clients', 'services', 'trainers']
    join_params = {'client_id': 'id', 'service_id': 'id', 'trainer_id': 'id'}
    where_cond = {'clients.id': user_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        orders = db.fetch(query)
    return orders


def get_user_order_from_db(user_id, ord_id):
    # db command
    table = 'orders'
    select_params = {'orders.id': 'order_id', 'services.name': 'service_name', 'trainers.name': 'trainer_name',
                     'orders.service_id': 'service_id', 'orders.trainer_id': 'trainer_id',
                     'orders.date': 'date', 'orders.time': 'time'}
    join_tables = ['clients', 'services', 'trainers']
    join_params = {'client_id': 'id', 'service_id': 'id', 'trainer_id': 'id'}
    where_cond = {'clients.id': user_id, 'orders.id': ord_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        order = db.fetch(query, False)
    return order


def edit_user_order_in_db(user):
    return True


def delete_user_order_from_db(ord_id):
    table = 'orders'
    where_params = {'id': 'ord_id'}
    query = qg.get_delete_sql_query(table, where_params)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result

# Cart #########################################
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



