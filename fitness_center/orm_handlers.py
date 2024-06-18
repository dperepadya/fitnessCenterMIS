from flask import g

from db_models.client import Client
from db_models.fitness_center import FitnessCenter
from db_models.review import Review
from db_models.schedule import Schedule
from db_models.service import Service
from db_models.trainer import Trainer
from db_models.trainer_services import TrainerService
from mappers.fitness_center_mappers import fc_to_fcdb
from mappers.review_mappers import review_to_reviewdb
from mappers.schedule_mappers import schedule_to_scheduledb
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
        fitness_center = (g.db.query(FitnessCenter)
                          .filter(FitnessCenter.id == fc_id).first())
        return fitness_center
    except Exception as e:
        print(f"Error fetching fitness center: {e}")
        return None


def modify_fitness_center_in_db(fc):
    if fc is None:
        return None
    try:
        fitness_center = (g.db.query(FitnessCenter)
                          .filter(FitnessCenter.id == fc.id).first())
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
        fitness_center = (g.db.query(FitnessCenter)
                          .filter(FitnessCenter.id == fc_id).first())
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
        fc_services = (g.db.query(Service)
                       .filter(Service.fitness_center_id == fc_id).all())
        return fc_services
    except Exception as e:
        print(f"Error fetching fitness center services: {e}")
        return None


def get_fitness_center_service_from_db(fc_id, serv_id):
    try:
        fc_service = (g.db.query(Service)
                      .filter(
            Service.fitness_center_id == fc_id,
            Service.id == serv_id
        ).first())
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
        fc_trainers = (g.db.query(Trainer)
                       .filter(Trainer.fitness_center_id == fc_id).all())
        return fc_trainers
    except Exception as e:
        print(f"Error fetching fitness center trainers: {e}")
        return None


def get_fitness_center_trainer_from_db(fc_id, trainer_id):
    try:
        fc_trainer = (g.db.query(Trainer)
                      .filter(
            Trainer.fitness_center_id == fc_id,
            Trainer.id == trainer_id
        ).first())
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
        trainer = (g.db.query(Trainer)
                   .filter(
                        Trainer.fitness_center_id == fc_id,
                        Trainer.id == trainer_id
                    ).first())
        if trainer:
            g.db.delete(trainer)
            g.db.commit()
            return True
        return False
    except Exception as e:
        g.db.rollback()
        print(f"Error deleting fitness center trainer: {e}")
        return False


def get_fitness_center_trainer_rating_from_db(fc_id, trainer_id):
    try:
        fc_trainer_rating = (g.db.query(Client.name.label('client_name'),
                                        Review.grade.label('grade'))
                             .join(Review, Review.client_id == Client.id)
                             .join(Trainer, Trainer.id == Review.trainer_id)
                             .filter(
                                Trainer.fitness_center_id == fc_id,
                                Trainer.id == trainer_id
                            ).all())
        return fc_trainer_rating
    except Exception as e:
        print(f"Error fetching trainer rating: {e}")
        return None


def add_fitness_center_trainer_rating(review):
    if review is None:
        return False
    try:
        review = review_to_reviewdb(review)
        g.db.add(review)
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error adding trainer rating: {e}")
        return False


def modify_fitness_center_trainer_rating_in_db(fc_id, trainer_id):
    return True


def get_fitness_center_trainer_schedule_from_db(fc_id, trainer_id):
    try:
        fc_trainer_schedule = (g.db.query(Trainer.name.label('trainer_name'),
                                          Schedule.date.label('date'),
                                          Schedule.start_time.label('start_time'),
                                          Schedule.end_time.label('end_time'))
                               .join(Schedule, Schedule.trainer_id == Trainer.id)
                               .filter(Trainer.fitness_center_id == fc_id, Trainer.id == trainer_id)
                               .all())
        return fc_trainer_schedule
    except Exception as e:
        print(f"Error fetching trainer schedule: {e}")
        return None


def add_fitness_center_trainer_schedule(schedule):
    if schedule is None:
        return False
    try:
        schedule_db = schedule_to_scheduledb(schedule)
        g.db.add(schedule_db)
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error adding trainer schedule: {e}")
        return False


def modify_fitness_center_trainer_schedule_in_db(fc_id, trainer_id):
    return True


def delete_fitness_center_trainer_schedule_from_db(trainer_id, schedule_id):
    try:
        schedule = (g.db.query(Schedule)
                    .filter(Schedule.id == schedule_id, Schedule.trainer_id == trainer_id)
                    .first())
        if schedule is None:
            return False
        g.db.delete(schedule)
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error deleting trainer schedule: {e}")
        return False


def get_fitness_center_service_trainers_from_db(fc_id, serv_id):
    try:
        fc_serv_trainers = (g.db.query(Trainer.name.label('name'),
                                       Trainer.age.label('age'),
                                       Trainer.gender.label('gender'))
                            .join(TrainerService, TrainerService.service_id == Service.id)
                            .join(Trainer, TrainerService.trainer_id == Trainer.id)
                            .filter(Service.id == serv_id,
                                    Trainer.fitness_center_id == fc_id,
                                    Service.fitness_center_id == fc_id)
                            .all())
        return fc_serv_trainers
    except Exception as e:
        print(f"Error fetching service trainers from db: {e}")
        return None


def get_fitness_center_trainer_services_from_db(fc_id, trainer_id):
    try:
        fc_trainer_servs = (g.db.query(Service.name.label('name'),
                                       Service.duration.label('duration'),
                                       Service.price.label('price'),
                                       Service.description.label('description'),
                                       Service.max_attendees.label('max_attendees'))
                            .join(TrainerService, TrainerService.service_id == Service.id)
                            .join(Trainer, TrainerService.trainer_id == Trainer.id)
                            .filter(Trainer.id == trainer_id,
                                    Trainer.fitness_center_id == fc_id,
                                    Service.fitness_center_id == fc_id)
                            .all())
        return fc_trainer_servs
    except Exception as e:
        print(f"Error fetching trainer services from db: {e}")
        return None


def get_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id):
    try:
        fc_serv_trainer = (g.db.query(Trainer.name.label('id'),
                                      Trainer.name.label('name'),
                                      Trainer.age.label('age'),
                                      Trainer.gender.label('gender'),
                                      Trainer.fitness_center_id.label('fc_id'),
                                      Service.id.label('service_id'))
                            .join(TrainerService, TrainerService.service_id == Service.id)
                            .join(Trainer, TrainerService.trainer_id == Trainer.id)
                            .filter(Service.id == serv_id, Trainer.id == trainer_id,
                                    Trainer.fitness_center_id == fc_id,
                                    Service.fitness_center_id == fc_id)
                            .first())
        return fc_serv_trainer
    except Exception as e:
        print(f"Error fetching service trainers from db: {e}")
        return None


def add_fitness_center_trainer_and_service_to_db(trainer_id, service_id, capacity):
    try:
        trainer_service = TrainerService(trainer_id=trainer_id, service_id=service_id,
                                         capacity=capacity)
        if trainer_service is None:
            return False
        g.db.add(trainer_service)
        g.db.commit()
        return True
    except Exception as e:
        g.db.rollback()
        print(f"Error adding trainer service: {e}")
        return False


def modify_fitness_center_service_trainer_in_db(fc_id, serv_id, trainer_id):
    return True


def delete_fitness_center_service_trainer_from_db(fc_id, serv_id, trainer_id):
    return True
