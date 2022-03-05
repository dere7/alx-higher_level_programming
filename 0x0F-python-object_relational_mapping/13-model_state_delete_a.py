#!/usr/bin/python3
"""deletes all State object with a name containing 'a'"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, delete
    from sqlalchemy.util._collections import immutabledict
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = delete(State).where(State.name.contains('a'))
    session.execute(stmt, execution_options=immutabledict(
        {'synchronize_session': 'fetch'}))
    session.commit()
    session.close()
