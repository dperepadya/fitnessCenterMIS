from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.sqlalchemy_utils import Base


class Credential(Base):
    __tablename__ = 'credentials'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship("Client", back_populates="credentials")
