from database.sqlite_utils import SQLLiteDatabase
from utils.query_generators import QueryGenerator as qg


def get_fitness_centers_from_db():
    # db command
    with SQLLiteDatabase('fitnessdb.db') as db:
        table = 'fitness_centers'
        select_params = {'name': 'fc_name'}
        query = qg.get_select_sql_query(table, select_params)
        print(query)
        fc_list = db.fetch(query, True)
    return fc_list


def add_fitness_centers_to_db():
    # db command
    return True


def get_fitness_center_from_db(fc_id):
    # db command
    table = 'fitness_centers'
    select_params = None
    where_params = {'id': str(fc_id)}
    query = qg.get_select_sql_query(table, select_params, where_params)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc = db.fetch(query)
    return fc


def modify_fitness_center_in_db(fc_id):
    # db command
    return True


def get_fitness_center_bonuses_from_db():
    return None


def get_fitness_center_services_from_db(fc_id):
    # db command
    table = 'services'
    select_params = {'services.name': 'service_name'}
    join_tables = ['fitness_centers']
    join_params = {'fitness_center_id': 'id'}
    where_cond = {'fitness_center_id': fc_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_services = db.fetch(query, True)
    return fc_services


def get_fitness_center_service_from_db(fc_id, serv_id):
    # db command
    table = 'services'
    select_params = {'services.name': 'service_name'}
    join_tables = ['fitness_centers']
    join_params = {'fitness_center_id': 'id'}
    where_cond = {'fitness_center_id': fc_id, 'services.id': serv_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_service = db.fetch(query)
    return fc_service


def add_fitness_center_service_to_db(serv):
    # db command
    return True


def modify_fitness_center_service_in_db(fc_id, serv_id):
    # db command
    return True


def delete_fitness_center_service_from_db(fc_id, serv_id):
    # db command
    return True


def get_fitness_center_trainers_from_db(fc_id):
    # db command
    table = 'trainers'
    select_params = {'trainers.name': 'trainer_name'}
    join_tables = ['fitness_centers']
    join_params = {'fitness_center_id': 'id'}
    where_cond = {'fitness_center_id': fc_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_trainers = db.fetch(query, True)
    return fc_trainers


def get_fitness_center_trainer_from_db(fc_id, trainer_id):
    # db command
    table = 'trainers'
    select_params = {'trainers.name': 'trainer_name'}
    join_tables = ['fitness_centers']
    join_params = {'fitness_center_id': 'id'}
    where_cond = {'fitness_center_id': fc_id, 'trainers.id': trainer_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_trainer = db.fetch(query)
    return fc_trainer


def add_fitness_center_trainer_to_db(trainer):
    # db command
    return True


def modify_fitness_center_trainer_in_db(fc_id, trainer_id):
    # db command
    return True


def delete_fitness_center_trainer_from_db(fc_id, trainer_id):
    # db command
    return True


def get_fitness_center_trainer_rating_from_db(fc_id, trainer_id):
    # db command
    table = 'reviews'
    select_params = {'clients.name': 'client_name', 'reviews.grade': 'grade'}
    join_tables = ['clients', 'trainers']
    join_params = {'client_id': 'id', 'trainer_id': 'id'}
    where_cond = {'trainers.fitness_center_id': fc_id, 'trainers.id': trainer_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_trainer_rating = db.fetch(query, True)
    return fc_trainer_rating


def set_fitness_center_trainer_rating(fc_id, trainer_id):
    return True


def modify_fitness_center_trainer_rating_in_db(fc_id, trainer_id):
    return True


def get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id):
    # db command
    table = 'schedules'
    select_params = {'trainers.name': 'trainer_name', 'schedules.date': 'date', 'schedules.start_time': 'start_time',
                     'schedules.end_time': 'end_time'}
    join_tables = ['trainers']
    join_params = {'trainer_id': 'id'}
    where_cond = {'trainers.fitness_center_id': fc_id, 'trainers.id': trainer_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_trainer_schedule = db.fetch(query, True)
    return fc_trainer_schedule


def add_fitness_center_trainer_schedule(fc_id, trainer_id):
    return True


def modify_fitness_center_trainer_schedule_in_db(fc_id, trainer_id):
    return True


def get_fitness_center_services_and_trainers_from_db(fc_id, serv_id):
    # db command
    table = 'trainers'
    select_params = {'trainers.name': 'trainer_name'}
    join_tables = ['services', 'fitness_centers']
    join_params = {'service_id': 'id', 'fitness_center_id': 'id'}
    where_cond = {'fitness_centers.id': fc_id, 'services.id': serv_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_serv_trainers = db.fetch(query, True)
    return fc_serv_trainers


def add_trainer_to_fitness_center_service_in_db(fc_id, serv_id, trainer):
    return True


def get_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id):
    # db command
    table = 'trainers'
    select_params = {'trainers.name': 'trainer_name'}
    join_tables = ['services', 'fitness_centers']
    join_params = {'service_id': 'id', 'fitness_center_id': 'id'}
    where_cond = {'fitness_centers.id': fc_id, 'services.id': serv_id, 'trainers.id': trainer_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_serv_trainer = db.fetch(query)
    return fc_serv_trainer


def modify_fitness_center_service_trainer_in_db(fc_id, serv_id, trainer_id):
    return True


def delete_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id):
    return True










