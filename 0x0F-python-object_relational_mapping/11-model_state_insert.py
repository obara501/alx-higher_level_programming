#!/usr/bin/python3

"""Adds the `Louisiana` state
    to the database `hbtn_0e_6_usa`
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import State, Base


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
    )
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_state = State(name='Louisiana')
    query = session.add(new_state)
    session.commit()
    louisiana = session.query(State).filter(State.name == 'Louisiana').first()
    print(louisiana.id)
    session.close()
