#!/usr/bin/python3

"""Creates the state `California` with the city
    `San Francisco` from the database `hbtn_0e_100_usa`

    Usage:
        ./100-relationship_states_cities.py <user> <password> <db>
"""
import sys
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    # Create the state an, cities=[city]d city
    city = City(name='San Francisco')
    state = State(name='California')
    state.cities.append(city)

    # state.cities.append(city)
    # Save the entries to the database
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
