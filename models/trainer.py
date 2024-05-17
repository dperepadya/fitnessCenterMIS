class Trainer:
    def __init__(self, name):
        self.name = name
        self.schedule = []
        self.rating = 0

    def set_schedule(self, schedule):
        self.schedule = schedule

    def get_schedule(self):
        return self.schedule

    def set_rating(self, rating):
        self.rating = rating

    def get_rating(self):
        return self.rating

    @classmethod
    def empty(cls):
        return cls
