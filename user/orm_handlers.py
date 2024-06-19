from datetime import datetime, timedelta

from flask import g
from sqlalchemy import and_
from sqlalchemy.orm import joinedload

from database.database import db_session
from db_models.client import Client
from db_models.order import Order
from db_models.schedule import Schedule
from db_models.trainer_services import TrainerService
from mappers.order_mappers import order_to_orderdb
from mappers.user_mappers import user_to_userdb, existing_user_to_userdb
from user.handlers import get_available_time_slots as get_time_slots


def get_user_from_db(user_id):
    user = db_session.query(Client).filter(Client.id == user_id).first()
    if user:
        return user
    else:
        return None


def update_user_in_db(user):
    if user is None:
        return False
    try:
        db_user = db_session.query(Client).filter(Client.id == user.id).first()
        if db_user is None:
            return False
        existing_user_to_userdb(db_user, user)
        if db_user is None:
            return False
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        print(f"Error inserting user: {e}")
        return False


def update_user_funds_in_db(user_id, funds):
    if funds == 0:
        return True
    try:
        db_user = db_session.query(Client).filter(Client.id == user_id).first()
        if db_user is None:
            return False
        db_user.funds += funds
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        print(f"Error updating user funds: {e}")
        return False


def add_user_order_to_db(order):
    if order is None:
        return False
    try:
        order = order_to_orderdb(order)
        db_session.add(order)
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        print(f"Error adding order: {e}")
        return False


def get_trainer_services_list():
    try:
        trainer_services = db_session.query(TrainerService).all()
        return trainer_services
    except Exception as e:
        print(f"Error fetching trainer services list: {e}")
        return None


def get_trainer_service(trainer_service_id):
    try:
        trainer_service = (db_session.query(TrainerService)
                           .filter(TrainerService.id == trainer_service_id)
                           .first())
        return trainer_service
    except Exception as e:
        print(f"Error fetching trainer service with id {trainer_service_id}: {e}")
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


def get_orders_from_db(client_id, service_id, trainer_id, date):
    try:
        orders = db_session.query(Order).filter(
            Order.client_id == client_id,
            Order.service_id == service_id,
            Order.trainer_id == trainer_id,
            Order.date == date
        ).all()
        return orders
    except Exception as e:
        print(f"Error fetching orders: {e}")
        return None


def get_available_time_slots(client_id, trainer_service_id, date):
    return get_time_slots(client_id, trainer_service_id, date)


def get_user_orders_from_db(user_id):
    try:
        orders = db_session.query(Order).options(
            joinedload(Order.service),
            joinedload(Order.trainer)
        ).filter(Order.client_id == user_id).all()

        if orders is None or len(orders) == 0:
            return None

        results = []
        for order in orders:
            results.append({
                'order_id': order.id,
                'service_name': order.service.name,
                'trainer_name': order.trainer.name,
                'service_id': order.service_id,
                'trainer_id': order.trainer_id,
                'date': order.date,
                'time': order.time
            })

        return results

    except Exception as e:
        print(f"Error fetching user orders: {e}")
        return None


def get_user_order_from_db(user_id, ord_id):
    try:
        order = db_session.query(Order).options(
            joinedload(Order.service),
            joinedload(Order.trainer)
        ).filter(
            and_(
                Order.client_id == user_id,
                Order.id == ord_id
            )
        ).first()

        if order is None:
            return None
        result = {
            'order_id': order.id,
            'service_name': order.service.name,
            'trainer_name': order.trainer.name,
            'service_id': order.service_id,
            'trainer_id': order.trainer_id,
            'date': order.date,
            'time': order.time
        }
        return result

    except Exception as e:
        print(f"Error fetching user order: {e}")
        return None


def delete_user_order_from_db(ord_id):
    try:
        order = db_session.query(Order).filter(Order.id == ord_id).first()
        if order is None:
            return False
        db_session.delete(order)
        db_session.commit()
        return True

    except Exception as e:
        db_session.rollback()
        print(f"Error deleting order: {e}")
        return False
