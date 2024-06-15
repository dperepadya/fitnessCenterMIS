from datetime import datetime

from flask import Blueprint, jsonify, request, session, render_template
from jupyter_server import services

from fitness_center import handlers
from models.fitness_center import FitnessCenter
from models.review import Review
from models.schedule import Schedule
from models.service import Service
from models.trainer import Trainer
from utils.converters import Converter
from utils.login_decorator import check_user_login

fitness_center_bp = Blueprint('fitness_center', __name__)


@fitness_center_bp.get('/')
@check_user_login
def get_fitness_centers_list():
    fc_list = handlers.get_fitness_centers_from_db()
    if fc_list is None:
        return jsonify({'message': 'Fitness centers list is empty'}), 404
    # print(type(fc_list))
    # fc_list_str = Converter.convert_to_string(fc_list)
    # user = session.get('user')
    # user_name = user['client_name']
    # print(user_name, fc_list_str)
    # return jsonify({'message': f"{user_name} {fc_list_str}"}), 200
    return render_template('fitness_centers_list.html', fitness_centers=fc_list)


# Add fitness center ======================================
@fitness_center_bp.get('/add')
@check_user_login
def get_add_fitness_center_form():
    return render_template('fitness_center_add.html')


@fitness_center_bp.post('/add')
@check_user_login
def add_fitness_center():
    fc_data = request.form
    fc = FitnessCenter(fc_data['name'], fc_data['address'], fc_data['phone'], fc_data['email'])
    if handlers.add_fitness_center_to_db(fc):
        return jsonify({'message': 'New Fitness Center added successfully'}), 201
    else:
        return jsonify({'message': 'Cannot add a Fitness Center'}), 404


# Edit fitness center ======================================
@fitness_center_bp.get('/<int:fc_id>/edit')
@check_user_login
def get_edit_fitness_center_form(fc_id):
    fc_info = handlers.get_fitness_center_from_db(fc_id)
    if fc_info is None:
        return jsonify({'message': 'Cannot find a fitness center'}), 404
    return render_template('fitness_center_edit.html', fc_id=fc_id)


@fitness_center_bp.post('/<int:fc_id>/edit')
@check_user_login
def edit_fitness_center(fc_id):
    fc_data = request.form
    fc = FitnessCenter(fc_data['name'], fc_data['address'], fc_data['phone'], fc_data['email'])
    if handlers.modify_fitness_center_in_db(fc):
        return jsonify({'message': 'Fitness Center updated successfully'}), 201
    else:
        return jsonify({'message': 'Cannot update the Fitness Center'}), 404


# Delete fitness center ======================================
@fitness_center_bp.get('/delete')
@check_user_login
def get_delete_fitness_center_form():
    fc_list = handlers.get_fitness_centers_from_db()
    if fc_list is None:
        return jsonify({'message': 'Fitness centers list is empty'}), 404
    return render_template('fitness_center_delete.html', fitness_centers=fc_list)


@fitness_center_bp.post('/delete')
@check_user_login
def delete_fitness_center():
    fc_data = request.form
    fc_id = fc_data['fc_id']
    if handlers.delete_fitness_center_from_db(fc_id):
        return jsonify({'message': 'Fitness Center removed successfully'}), 201
    else:
        return jsonify({'message': 'Cannot delete the Fitness Center'}), 404


# Get fitness center info ======================================

@fitness_center_bp.get('/<int:fc_id>')
@check_user_login
def get_fitness_center_info(fc_id):
    fc_info = handlers.get_fitness_center_from_db(fc_id)
    if fc_info is None:
        return jsonify({'message': 'Cannot find a fitness centers'}), 404
    # fc_str = Converter.convert_to_string(fc)
    # user = session.get('user')
    # user_name = user['client_name']
    # print(user_name, fc_list_str)
    # return jsonify({'message': f"Client: {user_name} Fitness center: id {fc_id} info: {fc_str}"}), 200
    return render_template('fitness_center_info.html', fc=fc_info)


# Get Fitness Center Services ======================================


@fitness_center_bp.get('/<int:fc_id>/services')
@check_user_login
def get_fitness_center_services(fc_id):
    fc_services = handlers.get_fitness_center_services_from_db(fc_id)
    if fc_services is None:
        return jsonify({'message': 'Fitness center services list is empty'}), 404
    # fc_services_str = Converter.convert_to_string(fc_services)
    # user = session.get('user')
    # user_name = user['client_name']
    # return jsonify({'message': f"{user_name} fitness center {fc_id} services: {fc_services_str}"}), 200
    return render_template('services_list.html', services=fc_services, fc_id=fc_id)


# Get Fitness Center Service info ======================================


@fitness_center_bp.get('/<int:fc_id>/services/<int:serv_id>')
@check_user_login
def get_fitness_center_service_info(fc_id, serv_id):
    fc_service = handlers.get_fitness_center_service_from_db(fc_id, serv_id)
    if fc_service is None:
        return jsonify({'message': 'Fitness center service not found'}), 404
    # fc_service_str = Converter.convert_to_string(fc_service)
    # user = session.get('user')
    # user_name = user['client_name']
    # return jsonify({'message': f"{user_name} fitness center {fc_id} service {serv_id}: {fc_service_str}"}), 200
    return render_template('service_info.html', service=fc_service)

# Add Fitness Center Services ======================================


@fitness_center_bp.get('/<int:fc_id>/services/add')
@check_user_login
def get_add_fitness_center_service_form(fc_id):
    return render_template('service_add.html', fc_id=fc_id)


@fitness_center_bp.post('/<int:fc_id>/services/add')
@check_user_login
def add_fitness_center_service(fc_id):
    serv_data = request.form
    serv = Service(serv_data['name'], serv_data['description'], serv_data['duration'], serv_data['price'],
                   serv_data['max_attendees'])
    serv.fitness_center_id = fc_id
    if handlers.add_fitness_center_service_to_db(serv):
        return jsonify({'message': 'Fitness Center Service added successfully'}), 201
    else:
        return jsonify({'message': 'Cannot add the Fitness Center Service'}), 404

# Delete a Fitness Center Service ======================================


@fitness_center_bp.get('/<int:fc_id>/services/delete')
@check_user_login
def get_delete_fitness_center_service_form(fc_id):
    fc_services = handlers.get_fitness_center_services_from_db(fc_id)
    if fc_services is None:
        return jsonify({'message': 'Fitness center Services list is empty'}), 404
    return render_template('service_delete.html', services=fc_services, fc_id=fc_id)


@fitness_center_bp.post('/<int:fc_id>/services/delete')
@check_user_login
def delete_fitness_center_service(fc_id):
    fc_services = request.form
    serv_id = fc_services['service_id']
    if handlers.delete_fitness_center_service_from_db(fc_id, serv_id):
        return jsonify({'message': 'Fitness Center Service removed successfully'}), 201
    else:
        return jsonify({'message': 'Cannot remove the Fitness Center Service'}), 404

# Get Fitness Center Trainers ======================================


@fitness_center_bp.get('/<int:fc_id>/trainers')
@check_user_login
def get_fitness_center_trainers(fc_id):
    fc_trainers = handlers.get_fitness_center_trainers_from_db(fc_id)
    if fc_trainers is None:
        return jsonify({'message': 'Fitness center trainers list is empty'}), 404
    # fc_trainers_str = Converter.convert_to_string(fc_trainers)
    # user = session.get('user')
    # user_name = user['client_name']
    # return jsonify({'message': f"{user_name} fitness center {fc_id} trainers: {fc_trainers_str}"}), 200
    return render_template('trainers_list.html', trainers=fc_trainers, fc_id=fc_id)


# Get Fitness Center Service Trainer ======================================

@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>')
@check_user_login
def get_fitness_center_trainer_info(fc_id, trainer_id):
    fc_trainer = handlers.get_fitness_center_trainer_from_db(fc_id, trainer_id)
    if fc_trainer is None:
        return jsonify({'message': 'Fitness center trainer not found'}), 404
    # fc_trainer_str = Converter.convert_to_string(fc_trainer)
    # user = session.get('user')
    # user_name = user['client_name']
    # return jsonify({'message': f"{user_name} fitness center {fc_id} trainer {trainer_id}:"
    #                            f" {fc_trainer_str}"}), 200
    return render_template('trainer_info.html', trainer=fc_trainer)


# Add Fitness Center Trainers ======================================


@fitness_center_bp.get('/<int:fc_id>/trainers/add')
@check_user_login
def get_add_fitness_center_trainer_form(fc_id):
    return render_template('trainer_add.html', fc_id=fc_id)


@fitness_center_bp.post('/<int:fc_id>/trainers/add')
@check_user_login
def add_fitness_center_trainer(fc_id):
    trainer_data = request.form
    trainer = Trainer(trainer_data['name'], trainer_data['age'], trainer_data['gender'])
    trainer.fitness_center_id = fc_id
    if handlers.add_fitness_center_trainer_to_db(trainer):
        return jsonify({'message': 'Fitness Center Trainer added successfully'}), 201
    else:
        return jsonify({'message': 'Cannot add the Fitness Center Trainer'}), 404

# Delete a Fitness Center Trainer ======================================


@fitness_center_bp.get('/<int:fc_id>/trainers/delete')
@check_user_login
def get_delete_fitness_center_trainer_form(fc_id):
    fc_trainers = handlers.get_fitness_center_trainers_from_db(fc_id)
    if fc_trainers is None:
        return jsonify({'message': 'Fitness center Trainers list is empty'}), 404
    return render_template('trainer_delete.html', trainers=fc_trainers, fc_id=fc_id)


@fitness_center_bp.post('/<int:fc_id>/trainers/delete')
@check_user_login
def delete_fitness_center_trainer(fc_id):
    fc_trainers = request.form
    trainer_id = fc_trainers['trainer_id']
    if handlers.delete_fitness_center_trainer_from_db(fc_id, trainer_id):
        return jsonify({'message': 'Fitness Center Trainer removed successfully'}), 201
    else:
        return jsonify({'message': 'Cannot remove the Fitness Center Trainer'}), 404


# Get Fitness Center Service Trainers ======================================


@fitness_center_bp.get('/<int:fc_id>/services/<int:serv_id>/trainers')
@check_user_login
def get_fitness_center_service_trainers(fc_id, serv_id):
    fc_trainers = handlers.get_fitness_center_service_trainers_from_db(fc_id, serv_id)
    if fc_trainers is None:
        return jsonify({'message': 'Fitness center trainers list is empty'}), 404
    # fc_trainers_str = Converter.convert_to_string(fc_trainers)
    # user = session.get('user')
    # user_name = user['client_name']
    # return jsonify({'message': f"{user_name} fitness center {fc_id} trainers: {fc_trainers_str}"}), 200
    return render_template('service_trainers_list.html', trainers=fc_trainers, fc_id=fc_id,
                           serv_id=serv_id)


# Get Fitness Center Trainer Services ======================================


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/services')
@check_user_login
def get_fitness_center_trainer_services(fc_id, trainer_id):
    fc_trainers = handlers.get_fitness_center_trainer_services_from_db(fc_id, trainer_id)
    if fc_trainers is None:
        return jsonify({'message': 'Fitness center trainers list is empty'}), 404
    # fc_trainers_str = Converter.convert_to_string(fc_trainers)
    # user = session.get('user')
    # user_name = user['client_name']
    # return jsonify({'message': f"{user_name} fitness center {fc_id} trainers: {fc_trainers_str}"}), 200
    return render_template('trainer_services_list.html', trainers=fc_trainers, fc_id=fc_id,
                           trainer_id=trainer_id)

# Assign Fitness Center Service to Trainer ======================================


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/services/add')
@check_user_login
def get_add_fitness_center_trainer_service_form(fc_id, trainer_id):
    return render_template('trainer_service_assign.html', fc_id=fc_id, trainer_id=trainer_id)


@fitness_center_bp.post('/<int:fc_id>/trainers/<int:trainer_id>/services/add')
@check_user_login
def add_fitness_center_service_trainer(fc_id, trainer_id):
    service_data = request.form
    service_id = service_data['service_id']
    capacity = service_data['capacity']
    if handlers.add_fitness_center_trainer_and_service_to_db(trainer_id, service_id, capacity):
        return jsonify({'message': 'Fitness Center Service assigned successfully'}), 201
    else:
        return jsonify({'message': 'Cannot assign the Service to the Trainer'}), 404


# Trainer rating #############################################


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/rating')
@check_user_login
def get_fitness_center_trainer_rating_from_db(fc_id, trainer_id):
    fc_trainer_reviews = handlers.get_fitness_center_trainer_rating_from_db(fc_id, trainer_id)
    if fc_trainer_reviews is None:
        return jsonify({'message': 'Fitness center trainer rating not found'}), 404
    # fc_trainer_reviews_str = Converter.convert_to_string(fc_trainer_reviews)
    # user = session.get('user')
    # user_name = user['client_name']
    # return jsonify({'message': f"{user_name} fitness center {fc_id} trainer {trainer_id}:"
    #                            f" reviews {fc_trainer_reviews_str}"}), 200
    return render_template('trainer_reviews.html', reviews=fc_trainer_reviews,
                           fc_id=fc_id, trainer_id=trainer_id)


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/rating/add')
@check_user_login
def get_fitness_center_trainer_rating_form(fc_id, trainer_id):
    user = session.get('user')  # User is defined after Login
    user_id = user['id']
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


# Schedule


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/schedule')
@check_user_login
def get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id):
    fc_trainer_schedule = handlers.get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id)
    if fc_trainer_schedule is None:
        return jsonify({'message': 'Fitness center trainer schedule not found'}), 404
    # schedule = [dict(row) for row in fc_trainer_schedule]
    # fc_trainer_schedule_str = Converter.convert_to_string(fc_trainer_schedule)
    # user = session.get('user')
    # user_name = user['client_name']
    # return jsonify({'message': f"{user_name} fitness center {fc_id} trainer {trainer_id}:"
    #                           f" schedule {fc_trainer_schedule_str}"}), 200
    return render_template('trainer_schedule_info.html', schedule=fc_trainer_schedule,
                           fc_id=fc_id, trainer_id=trainer_id)


@fitness_center_bp.post('/<int:fc_id>/trainers/<int:trainer_id>/schedule/add')
@check_user_login
def get_add_fitness_center_trainer_schedule_form(fc_id, trainer_id):
    return render_template('schedule_add.html', fc_id=fc_id, trainer_id=trainer_id)


@fitness_center_bp.post('/<int:fc_id>/trainers/<int:trainer_id>/schedule/add')
@check_user_login
def add_fitness_center_trainer_schedule(fc_id, trainer_id):
    schedule_data = request.form
    date = schedule_data['date']
    start_time = schedule_data['start_time']
    end_time = schedule_data['end_time']
    schedule = Schedule(date, start_time, end_time, trainer_id)
    result = handlers.add_fitness_center_trainer_schedule(schedule)
    if result is not None:
        return jsonify({'message': f"Schedule for trainer {trainer_id}"
                                   f" added successfully"}), 201
    else:
        return jsonify({'message': f"Cannot add trainer  {trainer_id} schedule"}), 400


@fitness_center_bp.get('/<int:fc_id>/trainers/<int:trainer_id>/schedule/delete')
@check_user_login
def get_delete_fitness_center_trainer_schedule_form(fc_id, trainer_id):
    fc_trainer_schedule = handlers.get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id)
    if fc_trainer_schedule is None:
        return jsonify({'message': 'Fitness center Trainers list is empty'}), 404
    return render_template('schedule_delete.html', schedule=fc_trainer_schedule, fc_id=fc_id,
                           trainer_id=trainer_id)


@fitness_center_bp.post('/<int:fc_id>/trainers/<int:trainer_id>/schedule/delete')
@check_user_login
def delete_fitness_center_trainer_schedule(fc_id, trainer_id):
    fc_trainer_schedule = request.form
    trainer_id = fc_trainer_schedule['trainer_id']
    schedule_id = fc_trainer_schedule['schedule_id']
    if handlers.delete_fitness_center_trainer_schedule_from_db(trainer_id, schedule_id):
        return jsonify({'message': 'Fitness Center Trainer Schedule removed successfully'}), 201
    else:
        return jsonify({'message': 'Cannot remove the Fitness Center Trainer Schedule'}), 404



# ======================================


@fitness_center_bp.get('/<int:fc_id>/bonuses')
@check_user_login
def get_fitness_center_bonuses():
    bonuses = handlers.get_fitness_center_bonuses_from_db()
    if bonuses:
        return jsonify(bonuses)
    else:
        return jsonify({'message': 'There is no info about bonuses'}), 404



