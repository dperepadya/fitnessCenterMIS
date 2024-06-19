from db_models.trainer import Trainer as TrainerModel
from models.trainer import Trainer as Trainer


def trainerdb_to_trainer(trainer):
    if trainer is None:
        return None
    trainer = Trainer(
        name=trainer.name,
        age=trainer.age,
        gender=trainer.gender
    )
    trainer.fitness_center_id = trainer.fitness_center_id
    return trainer


def trainer_to_trainerdb(trainer):
    if trainer is None:
        return None
    return TrainerModel(
        name=trainer.name,
        age=trainer.age,
        gender=trainer.gender,
        fitness_center_id=trainer.fitness_center_id
    )


def trainer_to_trainerdb(existing_trainer, trainer):
    if existing_trainer is None or trainer is None:
        return None
    existing_trainer.id = trainer.id
    existing_trainer.name = trainer.name,
    existing_trainer.age = trainer.age,
    existing_trainer.gender = trainer.gender,
    existing_trainer.fitness_center_id = trainer.fitness_center_id


