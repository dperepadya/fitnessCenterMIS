from datetime import timedelta, datetime

from database.database import db_session
from db_models.schedule import Schedule
from db_models.trainer_services import TrainerService
from user.orm_handlers import get_orders_from_db


def get_time_slots(client_id, trainer_id, service_id, date):
    trainer_service = get_trainer_service(trainer_id, service_id)
    if trainer_service is None:
        return None
    # trainer_id = trainer_service['trainer_id']
    # service_id = trainer_service['service_id']
    capacity = trainer_service['capacity']
    # Get trainer schedule
    schedule = get_trainer_schedule(trainer_id, date)
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


def get_available_time_slots(client_id, trainer_id, service_id, date):
    return get_time_slots(client_id, trainer_id, service_id, date)


def get_trainer_services_list():
    try:
        trainer_services = db_session.query(TrainerService).all()
        return trainer_services
    except Exception as e:
        print(f"Error fetching trainer services list: {e}")
        return None


def get_trainer_service(trainer_id, service_id):
    try:
        trainer_service = (db_session.query(TrainerService)
                           .filter(trainer_id == trainer_id,
                                   service_id == service_id)
                           .first())
        return trainer_service
    except Exception as e:
        print(f"Error fetching trainer service with ids {service_id} {trainer_id}: {e}")
        return None


def get_trainer_schedule(trainer_id, date):
    try:
        schedule = (db_session.query(Schedule)
                    .filter(Schedule.trainer_id == trainer_id, Schedule.date == date)
                    .first())
        return schedule
    except Exception as e:
        print(f"Error fetching schedule: {e}")
        return None
