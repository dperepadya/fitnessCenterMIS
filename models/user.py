class User:
    def __init__(self, name, date_of_birth, address, phone, email):
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.funds = 0
        self.id = 0
        self.fitness_center_id = None

    def deposit(self, amount):
        self.funds = amount

    def get_balance(self):
        return self.funds

    @classmethod
    def empty(cls):
        return cls

