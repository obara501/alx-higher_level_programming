#!/usr/bin/python3

"""City Class

    Represents a city within a state
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base


class City(Base):
    """Represents a city"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
