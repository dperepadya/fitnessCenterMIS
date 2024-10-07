class Review:
    def __init__(self, date, grade, comment, client_id, trainer_id):
        self.date = date
        self.grade = grade
        self.comment = comment
        self.client_id = client_id
        self.trainer_id = trainer_id

    @classmethod
    def empty(cls):
        return cls
