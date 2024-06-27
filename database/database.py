import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


host = os.environ.get('DB_HOST', 'localhost')
path = f"postgresql+psycopg2://postgress:example@{host}:5432"
# engine = create_engine(path)
engine = create_engine('sqlite:///fitnessdb.db')

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()

Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)
