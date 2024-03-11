#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(
         pool_pre_ping=True)
    Base.metadata.create_all(engine)
