class Service:
    def __init__(self, service_id, name, description):
        self.service_id = service_id
        self.name = name
        self.description = description

    @classmethod
    def empty(cls):
        return cls
