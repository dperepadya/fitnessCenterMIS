from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from database.database import Base


class FitnessCenter(Base):
    __tablename__ = 'fitness_centers'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

    trainer = relationship("Trainer", back_populates="fitness_center")
    service = relationship("Service", back_populates="fitness_center")
    client = relationship("Client", back_populates="fitness_center")
