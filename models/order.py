
class Order:
    def __init__(self, date, time, client_id, trainer_id, service_id):
        self.date = date
        self.time = time
        self.client_id = client_id
        self.trainer_id = trainer_id
        self.service_id = service_id

    @classmethod
    def empty(cls):
        return cls
