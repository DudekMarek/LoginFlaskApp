import sqlalchemy
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"
    user_id = Column(Integer(), primary_key=True)
    username = Column(String())
    password_hash = Column(String())