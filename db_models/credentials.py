from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Credentials(Base):
    __tablename__ = 'credentials'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)

    client = relationship("Client", back_populates="credentials")
