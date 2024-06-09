class Trainer:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.fitness_center_id = None

    @classmethod
    def empty(cls):
        return cls
