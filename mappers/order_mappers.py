from db_models.order import Order as OrderModel
from models.order import Order as Order


def order_to_orderdb(order):
    if order is None:
        return None
    return OrderModel(
            date=order.date,
            time=order.time,
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

