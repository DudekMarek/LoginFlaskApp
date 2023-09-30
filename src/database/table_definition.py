import sqlalchemy
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(64), nullable=False)
    salt = Column(String(32), nullable=False)

    def __init__(self, username, password_hash, salt):
        self.username = username
        self.password_hash = password_hash
        self.salt = salt