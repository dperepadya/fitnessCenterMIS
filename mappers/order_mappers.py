from datetime import datetime

from db_models.order import Order as OrderModel
from models.order import Order as Order


def order_to_orderdb(order):
    if order is None:
        return None
    date_obj = datetime.strptime(order.date, '%Y-%m-%d').date()
    time_obj = datetime.strptime(order.time, '%H:%M').time()
    return OrderModel(
            date=date_obj,
            time=time_obj,
            client_id=order.client_id,
            trainer_id=order.trainer_id,
            service_id=order.service_id
        )


def orderdb_to_order(order):
    if order is None:
        return None
    return Order(
            date=order.date,
            time=order.time,
            client_id=order.client_id,
            trainer_id=order.trainer_id,
            service_id=order.service_id
        )


def normalize_time(time_str):
    # If the time is in HH:MM:SS format, strip the seconds
    if len(time_str) == 8:  # HH:MM:SS
        time_obj = datetime.strptime(time_str, '%H:%M:%S').time()
        # Convert to HH:MM format
        time_str = time_obj.strftime('%H:%M')
    elif len(time_str) == 5:  # HH:MM
        time_obj = datetime.strptime(time_str, '%H:%M').time()
        # Already in HH:MM format
        time_str = time_obj.strftime('%H:%M')
    else:
        raise ValueError("Invalid time format")
    return time_str
