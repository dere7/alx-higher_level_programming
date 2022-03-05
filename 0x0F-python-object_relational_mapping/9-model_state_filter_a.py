#!/usr/bin/python3
"""lists all State objects that contain the letter a"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = select(State).where(State.name.contains('a')).order_by(State.id)
    for state in session.execute(stmt):
        print(f'{state[0].id}: {state[0].name}')
    session.close()
