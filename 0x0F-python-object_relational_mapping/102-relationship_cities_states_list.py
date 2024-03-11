#!/usr/bin/python3

"""Lists all states and their corresponding cities
    from the database `hbtn_0e_101_usa`
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import MetaData

metadata = MetaData()


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)
    session = Session(bind=engine)
    metadata.reflect(bind=engine)
    state = metadata.tables['states']
    city = metadata.tables['cities']
    query = session.query(state, city).join(city).all()
    for s in query:
        print('{}: {} -> {}'.format(s[2], s[4], s[1]))
    session.close()
