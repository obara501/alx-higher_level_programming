#!/usr/bin/python3

"""Updates the name of a state whose id is `2`
    in the database `hbtn_0e_6_usa` to "New Mexico"
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from model_state import Base, State


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    )
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    try:
        result = session.query(State).filter(State.id == 2).first()
        result.name = "New Mexico"
        session.commit()
    except SQLAlchemyError as error:
        pass
    finally:
        session.close()
