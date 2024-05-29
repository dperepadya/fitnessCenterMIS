from flask import Blueprint, jsonify, request, session
from fitness_center import handlers
from models.fitness_center import FitnessCenter
from models.service import Service
from models.trainer import Trainer

fitness_center_bp = Blueprint('fitness_center', __name__)


@fitness_center_bp.get('/')
def get_fitness_centers_list():
    user = session.get('user')  # User is defined after Login
    if user is not None:
        fc_list = handlers.get_fitness_centers_from_db(user['id'])
        if fc_list is not None :
            return jsonify(user['id'], fc_list), 200
        else:
            return jsonify({'message': 'Fitness centers list is empty'}), 404
    else:
        return jsonify({'message': 'User not logged in'}), 401



@fitness_center_bp.post('/')
def add_fitness_center():
    fc_data = request.json
    fc = FitnessCenter.empty()
    return handlers.add_fitness_center_to_db(fc)


@fitness_center_bp.put('/<fc_id>')
def edit_fitness_center():
    fc_data = request.json
    fc = FitnessCenter.empty()
    return handlers.modify_fitness_center_in_db(fc)


@fitness_center_bp.get('/<fc_id>')
def get_fitness_center_info(fc_id):
    fc = handlers.get_fitness_center_from_db(fc_id)
    if fc:
        return jsonify(fc)
    else:
        return jsonify({'message': 'Fitness center not found'}), 404


@fitness_center_bp.get('/<fc_id>/bonuses')
def get_fitness_center_bonuses():
    bonuses = handlers.get_fitness_center_bonuses_from_db()
    if bonuses:
        return jsonify(bonuses)
    else:
        return jsonify({'message': 'There is no info about bonuses'}), 404


@fitness_center_bp.get('/<fc_id>/services')
def get_fitness_center_services():
    fc = handlers.get_fitness_center_services_from_db()
    if fc:
        return jsonify(fc)
    else:
        return jsonify({'message': 'Fitness center service not found'}), 404


@fitness_center_bp.post('/<fc_id>/services')
def add_fitness_center_service():
    serv_data = request.json
    serv = Service.empty()
    return handlers.add_fitness_center_service_to_db(serv)


@fitness_center_bp.get('/<fc_id>/services/<serv_id>')
def get_fitness_center_service_info(fc_id, serv_id):
    fc = handlers.get_fitness_center_service_from_db(fc_id, serv_id)
    if fc:
        return jsonify(fc)
    else:
        return jsonify({'message': 'Fitness center services list is empty'}), 404


@fitness_center_bp.put('/<fc_id>/services/<serv_id>')
def edit_fitness_center_service():
    serv_data = request.json
    serv = Service.empty()
    return handlers.modify_fitness_center_service_in_db(serv)


@fitness_center_bp.delete('/<fc_id>/services/<serv_id>')
def delete_fitness_center_service(fc_id, serv_id):
    return handlers.delete_fitness_center_service_from_db(fc_id, serv_id)


@fitness_center_bp.get('/<fc_id>/trainers')
def get_fitness_center_trainers(fc_id):
    fc = handlers.get_fitness_center_trainers_from_db(fc_id)
    if fc:
        return jsonify(fc)
    else:
        return jsonify({'message': 'Fitness center trainer not found'}), 404


@fitness_center_bp.post('/<fc_id>/trainers')
def get_fitness_center_trainer():
    trainer_data = request.json
    trainer = Trainer.empty()
    return handlers.add_fitness_center_trainer_to_db(trainer)


@fitness_center_bp.get('/<fc_id>/trainers/<trainer_id>')
def get_fitness_center_trainer_info(fc_id, trainer_id):
    fc = handlers.get_fitness_center_trainer_from_db(fc_id, trainer_id)
    if fc:
        return jsonify(fc)
    else:
        return jsonify({'message': 'Fitness center trainers list is empty'}), 404


@fitness_center_bp.put('/<fc_id>/trainers/<trainer_id>')
def edit_fitness_center_trainer():
    trainer_data = request.json
    trainer = Trainer.empty()
    return handlers.modify_fitness_center_trainer_in_db(trainer)


@fitness_center_bp.get('/<fc_id>/trainers/<trainer_id>')
def delete_fitness_center_trainer(fc_id, trainer_id):
    return handlers.delete_fitness_center_trainer_from_db(fc_id, trainer_id)


@fitness_center_bp.get('/<fc_id>/trainers/<trainer_id>/rating')
def get_fitness_center_trainer_rating_from_db(fc_id, trainer_id):
    return handlers.get_fitness_center_trainer_rating_from_db(fc_id, trainer_id)


@fitness_center_bp.post('/<fc_id>/trainers/<trainer_id>/rating')
def set_fitness_center_trainer_rating():
    return True


@fitness_center_bp.put('/<fc_id>/trainers/<trainer_id>/schedule')
def modify_fitness_center_trainer_schedule_in_db(fc_id, trainer_id):
    return True


@fitness_center_bp.get('/<fc_id>/trainers/<trainer_id>/schedule')
def get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id):
    return handlers.get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id)


@fitness_center_bp.post('/<fc_id>/trainers/<trainer_id>/schedule')
def set_fitness_center_trainer_schedule():
    return True


@fitness_center_bp.get('/<fc_id>/services/<serv_id>/trainer')
def get_fitness_center_services_and_trainers(fc_id, serv_id):
    fc_s_t = handlers.get_fitness_center_services_and_trainers_from_db(fc_id, serv_id)
    if fc_s_t:
        return jsonify(fc_s_t)
    else:
        return jsonify({'message': 'Fitness center service-trainer pairs not found'}), 404


@fitness_center_bp.post('/<fc_id>/services/<serv_id>/trainer')
def add_trainer_to_fitness_center_service(fc_id, serv_id):
    trainer_data = request.json
    trainer = Trainer.empty()
    return handlers.add_trainer_to_fitness_center_service_in_db(fc_id, serv_id, trainer)


@fitness_center_bp.get('/<fc_id>/services/<serv_id>/trainer/<trainer_id>')
def get_fitness_center_service_trainer_pair_info(fc_id, serv_id, trainer_id):
    trainer = handlers.get_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id)
    if trainer:
        return jsonify(trainer)
    else:
        return jsonify({'message': 'Fitness center & service trainer not found'}), 404


@fitness_center_bp.put('/<fc_id>/services/<serv_id>/trainer/<trainer_id>')
def edit_fitness_center_service_trainer(fc_id, serv_id, trainer_id):
    serv_data = request.json
    trainer = handlers.modify_fitness_center_service_trainer_in_db(fc_id, serv_id, trainer_id)
    if trainer:
        return jsonify(trainer)
    else:
        return jsonify({'message': 'Fitness center & service trainer not found'}), 404


@fitness_center_bp.delete('/<fc_id>/services/<serv_id>/trainer/<trainer_id>')
def delete_trainer_from_fitness_center_service(fc_id, serv_id, trainer_id):
    return handlers.delete_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id)





