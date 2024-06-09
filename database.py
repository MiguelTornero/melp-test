from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)

class Base(DeclarativeBase):
    pass

def create_session():
    return Session(engine)

def initiate_db():
    Base.metadata.create_all(engine, checkfirst=True)