from sqlalchemy import Integer, ForeignKey, Column, Date, Time, String
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class Review(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    date = Column(Date, nullable=False)
    grade = Column(Integer, nullable=False)
    comment = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))
    trainer_id = Column(Integer, ForeignKey('trainers.id'))

    client = relationship("Client", back_populates="reviews")
    trainer = relationship("Trainer", back_populates="reviews")
