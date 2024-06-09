from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)

class Base(DeclarativeBase):
    pass