#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""


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
    first = session.query(State).order_by(State.id).first()
    if first is None:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
    session.close()
