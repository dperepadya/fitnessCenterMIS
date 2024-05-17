from models.fitness_center import FitnessCenter
from models.service import Service


def get_fitness_centers_from_db():
    # db command
    fc_list = None
    return fc_list


def get_fitness_center_from_db(fc_id):
    # db command
    fc = FitnessCenter.empty()  # 'Olymp', 'EastWay av. 12/25', 'olymp@fitnesskyiv.com')
    return fc


def get_fitness_center_services_from_db(fc_id):
    # db command
    fc_services_list = {}
    return fc_services_list


def get_fitness_center_service_from_db(fc_id, service_id):
    # db command
    fc_service = Service.empty()
    return fc_service


def get_fitness_center_trainers_from_db(fc_id):
    # db command
    fc_trainers_list = {}
    return fc_trainers_list


def get_fitness_center_trainer_from_db(fc_id, trainer_id):
    # db command
    fc_service = Trainer.empty()
    return fc_service





