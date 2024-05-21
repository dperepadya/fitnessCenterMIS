from models.cart import Cart
from models.order import Order


class User:
    def __init__(self, username, address, date_of_birth, phone, email):
        self.name = username
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.funds = 0

    def deposit(self, amount):
        self.funds = amount

    def get_balance(self):
        return self.funds

    @classmethod
    def empty(cls):
        return cls

