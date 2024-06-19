from sqlalchemy import Integer, ForeignKey, Column, Date, String
from sqlalchemy.orm import relationship

from database.database import Base


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    date = Column(Date, nullable=False)
    grade = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    trainer_id = Column(Integer, ForeignKey('trainers.id'), nullable=False)

    client = relationship("Client", back_populates="review")
    trainer = relationship("Trainer", back_populates="review")
