from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, index=True)
    # Other columns...

    trainers = relationship("TrainerService", back_populates="service")
