from datetime import datetime

from flask import Blueprint, jsonify, request, session, render_template
from user import handlers as hndl
from models.user import User
from utils.converters import Converter
from utils.login_decorator import check_user_login

user_bp = Blueprint('user', __name__)


# Get user info (session)
@user_bp.get('/')
@check_user_login
def get_user():
    user = session.get('user')  # User is defined after Login
    return jsonify({'message': f"User: {user['client_name']}"}), 200


# A user can be added with /register POST command
# @user_bp.get('/')
# def new_user():
#    return None


# Update User info
@user_bp.get('/edit')
@check_user_login
def get_user_edit_form():
    user = session.get('user')  # User is defined after Login
    user_id = user['client_id']
    user_info = hndl.get_user_from_db(user_id)
    if user_info is None:
        return jsonify({'message': 'Cannot find user'}), 404
    if user_info['date_of_birth'] is not None:
        user_info['date_of_birth'] = datetime.strptime(user_info['date_of_birth'],
                                                       '%d.%m.%Y').strftime('%Y-%m-%d')
    return render_template('client_edit.html', user=user_info, user_id=user_id)


@user_bp.post('/edit')
def edit_user():
    user_data = request.form
    user_id = user_data['user_id']
    date_of_birth = user_data['date_of_birth']
    if date_of_birth is not None:
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').strftime('%d.%m.%Y')
    user = User(user_data['name'], date_of_birth, user_data['address'], user_data['phone'],
                user_data['email'])
    user.id = user_id
    if hndl.update_user_in_db(user):
        return jsonify({'message': 'User info updated successfully'}), 201
    else:
        return jsonify({'message': 'Cannot update user'}), 404


# Get User balance
@user_bp.get('/funds')
@check_user_login
def get_user_wallet_state():
    user = session.get('user')  # User is defined after Login
    user_id = user['client_id']
    user_info = hndl.get_user_from_db(user_id)
    return render_template('client_funds.html', user=user_info)
    # return jsonify({'message': f"{user['client_name']} {user['funds']}"}), 200


# Top up User balance
@user_bp.put('/funds')
@check_user_login
def update_user_wallet():
    amount = request.json
    user = session.get('user')  # User is defined after Login
    if user and amount and amount > 0:
        user.funds += amount
        if hndl.update_user_in_db(user):
            return jsonify({'message': 'User account was successfully funded'}), 200
        return jsonify({'message': 'Cannot top up User account'}), 400
    else:
        return jsonify({'message': 'Cannot top up User account'}), 400


# Get User cart information
@user_bp.get('/cart')
@check_user_login
def get_user_cart():
    user = session.get('user')  # User is defined after Login
    cart = hndl.get_user_cart_from_db(user)
    if cart:
        return jsonify(cart)
    else:
        return jsonify({'message': 'User cart is empty'}), 404


@user_bp.post('/cart')
@check_user_login
def add_user_cart_item():
    return hndl.add_user_cart_item_to_db(request.json)


@user_bp.get('/cart/<int:item_id>')
@check_user_login
def get_user_cart_item(item_id):
    user = session.get('user')  # User is defined after Login
    cart_item = hndl.get_user_cart_item_from_db(user, item_id)
    if cart_item:
        return jsonify(cart_item)
    else:
        return jsonify({'message': 'User cart is empty'}), 404


@user_bp.put('/cart/<int:item_id>')
@check_user_login
def edit_user_cart_item(item_id):
    user = session.get('user')  # User is defined after Login
    return hndl.edit_user_cart_item_in_db(user, item_id)


@user_bp.delete('/cart/<int:item_id>')
@check_user_login
def delete_user_cart_item(item_id):
    user = session.get('user')  # User is defined after Login
    return hndl.delete_user_cart_item_from_db(user, item_id)


@user_bp.get('/order')
@check_user_login
def get_user_orders():
    user = session.get('user')  # User is defined after Login
    user_id = user['client_id']
    orders = hndl.get_user_orders_from_db(user_id)
    if orders is not None:
        orders_str = Converter.convert_to_string(orders)
        user_name = user['user_name']
        return jsonify({'message': f"{user_name} orders: {orders_str}"}), 200
    else:
        return jsonify({'message': 'User orders list is empty'}), 404


@user_bp.get('/order/<int:ord_id>')
@check_user_login
def get_user_order(ord_id):
    user = session.get('user')
    user_id = user['client_id']
    order = hndl.get_user_order_from_db(user_id, ord_id)
    if order is not None:
        order_str = Converter.convert_to_string(order)
        user_name = user['user_name']
        return jsonify({'message': f"{user_name} order {ord_id}: {order_str}"}), 200
    else:
        return jsonify({'message': f'Connot find an order with Id {ord_id}'}), 404


@user_bp.post('/order')
@check_user_login
def add_user_order(item_id):
    user = session.get('user')  # User is defined after Login
    return hndl.add_user_order_to_db(user)


@user_bp.put('/order')
@check_user_login
def edit_user_order(item_id):
    user = session.get('user')  # User is defined after Login
    return hndl.edit_user_order_in_db(user)


@user_bp.delete('/order/<int:ord_id>')
@check_user_login
def delete_user_order(ord_id):
    user = session.get('user')  # User is defined after Login
    return hndl.delete_user_order_from_db(user, ord_id)






