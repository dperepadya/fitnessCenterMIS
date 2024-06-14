from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    date_of_birth = Column(String)
    phone = Column(String)
    email = Column(String)
    funds = Column(Integer)
    fitness_center_id = Column(Integer)
    credentials = relationship("Credential", back_populates="client")
