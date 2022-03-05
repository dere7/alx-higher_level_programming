#!/usr/bin/python3
"""lists all State objects from database"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print(f'{state.id}: {state.name}')
    session.close()
