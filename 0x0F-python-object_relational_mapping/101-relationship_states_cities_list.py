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
    states_list = []
    for s in query:
        if s[1] not in states_list:
            print('{}: {}'.format(s[0], s[1]))
            states_list.append(s[1])
        print('\t{}: {}'.format(s[2], s[4]))
    session.close()
