import uuid
from datetime import datetime


class Order:
    def __init__(self, username, address, date_of_birth, phone, email):
        self.id = str(uuid.uuid4())
        self.order_time = datetime.now()
        self.services = {}  # {id, (service, trainer)}

    def get_services(self):
        return self.services

    def add_service(self, service, trainer):
        if service:
            s_id = service.service_id
            if s_id in self.services:
                print(f"Service {s_id} already added")
            else:
                self.services[s_id] = (service, trainer)
                return True
        else:
            print(f"Service object isn't valid")
        return False

    def remove_service(self, service_id):
        if service_id in self.services:
            del self.services[service_id]
            return True
        else:
            print(f"Service {service_id} not found.")
        return False

    def update_service(self, service_id, service_upd, trainer_upd):
        if self.remove_service(service_id):
            return self.add_service(service_upd, trainer_upd)
        else:
            print(f"Service {service_id} not found")
        return False

    @classmethod
    def empty(cls):
        return cls
