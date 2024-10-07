from datetime import timedelta, datetime, time

from database.database import db_session
from db_models.schedule import Schedule
from db_models.trainer_service import TrainerService
from user.orm_handlers import get_orders_from_db


def get_available_time_slots(client_id, trainer_id, service_id, date, step=15):
    trainer_service = get_trainer_service(trainer_id, service_id)
    if trainer_service is None:
        return None
    # trainer_id = trainer_service['trainer_id']
    # service_id = trainer_service['service_id']
    capacity = int(trainer_service.capacity)
    # Get trainer schedule
    schedule = get_trainer_schedule(trainer_id, date)
    if schedule is None:
        return None
    # date_start_time = datetime.strptime(schedule.start_time_str, '%H:%M').time()
    # date_end_time = datetime.strptime(schedule.end_time, '%H:%M').time()
    date_start_time = schedule.start_time
    date_end_time = schedule.end_time
    # Get booked slots on the date
    orders = get_orders_from_db(client_id, service_id, trainer_id, date)
    if orders is None:
        return None
    # booked_slots = [datetime.strptime(order.time, '%H:%M') for order in orders]
    booked_slots = [order.time for order in orders]
    slots = []
    current_time = date_start_time
    # while current_time < date_end_time - timedelta(minutes=capacity):
    while add_minutes_to_time(current_time, capacity) <= date_end_time:
        # slot_end_time = current_time + timedelta(minutes=capacity)
        slot_end_time = add_minutes_to_time(current_time, capacity)
        overlap = False
        for booked_time in booked_slots:
            # booked_end_time = booked_time + timedelta(minutes=capacity)
            booked_end_time = add_minutes_to_time(booked_time, capacity)
            if max(current_time, booked_time) < min(slot_end_time, booked_end_time):
                overlap = True
                break
        if not overlap:
            # time = current_time.strftime("%H:%M:%S") + f".{current_time.microsecond:06d}"
            slots.append(current_time)

        current_time = add_minutes_to_time(current_time, step)
    return slots


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
                           .filter(TrainerService.trainer_id == trainer_id,
                                   TrainerService.service_id == service_id)
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


def add_minutes_to_time(t, minutes):
    # Convert time to total minutes since midnight
    total_minutes = t.hour * 60 + t.minute + minutes

    # Calculate new hours and minutes
    new_hour = total_minutes // 60
    new_minute = total_minutes % 60

    # Return new time object
    return time(new_hour, new_minute)
