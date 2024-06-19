from sqlalchemy import Integer, ForeignKey, Column, Date, Time
from sqlalchemy.orm import relationship

from database.database import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    date = Column(Date)
    time = Column(Time)
    client_id = Column(Integer, ForeignKey('clients.id'))
    trainer_id = Column(Integer, ForeignKey('trainers.id'))
    service_id = Column(Integer, ForeignKey('services.id'))

    client = relationship("Client", back_populates="order")
    trainer = relationship("Trainer", back_populates="order")
    service = relationship("Service", back_populates="order")
