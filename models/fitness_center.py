class FitnessCenter:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.services = {}

    @classmethod
    def empty(cls):
        return cls

