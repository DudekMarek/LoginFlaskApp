import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

connection_string = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = sqlalchemy.create_engine(connection_string)
Session = sessionmaker(bind=engine)