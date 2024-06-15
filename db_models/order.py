from sqlalchemy import Integer, ForeignKey, Column, Date, Time
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    time = Column(Time)
    client_id = Column(Integer, ForeignKey('clients.id'))
    trainer_id = Column(Integer, ForeignKey('trainers.id'))
    service_id = Column(Integer, ForeignKey('services.id'))

    client = relationship("Client")
    trainer = relationship("Trainer")
    service = relationship("Service")
