#!/usr/bin/python3
"""prints the State object with name passed as argument"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = select(State).where(State.name == argv[4]).order_by(State.id)
    state = session.execute(stmt).first()
    if state is not None:
        print(state[0].id)
    else:
        print('Not found')
    session.close()
