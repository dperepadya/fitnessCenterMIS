class FitnessCenter:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    @classmethod
    def empty(cls):
        return cls

