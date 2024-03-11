#!/usr/bin/python3

"""State Module

This script lists all the State objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_states = session.query(State).order_by(State.id).all()
    for state in all_states:
        print('{}: {}'.format(state.id, state.name))
    session.commit()
    session.close()
