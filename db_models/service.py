from sqlalchemy import Column, Integer, ForeignKey, String, Float, Text
from sqlalchemy.orm import relationship

from database.database import Base


class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    max_attendees = Column(Integer, nullable=False)
    fitness_center_id = Column(Integer, ForeignKey('fitness_centers.id'))

    fitness_center = relationship("FitnessCenter", back_populates="service")
    order = relationship("Order", back_populates="service")
    trainer_service = relationship("TrainerService", back_populates="service")
