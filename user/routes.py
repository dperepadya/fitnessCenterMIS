from flask import Blueprint, jsonify, request, session
import services as svs
from models.user import User

user_bp = Blueprint('user', __name__)


# Get user info
@user_bp.get('/')
def get_user():
    user = session.get('user')  # User is defined after Login
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not logged in'}), 401


# A user can be added with /register POST command, isn't it?
@user_bp.post('/')
def new_user():
    return None


# Update User info
@user_bp.put('/')
def update_user():
    user_data = request.json
    user = User(user_data['username'], user_data['date of birth'], user_data['address'], user_data['phone'],
                user_data['email'])
    if svs.update_user_in_db(user):
        return jsonify({'message': 'User info updated successfully'}), 201
    else:
        return jsonify({'message': 'Cannot update user'}), 404


# Get User balance
@user_bp.get('/funds')
def get_user_wallet_state():
    user = session.get('user') # User is defined after Login
    if user:
        return jsonify(user['funds']), 200
    else:
        return jsonify({'message': 'Cannot get user balance'}), 404


# Top up User balance
@user_bp.put('/funds')
def update_user_wallet():
    amount = request.json
    user = session.get('user')  # User is defined after Login
    if user and amount and amount > 0:
        user.funds += amount
        if svs.update_user_in_db(user):
            return jsonify({'message': 'User account was successfully funded'}), 200
        return jsonify({'message': 'Cannot top up User account'}), 400
    else:
        return jsonify({'message': 'Cannot top up User account'}), 400


# Get User cart information
@user_bp.get('/cart')
def get_user_cart():
    user = session.get('user')  # User is defined after Login
    cart = svs.get_user_cart_from_db(user)
    if cart:
        return jsonify(cart)
    else:
        return jsonify({'message': 'User cart is empty'}), 404


@user_bp.post('/cart')
def add_user_cart_item():
    return svs.add_user_cart_item_to_db(request.json)


@user_bp.get('/cart/<item_id>')
def get_user_cart_item(item_id):
    user = session.get('user')  # User is defined after Login
    cart_item = svs.get_user_cart_item_from_db(user, item_id)
    if cart_item:
        return jsonify(cart_item)
    else:
        return jsonify({'message': 'User cart is empty'}), 404


@user_bp.put('/cart/<item_id>')
def edit_user_cart_item(item_id):
    user = session.get('user')  # User is defined after Login
    return svs.edit_user_cart_item_in_db(user, item_id)


@user_bp.delete('/cart/<item_id>')
def delete_user_cart_item(item_id):
    user = session.get('user')  # User is defined after Login
    return svs.delete_user_cart_item_from_db(user, item_id)


@user_bp.get('/order')
def get_user_orders():
    user = session.get('user')  # User is defined after Login
    orders = svs.get_user_orders_from_db(user)
    if orders:
        return jsonify(orders)
    else:
        return jsonify({'message': 'User orders list is empty'}), 404


@user_bp.get('/order/<ord_id>')
def get_user_order(ord_id):
    user = session.get('user')  # User is defined after Login
    order = svs.get_user_order_from_db(user, ord_id)
    if order:
        return jsonify(order)
    else:
        return jsonify({'message': f'Connote find an order with Id {ord_id}'}), 404


@user_bp.post('/order')
def add_user_order(item_id):
    user = session.get('user')  # User is defined after Login
    return svs.add_user_order_to_db(user)


@user_bp.put('/order')
def edit_user_order(item_id):
    user = session.get('user')  # User is defined after Login
    return svs.edit_user_order_in_db(user)


@user_bp.delete('/order/<ord_id>')
def delete_user_order(ord_id):
    user = session.get('user')  # User is defined after Login
    return svs.delete_user_order_from_db(user, ord_id)






