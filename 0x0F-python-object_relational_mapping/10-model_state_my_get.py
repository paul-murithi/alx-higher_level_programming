#!/usr/bin/python3
"""script that lists all State objects that contain the letter a
   from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(State.name == argv[4]).first()
    if states is None:
        print("Not found")
    else:
        print(states.id)
    session.close()
