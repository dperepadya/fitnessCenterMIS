from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class TrainerService(Base):
    __tablename__ = 'trainer_services'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    trainer_id = Column(Integer, ForeignKey('trainers.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    capacity = Column(Integer)

    # Relationships
    trainer = relationship("Trainer", back_populates="trainer_service")
    service = relationship("Service", back_populates="trainer_service")
    