from database_connection import engine
from table_definition import Base

Base.metadata.create_all(engine)