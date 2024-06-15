from datetime import datetime, timedelta

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

# User reservations handle


def add_user_order_to_db(order):
    # db command
    if order is None:
        return False
    query = qg.get_insert_sql_query('orders', {'date': order.date, 'time': order.time,
                                               'client_id': order.client_id, 'trainer_id': order.trainer_id,
                                               'service_id': order.service_id})
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


def get_trainer_services_list():
    # db command
    table = 'trainer_services'
    params = None
    where_conditions = None
    query = qg.get_select_sql_query(table, params, where_conditions)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        trainer_service = db.fetch(query)
    if trainer_service is not None:
        return trainer_service
    else:
        return None


def get_trainer_service(trainer_service_id):
    # db command
    table = 'trainer_services'
    params = None
    where_conditions = {'id': trainer_service_id}
    query = qg.get_select_sql_query(table, params, where_conditions)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        trainer_service = db.fetch(query, False)
    if trainer_service is not None:
        return trainer_service
    else:
        return None


def get_trainer_cshedule(trainer_id, date):
    table = 'schedules'
    params = None
    where_conditions = {'trainer_id': trainer_id, 'date': date}
    query = qg.get_select_sql_query(table, params, where_conditions)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        schedule = db.fetch(query, False)
    if schedule is None:
        return None
    return schedule


def get_orders_from_db(client_id, service_id, trainer_id, date):
    table = 'orders'
    params = None
    where_conditions = {'client_id': client_id, 'service_id': service_id, 'trainer_id': trainer_id, 'date': date}
    query = qg.get_select_sql_query(table, params, where_conditions)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        orders = db.fetch(query)
    if orders is None:
        return None
    return orders


def get_available_time_slots(client_id, trainer_service_id, date):
    trainer_service = get_trainer_service(trainer_service_id)
    if trainer_service is None:
        return None
    trainer_id = trainer_service['trainer_id']
    service_id = trainer_service['service_id']
    capacity = trainer_service['capacity']
    # Get trainer schedule
    schedule = get_trainer_cshedule(trainer_id, date)
    if schedule is None:
        return None
    date_start_time = datetime.strptime(schedule['start_time'], '%H:%M')
    date_end_time = datetime.strptime(schedule['end_time'], '%H:%M')
    # Get booked slots on the date
    orders = get_orders_from_db(client_id, service_id, trainer_id, date)
    if orders is None:
        return None
    booked_slots = [datetime.strptime(order['time'], '%H:%M') for order in orders]

    slots = []
    current_time = date_start_time
    while current_time < date_end_time - timedelta(minutes=capacity):
        slot_end_time = current_time + timedelta(minutes=capacity)
        overlap = False
        for booked_time in booked_slots:
            booked_end_time = booked_time + timedelta(minutes=capacity)
            if max(current_time, booked_time) < min(slot_end_time, booked_end_time):
                overlap = True
                break
        if not overlap:
            slots.append(current_time.strftime("%H:%M"))
        current_time += timedelta(minutes=15)
    return slots


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



