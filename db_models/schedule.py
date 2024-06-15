from sqlalchemy import Integer, ForeignKey, Column, Date, Time
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time)
    trainer_id = Column(Integer, ForeignKey('trainers.id'))

    trainer = relationship("Trainer", back_populates="schedules")

