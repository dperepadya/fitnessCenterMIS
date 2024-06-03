from datetime import datetime

from flask import Blueprint, jsonify, request, session, render_template
from fitness_center import handlers
from models.fitness_center import FitnessCenter
from models.review import Review
from models.service import Service
from models.trainer import Trainer
from utils.converters import Converter
from utils.login_decorator import check_user_login

fitness_center_bp = Blueprint('fitness_center', __name__)


@fitness_center_bp.get('/')
@check_user_login
def get_fitness_centers_list():
    fc_list = handlers.get_fitness_centers_from_db()
    if fc_list is not None:
        # print(type(fc_list))
        fc_list_str = Converter.convert_to_string(fc_list)
        user = session.get('user')
        user_name = user['client_name']
        # print(user_name, fc_list_str)
        return jsonify({'message': f"{user_name} {fc_list_str}"}), 200
    else:
        return jsonify({'message': 'Fitness centers list is empty'}), 404


@fitness_center_bp.post('/')
@check_user_login
def add_fitness_center():
    fc_data = request.json
    fc = FitnessCenter.empty()
    return handlers.add_fitness_center_to_db(fc)


@fitness_center_bp.put('/<int:fc_id>')
@check_user_login
def edit_fitness_center():
    fc_data = request.json
    fc = FitnessCenter.empty()
    return handlers.modify_fitness_center_in_db(fc)


@fitness_center_bp.get('/<int:fc_id>')
@check_user_login
def get_fitness_center_info(fc_id):
    fc = handlers.get_fitness_center_from_db(fc_id)
    if fc is not None:
        # print(type(fc_list))
        fc_str = Converter.convert_to_string(fc)
        user = session.get('user')
        user_name = user['client_name']
        # print(user_name, fc_list_str)
        return jsonify({'message': f"Client: {user_name} Fitness center: id {fc_id} info: {fc_str}"}), 200
    else:
        return jsonify({'message': 'Fitness centers list is empty'}), 404


@fitness_center_bp.get('/<int:fc_id>/bonuses')
@check_user_login
def get_fitness_center_bonuses():
    bonuses = handlers.get_fitness_center_bonuses_from_db()
    if bonuses:
        return jsonify(bonuses)
    else:
        return jsonify({'message': 'There is no info about bonuses'}), 404


@fitness_center_bp.get('/<int:fc_id>/services')
@check_user_login
def get_fitness_center_services(fc_id):
    fc_services = handlers.get_fitness_center_services_from_db(fc_id)
    if fc_services is not None:
        fc_services_str = Converter.convert_to_string(fc_services)
        user = session.get('user')
        user_name = user['client_name']
        return jsonify({'message': f"{user_name} fitness center {fc_id} services: {fc_services_str}"}), 200
    else:
        return jsonify({'message': 'Fitness center services list is empty'}), 404


@fitness_center_bp.post('/<int:fc_id>/services')
@check_user_login
def add_fitness_center_service(fc_id):
    serv_data = request.json
    serv = Service.empty()
    return handlers.add_fitness_center_service_to_db(serv)


@fitness_center_bp.get('/<int:fc_id>/services/<int:serv_id>')
@check_user_login
def get_fitness_center_service_info(fc_id, serv_id):
    fc_service = handlers.get_fitness_center_service_from_db(fc_id, serv_id)
    if fc_service is not None:
        fc_service_str = Converter.convert_to_string(fc_service)
        user = session.get('user')
        user_name = user['client_name']
        return jsonify({'message': f"{user_name} fitness center {fc_id} service {serv_id}: {fc_service_str}"}), 200
    else:
        return jsonify({'message': 'Fitness center service not found'}), 404


@fitness_center_bp.put('/<int:fc_id>/services/<int:serv_id>')
@check_user_login
def edit_fitness_center_service():
    serv_data = request.json
    serv = Service.empty()
    return handlers.modify_fitness_center_service_in_db(serv)


@fitness_center_bp.delete('/<int:fc_id>/services/<int:serv_id>')
@check_user_login
def delete_fitness_center_service(fc_id, serv_id):
    return handlers.delete_fitness_center_service_from_db(fc_id, serv_id)


@fitness_center_bp.get('/<int:fc_id>/trainers')
@check_user_login
def get_fitness_center_trainers(fc_id):
    fc_trainers = handlers.get_fitness_center_trainers_from_db(fc_id)
    if fc_trainers is not None:
        fc_trainers_str = Converter.convert_to_string(fc_trainers)
        user = session.get('user')
        user_name = user['client_name']
        return jsonify({'message': f"{user_name} fitness center {fc_id} trainers: {fc_trainers_str}"}), 200
    else:
        return jsonify({'message': 'Fitness center trainers list is empty'}), 404


@fitness_center_bp.post('/<int:fc_id>/trainers')
@check_user_login
def add_fitness_center_trainer():
    trainer_data = request.json
    trainer = Trainer.empty()
    return handlers.add_fitness_center_trainer_to_db(trainer)


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>')
@check_user_login
def get_fitness_center_trainer_info(fc_id, trainer_id):
    fc_trainer = handlers.get_fitness_center_trainer_from_db(fc_id, trainer_id)
    if fc_trainer is not None:
        fc_trainer_str = Converter.convert_to_string(fc_trainer)
        user = session.get('user')
        user_name = user['client_name']
        return jsonify({'message': f"{user_name} fitness center {fc_id} trainer {trainer_id}:"
                                   f" {fc_trainer_str}"}), 200
    else:
        return jsonify({'message': 'Fitness center trainer not found'}), 404


@fitness_center_bp.put('/<int:fc_id>/trainers/<int:trainer_id>')
@check_user_login
def edit_fitness_center_trainer():
    trainer_data = request.json
    trainer = Trainer.empty()
    return handlers.modify_fitness_center_trainer_in_db(trainer)


@fitness_center_bp.delete('/<int:fc_id>/trainers/<int:trainer_id>')
@check_user_login
def delete_fitness_center_trainer(fc_id, trainer_id):
    return handlers.delete_fitness_center_trainer_from_db(fc_id, trainer_id)


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/rating')
@check_user_login
def get_fitness_center_trainer_rating_from_db(fc_id, trainer_id):
    fc_trainer_reviews = handlers.get_fitness_center_trainer_rating_from_db(fc_id, trainer_id)
    if fc_trainer_reviews is not None:
        fc_trainer_reviews_str = Converter.convert_to_string(fc_trainer_reviews)
        user = session.get('user')
        user_name = user['client_name']
        return jsonify({'message': f"{user_name} fitness center {fc_id} trainer {trainer_id}:"
                                   f" reviews {fc_trainer_reviews_str}"}), 200
    else:
        return jsonify({'message': 'Fitness center trainer rating not found'}), 404


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/rating/add')
@check_user_login
def get_fitness_center_trainer_rating_form(fc_id, trainer_id):
    user = session.get('user')  # User is defined after Login
    user_id = user['client_id']
    return render_template('trainer_review_add.html', user_id=user_id,
                           trainer_id=trainer_id, fc_id=fc_id)


@fitness_center_bp.post('/<int:fc_id>/trainers/<int:trainer_id>/rating/add')
def add_fitness_center_trainer_rating(fc_id, trainer_id):
    review_data = request.form
    user_id = review_data['user_id']
    # trainer_id = review_data['trainer_id']
    date = review_data['date']
    if date is not None:
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%d.%m.%Y')
    review = Review(review_data['date'], review_data['grade'], review_data['comment'],
                    user_id, trainer_id)
    result = handlers.add_fitness_center_trainer_rating(review)
    if result is not None:
        return jsonify({'message': f"User {user_id} review for trainer {trainer_id}"
                                   f" created successfully"}), 201
    else:
        return jsonify({'message': 'Cannot add this review'}), 400


@fitness_center_bp.put('/<int:fc_id>/trainers/<int:trainer_id>/schedule')
@check_user_login
def modify_fitness_center_trainer_schedule_in_db(fc_id, trainer_id):
    return True


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/schedule')
@check_user_login
def get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id):
    fc_trainer_schedule = handlers.get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id)
    if fc_trainer_schedule is not None:
        fc_trainer_schedule_str = Converter.convert_to_string(fc_trainer_schedule)
        user = session.get('user')
        user_name = user['client_name']
        return jsonify({'message': f"{user_name} fitness center {fc_id} trainer {trainer_id}:"
                                   f" schedule {fc_trainer_schedule_str}"}), 200
    else:
        return jsonify({'message': 'Fitness center trainer schedule not found'}), 404


@fitness_center_bp.post('/<int:fc_id>/trainers/<int:trainer_id>/schedule')
@check_user_login
def add_fitness_center_trainer_schedule():
    return True


@fitness_center_bp.get('/<int:fc_id>/services/<int:serv_id>/trainer')
@check_user_login
def get_fitness_center_services_and_trainers(fc_id, serv_id):
    fc_serv_trainers = handlers.get_fitness_center_services_and_trainers_from_db(fc_id, serv_id)
    if fc_serv_trainers is not None:
        fc_serv_trainers_str = Converter.convert_to_string(fc_serv_trainers)
        user = session.get('user')
        user_name = user['client_name']
        return jsonify({'message': f"{user_name} fitness center {fc_id} service {serv_id}:"
                                   f" trainers {fc_serv_trainers_str}"}), 200
    else:
        return jsonify({'message': 'Fitness center service-trainer pairs not found'}), 404


@fitness_center_bp.post('/<int:fc_id>/services/<int:serv_id>/trainers')
@check_user_login
def add_trainer_to_fitness_center_service(fc_id, serv_id):
    trainer_data = request.json
    trainer = Trainer.empty()
    return handlers.add_trainer_to_fitness_center_service_in_db(fc_id, serv_id, trainer)


@fitness_center_bp.get('/<int:fc_id>/services/<int:serv_id>/trainers/<int:trainer_id>')
@check_user_login
def get_fitness_center_service_trainer_pair_info(fc_id, serv_id, trainer_id):
    fc_serv_trainer = handlers.get_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id)
    if fc_serv_trainer is not None:
        fc_serv_trainer_str = Converter.convert_to_string(fc_serv_trainer)
        user = session.get('user')
        user_name = user['client_name']
        return jsonify({'message': f"{user_name} fitness center {fc_id} service {serv_id}:"
                                   f" trainer {fc_serv_trainer_str}"}), 200
    else:
        return jsonify({'message': 'Fitness center & service trainer not found'}), 404


@fitness_center_bp.put('/<int:fc_id>/services/<int:serv_id>/trainer/<int:trainer_id>')
@check_user_login
def edit_fitness_center_service_trainer(fc_id, serv_id, trainer_id):
    serv_data = request.json
    trainer = handlers.modify_fitness_center_service_trainer_in_db(fc_id, serv_id, trainer_id)
    if trainer:
        return jsonify(trainer)
    else:
        return jsonify({'message': 'Fitness center & service trainer not found'}), 404


@fitness_center_bp.delete('/<int:fc_id>/services/<int:serv_id>/trainer/<int:trainer_id>')
@check_user_login
def delete_trainer_from_fitness_center_service(fc_id, serv_id, trainer_id):
    return handlers.delete_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id)





