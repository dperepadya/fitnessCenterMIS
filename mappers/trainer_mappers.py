from db_models.trainer import Trainer as TrainerModel
from models.trainer import Trainer as Trainer
from utils.converters import safe_assign


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


def existing_trainer_to_trainerdb(existing_trainer, trainer):
    if existing_trainer is None or trainer is None:
        return None
    safe_assign(existing_trainer, 'id', trainer.id)
    safe_assign(existing_trainer, 'name', trainer.name)
    safe_assign(existing_trainer, 'age', trainer.age)
    safe_assign(existing_trainer, 'gender', trainer.gender)
    safe_assign(existing_trainer, 'fitness_center_id', trainer.fitness_center_id)


