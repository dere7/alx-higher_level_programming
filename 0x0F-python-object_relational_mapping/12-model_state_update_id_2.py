#!/usr/bin/python3
"""changes the name of a State object"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, update
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = update(State).where(State.id == 2).values(name='New Mexico')
    session.execute(stmt)
    session.commit()
    session.close()
