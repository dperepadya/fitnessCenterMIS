from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class TrainerService(Base):
    __tablename__ = 'trainer_services'
    id = Column(Integer, primary_key=True, index=True)
    trainer_id = Column(Integer, ForeignKey('trainers.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    capacity = Column(Integer)

    # Relationships
    trainer = relationship("Trainer", back_populates="services")
    service = relationship("Service", back_populates="trainers")
    