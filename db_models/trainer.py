from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class Trainer(Base):
    __tablename__ = 'trainers'
    id = Column(Integer, primary_key=True, index=True)
    # Other columns...
    services = relationship("TrainerService", back_populates="trainer")