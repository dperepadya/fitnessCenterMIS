from flask import g

from db_models.client import Client
from db_models.order import Order
from db_models.trainer_services import TrainerService
from mappers.order_mappers import order_to_orderdb
from mappers.user_mappers import user_to_userdb


def get_user_from_db(user_id):
    user = g.db.query(Client).filter(Client.id == user_id).first()
    if user:
        return user
    else:
        return None


def update_user_in_db(user):
    if user is None:
        return False
    try:
        db_user = g.db.query(Client).filter(Client.id == user.id).first()
        if db_user is None:
            return False
        db_user = user_to_userdb(user)
        if db_user is None:
            return False
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error inserting user: {e}")
        return False


def update_user_funds_in_db(user_id, funds):
    if funds == 0:
        return True
    try:
        db_user = g.db.query(Client).filter(Client.id == user_id).first()
        if db_user is None:
            return False
        db_user.funds += funds
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error updating user funds: {e}")
        return False


def add_user_order_to_db(order):
    if order is None:
        return False

    try:
        order = order_to_orderdb(order)
        g.db.add(order)
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error adding order: {e}")
        return False


def get_trainer_services_list():
    try:
        trainer_services = g.db.query(TrainerService).all()
        return trainer_services
    except Exception as e:
        print(f"Error fetching trainer services list: {e}")
        return None


def get_trainer_service(trainer_service_id):
    try:
        trainer_service = g.db.query(TrainerService).filter(TrainerService.id == trainer_service_id).first()
        return trainer_service
    except Exception as e:
        print(f"Error fetching trainer service with id {trainer_service_id}: {e}")
        return None

