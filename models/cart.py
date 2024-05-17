class Cart:
    def __init__(self):
        self.orders = {}  # {id, (order, state)}

    def get_orders(self, state=None):
        if state is None:
            return self.orders.keys()
        else:
            return self.orders[state]

    def get_order(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]
        return False

    def remove_order(self, order_id, state=None):
        if order_id is not None:
            if state is None:
                if order_id in self.orders:
                    del self.orders[order_id]
            else:
                orders_to_remove = [order_id for order_id, (_, order_state) in self.orders.items()
                                    if order_state == state]
                for order_id in orders_to_remove:
                    del self.orders[order_id]
        else:
            return False

    @classmethod
    def empty(cls):
        return cls
