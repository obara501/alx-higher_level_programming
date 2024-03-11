#!/usr/bin/python3

"""Prints all the states that contain the letter `a`
    from the database `hbtn_0e_6_usa`
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
    )
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        print('{}: {}'.format(state.id, state.name))
    session.commit()
    session.close()
