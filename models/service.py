class Service:
    def __init__(self, name, description, duration, price, max_attendees):
        self.name = name
        self.description = description
        self.duration = duration
        self.price = price
        self.max_attendees = max_attendees
        self.fitness_center_id = None

    @classmethod
    def empty(cls):
        return cls
