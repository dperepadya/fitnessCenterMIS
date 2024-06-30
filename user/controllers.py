# from datetime import datetime

from flask import Blueprint, jsonify, request, session, render_template

from models.order import Order
from user import orm_handlers as hndl
from models.user import User
from utils.login_decorator import check_user_login

user_bp = Blueprint('user', __name__)


# Get user info (session)
@user_bp.get('/')
@check_user_login
def get_user():
    user = session.get('user')  # User is defined after Login
    user_id = user['id']
    user_info = hndl.get_user_from_db(user_id)
    return render_template('client_info.html', user=user_info)
    # return jsonify({'message': f"User: {user['client_name']}"}), 200

# A user is being added with /register POST command

# @user_bp.get('/')
# def new_user():
#    return None


# Update User info
@user_bp.get('/edit')
@check_user_login
def get_user_edit_form():
    user = session.get('user')  # User is defined after Login
    if user is None:
        return jsonify({'message': 'Cannot find user'}), 404
    user_id = user['id']
    user_info = hndl.get_user_from_db(user_id)
    if user_info is None:
        return jsonify({'message': f'Cannot find user {user_id}'}), 404
    # if user_info['date_of_birth'] is not None:
    #    user_info['date_of_birth'] = datetime.strptime(user_info['date_of_birth'],
    #                                                   '%d.%m.%Y').strftime('%Y-%m-%d')
    return render_template('client_edit.html', user=user_info, user_id=user_id)


@user_bp.post('/edit')
def edit_user():
    user_data = request.form
    user_id = user_data['user_id']
    date_of_birth = user_data['date_of_birth']
    # if date_of_birth is not None:
    #    date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').strftime('%d.%m.%Y')
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
    user_id = user['id']
    user_info = hndl.get_user_from_db(user_id)
    return render_template('client_funds.html', user=user_info)
    # return jsonify({'message': f"{user['client_name']} {user['funds']}"}), 200


# Top up User balance
@user_bp.get('/funds/add')
@check_user_login
def get_add_user_funds_form():
    user = session.get('user')  # User is defined after Login
    user_id = user['id']
    user_info = hndl.get_user_from_db(user_id)
    if user_info is None:
        return jsonify({'message': 'Cannot find user'}), 404
    funds = user_info['funds']
    return render_template('client_funds_add.html', user_id=user_id, funds=funds)
    # return jsonify({'message': f"{user['client_name']} {user['funds']}"}), 200


@user_bp.post('/funds/add')
@check_user_login
def add_user_funds():
    user_data = request.form
    user_id = user_data['user_id']
    amount = user_data['amount']
    if amount is None:
        return jsonify({'message': 'Funds value is required'}), 400
    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'message': 'Amount must be number'}), 400
    user_info = hndl.get_user_from_db(user_id)
    current_funds = user_info['funds']
    new_funds = current_funds + amount
    if hndl.update_user_funds_in_db(user_id, new_funds):
        return jsonify({'message': f'User funds updated successfully. The balance {new_funds}'}), 201
    else:
        return jsonify({'message': 'Cannot update user funds'}), 404


@user_bp.get('/orders')
@check_user_login
def get_user_orders():
    user = session.get('user')  # User is defined after Login
    user_id = user['id']
    orders = hndl.get_user_orders_from_db(user_id)
    if orders is None:
        return jsonify({'message': 'User orders list is empty'}), 404
    # orders_str = Converter.convert_to_string(orders)
    # user_name = user['user_name']
    # return jsonify({'message': f"{user_name} orders: {orders_str}"}), 200
    return render_template('orders_list.html', user=user_id, orders=orders)


@user_bp.get('/orders/<int:ord_id>')
@check_user_login
def get_user_order(ord_id):
    user = session.get('user')
    user_id = user['id']
    order = hndl.get_user_order_from_db(user_id, ord_id)
    if order is None:
        return jsonify({'message': f'Connot find an order with Id {ord_id}'}), 404
    # order_str = Converter.convert_to_string(order)
    # user_name = user['user_name']
    # return jsonify({'message': f"{user_name} order {ord_id}: {order_str}"}), 200
    return render_template('order_info.html', user=user_id, order=order, ord_id=ord_id)


@user_bp.get('/orders/delete')
@check_user_login
def get_delete_user_order_form(ord_id):
    user = session.get('user')  # User is defined after Login
    user_id = user['id']
    orders = hndl.get_user_orders_from_db(user_id)
    if orders is None:
        return jsonify({'message': 'User orders list is empty'}), 404
    return render_template('order_delete.html', user=user_id, orders=orders)


@user_bp.post('/orders/delete')
@check_user_login
def delete_user_order(ord_id):
    orders_data = request.form
    order_id = orders_data['order_id']
    # user = session.get('user')  # User is defined after Login
    # user_id = user['id']
    if hndl.delete_user_order_from_db(order_id):
        return jsonify({'message': 'Order removed successfully'}), 201
    else:
        return jsonify({'message': 'Cannot delete the Order'}), 404

# Reservations handling ################################
# 1 st Main endpoint


@user_bp.get('/orders/add')
@check_user_login
def select_trainer_service_form():
    trainer_services = hndl.get_trainer_services_list()
    if trainer_services is None:
        return jsonify({'message': f'Cannot get trainers & services info'}), 404
    return render_template('trainer_service_select.html', trainer_services=trainer_services)

# 2nd endpoint: Select a date of desired reservation
# It's being called from "Trainer & Service" form
# Outputs: trainer_service id


@user_bp.get('/select_date')
def select_date():
    trainer_service_id = request.args.get('trainer_service_id')
    return render_template('select_date.html', trainer_service_id=trainer_service_id)

# 3d endpoint: Select a time slot (start time) of desired reservation
# It's being called from "Select Date" form
# Outputs: date, trainer_service_id


@user_bp.get('/select_time')
def select_time():
    user = session.get('user')  # User is defined after Login
    user_id = user['id']
    trainer_service_id = request.args.get('trainer_service_id')
    trainer_service_id = int(trainer_service_id)
    date = request.args.get('date')
    # if date is not None:
    #    date = datetime.strptime(date, '%Y-%m-%d').strftime('%d.%m.%Y')
    available_time_slots = hndl.get_available_time_slots(user_id, trainer_service_id, date)
    if available_time_slots is None:
        return jsonify({'message': 'Cannot find available time slots'}), 201
    return render_template('select_time.html', trainer_service_id=trainer_service_id, date=date,
                           available_time_slots=available_time_slots)


# It's being called from "Select Time" form
# Inputs: trainer_service_id, date, available time slots

@user_bp.post('/orders/add')
def add_order():
    user_id = session['user']['client_id']
    trainer_service_id = request.form['trainer_service_id']
    date = request.form['date']
    time = request.form['time']
    trainer_service = hndl.get_trainer_service(trainer_service_id)
    if trainer_service is None:
        return None
    trainer_id = trainer_service['trainer_id']
    service_id = trainer_service['service_id']

    order = Order(date, time, user_id, trainer_id, service_id)
    if hndl.add_user_order_to_db(order):
        return jsonify({'message': 'Order added successfully'}), 201
    else:
        return jsonify({'message': 'Failed to add order'}), 500


# User cart ##################################
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


