from sqlalchemy import Integer, ForeignKey, Column, Date, Time
from sqlalchemy.orm import relationship

from database.database import Base


class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    trainer_id = Column(Integer, ForeignKey('trainers.id'), nullable=False)

    trainer = relationship("Trainer", back_populates="schedule")

