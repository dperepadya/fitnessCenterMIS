from flask import g

from db_models.fitness_center import FitnessCenter
from db_models.service import Service
from db_models.trainer import Trainer
from mappers.fitness_center_mappers import fc_to_fcdb
from mappers.service_mappers import service_to_servicedb


def get_fitness_centers_from_db():
    try:
        fitness_centers = g.db.query(FitnessCenter).all()
        return fitness_centers
    except Exception as e:
        print(f"Error fetching fitness centers: {e}")
        return None


def add_fitness_center_to_db(fc):
    if fc is None:
        return False
    new_fc = fc_to_fcdb(fc)
    try:
        g.db.add(new_fc)
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error adding fitness center: {e}")
        return False


def get_fitness_center_from_db(fc_id):
    try:
        fitness_center = g.db.query(FitnessCenter).filter(FitnessCenter.id == fc_id).first()
        return fitness_center
    except Exception as e:
        print(f"Error fetching fitness center: {e}")
        return None


def modify_fitness_center_in_db(fc):
    if fc is None:
        return None
    try:
        fitness_center = g.db.query(FitnessCenter).filter(FitnessCenter.id == fc.id).first()
        if fitness_center:
            fc_to_fcdb(fitness_center, fc)
            g.db.commit()
            return True
        else:
            return False
    except Exception as e:
        g.db.rollback()
        print(f"Error modifying fitness center: {e}")
        return False


def delete_fitness_center_from_db(fc_id):
    try:
        fitness_center = g.db.query(FitnessCenter).filter(FitnessCenter.id == fc_id).first()
        if fitness_center is None:
            return False
        g.db.delete(fitness_center)
        g.db.commit()
        return True

    except Exception as e:
        g.db.rollback()
        print(f"Error deleting fitness center: {e}")
        return False


def get_fitness_center_services_from_db(fc_id):
    try:
        fc_services = g.db.query(Service).filter(Service.fitness_center_id == fc_id).all()
        return fc_services
    except Exception as e:
        print(f"Error fetching fitness center services: {e}")
        return None


def get_fitness_center_service_from_db(fc_id, serv_id):
    try:
        fc_service = g.db.query(Service).filter(
            Service.fitness_center_id == fc_id,
            Service.id == serv_id
        ).first()
        return fc_service
    except Exception as e:
        print(f"Error fetching fitness center service: {e}")
        return None


def add_fitness_center_service_to_db(service):
    if service is None:
        return False
    try:
        new_service = service_to_servicedb(service)
        g.db.add(service)
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error adding fitness center service: {e}")
        return False


def delete_fitness_center_service_from_db(fc_id, serv_id):
    try:
        service = g.db.query(Service).filter(
            Service.fitness_center_id == fc_id,
            Service.id == serv_id
        ).first()
        if service:
            g.db.delete(service)
            g.db.commit()
            return True
        return False
    except Exception as e:
        g.db.rollback()
        print(f"Error deleting fitness center service: {e}")
        return False


def get_fitness_center_trainers_from_db(fc_id):
    try:
        fc_trainers = g.db.query(Trainer).filter(Trainer.fitness_center_id == fc_id).all()
        return fc_trainers
    except Exception as e:
        print(f"Error fetching fitness center trainers: {e}")
        return None


def get_fitness_center_trainer_from_db(fc_id, trainer_id):
    try:
        fc_trainer = g.db.query(Trainer).filter(
            Trainer.fitness_center_id == fc_id,
            Trainer.id == trainer_id
        ).first()
        return fc_trainer
    except Exception as e:
        print(f"Error fetching fitness center trainer: {e}")
        return None


def add_fitness_center_trainer_to_db(trainer):
    if trainer is None:
        return False
    try:
        g.db.add(trainer)
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error adding fitness center trainer: {e}")
        return False


def delete_fitness_center_trainer_from_db(fc_id, trainer_id):
    try:
        trainer = g.db.query(Trainer).filter(
            Trainer.fitness_center_id == fc_id,
            Trainer.id == trainer_id
        ).first()
        if trainer:
            g.db.delete(trainer)
            g.db.commit()
            return True
        return False
    except Exception as e:
        g.db.rollback()
        print(f"Error deleting fitness center trainer: {e}")
        return False