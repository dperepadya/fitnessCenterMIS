from database.sqlite_utils import SQLLiteDatabase
from utils.query_generators import QueryGenerator as qg


def get_fitness_centers_from_db():
    # db command
    with SQLLiteDatabase('fitnessdb.db') as db:
        table = 'fitness_centers'
        select_params = None  # {'name': 'fc_name'}
        query = qg.get_select_sql_query(table, select_params)
        print(query)
        fc_list = db.fetch(query)
    return fc_list


def add_fitness_center_to_db(fc):
    if fc is None:
        return False
    query = qg.get_insert_sql_query('fitness_centers', {'name': fc.name, 'address': fc.address,
                                                        'phone': fc.phone, 'email': fc.email})
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


def get_fitness_center_from_db(fc_id):
    # db command
    table = 'fitness_centers'
    select_params = None
    where_params = {'id': fc_id}
    query = qg.get_select_sql_query(table, select_params, where_params)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc = db.fetch(query, False)
    return fc


def modify_fitness_center_in_db(fc):
    query = qg.get_update_sql_query('fitness_centers', {'name': fc.name, 'address': fc.address,
                                                        'phone': fc.phone, 'email': fc.email}, {"id": fc.id})
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


def delete_fitness_center_from_db(fc_id):
    table = 'fitness_centers'
    where_params = {'id': fc_id}
    query = qg.get_delete_sql_query(table, where_params)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


def get_fitness_center_bonuses_from_db():
    return None


def get_fitness_center_services_from_db(fc_id):
    # db command
    table = 'services'
    select_params = {'services.id': 'id', 'services.name': 'name', 'services.duration': 'duration',
                     'services.price': 'price', 'services.description': 'description',
                     'services.max_attendees': 'max_attendees'}
    join_tables = ['fitness_centers']
    join_params = {'fitness_center_id': 'id'}
    where_cond = {'fitness_center_id': fc_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_services = db.fetch(query)
    return fc_services


def get_fitness_center_service_from_db(fc_id, serv_id):
    # db command
    table = 'services'
    select_params = {'services.id': 'id', 'services.name': 'name', 'services.description': 'description',
                     'services.duration': 'duration', 'services.price': 'price',
                     'services.max_attendees': 'max_attendees', 'services.fitness_center_id': 'fc_id'}
    join_tables = ['fitness_centers']
    join_params = {'fitness_center_id': 'id'}
    where_cond = {'fitness_center_id': fc_id, 'services.id': serv_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_service = db.fetch(query, False)
    return fc_service


def add_fitness_center_service_to_db(service):
    if service is None:
        return False
    query = qg.get_insert_sql_query('services', {'name': service.name, 'duration': service.duration,
                                                 'price': service.price, 'description': service.description,
                                                 'max_attendees': service.max_attendees,
                                                 'fitness_center_id': service.fitness_center_id})
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


def modify_fitness_center_service_in_db(fc_id, serv_id):
    # db command
    return True


def delete_fitness_center_service_from_db(fc_id, serv_id):
    table = 'services'
    where_params = {'id': serv_id, 'fitness_center_id': fc_id}
    query = qg.get_delete_sql_query(table, where_params)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


def get_fitness_center_trainers_from_db(fc_id):
    # db command
    table = 'trainers'
    select_params = {'trainers.id': 'id', 'trainers.name': 'name', 'trainers.age': 'age', 'trainers.gender': 'gender',
                     'trainers.capacity': 'capacity', 'trainers.fitness_center_id': 'fc_id',
                     'trainers.service_id': 'service_id'}
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
    select_params = {'trainers.id': 'id', 'trainers.name': 'name', 'trainers.age': 'age',
                     'trainers.gender': 'gender', 'trainers.fitness_center_id': 'fc_id',
                     'trainers.service_id': 'service_id'}
    join_tables = ['fitness_centers']
    join_params = {'fitness_center_id': 'id'}
    where_cond = {'fitness_center_id': fc_id, 'trainers.id': trainer_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_trainer = db.fetch(query, False)
    return fc_trainer


def add_fitness_center_trainer_to_db(trainer):
    # db command
    return True


def modify_fitness_center_trainer_in_db(fc_id, trainer_id):
    # db command
    return True


def delete_fitness_center_trainer_from_db(fc_id, trainer_id):
    table = 'trainers'
    where_params = {'id': trainer_id, 'fitness_center_id': fc_id}
    query = qg.get_delete_sql_query(table, where_params)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


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


def add_fitness_center_trainer_rating(review):
    if review is None:
        return False

    query = qg.get_insert_sql_query('reviews', {'date': review.date, 'grade': review.grade,
                                                'comment': review.comment, 'client_id': review.client_id,
                                                'trainer_id': review.trainer_id})
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        result = db.save(query)
    return result


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
    select_params = {'trainers.id': 'id', 'trainers.name': 'name', 'trainers.age': 'age',
                     'trainers.gender': 'gender', 'trainers.fitness_center_id': 'fc_id',
                     'trainers.service_id': 'service_id'}

    join_tables = ['services', 'fitness_centers']
    join_params = {'service_id': 'id', 'fitness_center_id': 'id'}
    where_cond = {'fitness_centers.id': fc_id, 'services.id': serv_id, 'trainers.id': trainer_id}
    query = qg.get_select_sql_join_query(table, select_params, join_tables, join_params, where_cond)
    print(query)
    with SQLLiteDatabase('fitnessdb.db') as db:
        fc_serv_trainer = db.fetch(query, False)
    return fc_serv_trainer


def modify_fitness_center_service_trainer_in_db(fc_id, serv_id, trainer_id):
    return True


def delete_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id):
    return True










