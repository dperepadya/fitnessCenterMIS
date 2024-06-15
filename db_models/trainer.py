from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class Trainer(Base):
    __tablename__ = 'trainers'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    fitness_center_id = Column(Integer, ForeignKey('fitness_centers.id'))

    fitness_center = relationship("FitnessCenter", back_populates="trainers")
    schedules = relationship("Schedule", back_populates="trainer")
    orders = relationship("Order", back_populates="trainer")
    services = relationship("TrainerService", back_populates="trainer")
