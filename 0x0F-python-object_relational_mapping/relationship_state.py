#!/usr/bin/python3

"""State model module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents the states in the USA database

    __tablename__ (str): The MySQL table name to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          cascade='all, delete-orphan',
                          backref=backref("state", cascade="all"))
