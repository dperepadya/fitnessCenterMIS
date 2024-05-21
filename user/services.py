from flask import jsonify

from models.order import Order
from models.user import User


def get_user_from_db(user_id):
    # db command
    user = None
    if user:
        return user
    else:
        return None


def update_user_in_db(user):
    if user:
        # db command
        return True
    return False


def get_user_cart_from_db(user):
    # db command
    cart = None
    return cart


def get_user_cart_item_from_db(user, item_id):
    item = None
    return item


def delete_user_cart_item_from_db(user, item_id):
    # db command
    return True


def edit_user_cart_item_in_db(user, item_id):
    # db command
    return True


def add_user_order_to_db(user):
    return True


def get_user_orders_from_db(user):
    orders = {}
    return orders


def get_user_order_from_db(user, ord_id):
    orders = Order.empty()
    return orders


def edit_user_order_in_db(user):
    return True


def delete_user_order_from_db(user, ord_id):
    return True




