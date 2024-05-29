from databases.sqlite_utils import SQLLiteDatabase
from models.fitness_center import FitnessCenter
from models.service import Service
from models.trainer import Trainer
from utils.query_generators import QueryGenerator as qg


def get_fitness_centers_from_db(user_id):
    # db command
    with SQLLiteDatabase('fitnessdb.db') as db:
        query = qg.get_select_sql_query('fitness_centers', None, {"user.id": user_id})
        fc_list = db.fetch(query, True)
    return fc_list


def add_fitness_centers_to_db():
    # db command
    return True


def get_fitness_center_from_db(fc_id):
    # db command
    fc = FitnessCenter.empty()  # 'Olymp', 'EastWay av. 12/25', 'olymp@fitnesskyiv.com')
    return fc


def modify_fitness_center_in_db(fc_id):
    # db command
    return True


def get_fitness_center_bonuses_from_db():
    return None


def get_fitness_center_services_from_db(fc_id):
    # db command
    fc_services_list = {}
    return fc_services_list


def get_fitness_center_service_from_db(fc_id, serv_id):
    # db command
    fc_service = None
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


def get_fitness_center_trainers_from_db():
    fc_trainers_list = {}
    return fc_trainers_list


def get_fitness_center_trainer_from_db(fc_id):
    # db command
    trainer = Trainer.empty()
    return trainer


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
    return True


def set_fitness_center_trainer_rating(fc_id, trainer_id):
    return True


def modify_fitness_center_trainer_rating_in_db(fc_id, trainer_id):
    return True


def get_fitness_center_schedule_rating_from_db(fc_id, schedule_id):
    return True


def set_fitness_center_schedule_rating(fc_id, schedule_id):
    return True


def modify_fitness_center_schedule_rating_in_db(fc_id, schedule_id):
    return True


def get_fitness_center_services_and_trainers_from_db(fc_id, serv_id):
    return None


def add_trainer_to_fitness_center_service_in_db(fc_id, serv_id, trainer):
    return True


def get_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id):
    return None


def modify_fitness_center_service_trainer_in_db(fc_id, serv_id, trainer_id):
    return True


def delete_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id):
    return True










