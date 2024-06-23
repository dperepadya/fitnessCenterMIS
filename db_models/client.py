from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from database.database import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String)
    date_of_birth = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    funds = Column(Float)
    fitness_center_id = Column(Integer, ForeignKey('fitness_centers.id'), nullable=False)

    fitness_center = relationship("FitnessCenter", back_populates="client")
    credentials = relationship("Credentials", back_populates="client")
    order = relationship("Order", back_populates="client")
    review = relationship("Review", back_populates="client")

