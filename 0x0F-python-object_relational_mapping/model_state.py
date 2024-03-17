#!/usr/bin/python3
"""contains the class definition of a State and an instance
   Base = declarative_base"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines the state class to be mapped to table state
    __tablename__ (str): The database table to be maped to
    id (Integer): The state's id.
    name(String): The state's name.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
