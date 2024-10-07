class Schedule:
    def __init__(self, date, start_time, end_time, trainer_id):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.trainer_id = trainer_id

    @classmethod
    def empty(cls):
        return cls
