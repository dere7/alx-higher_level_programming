#!/usr/bin/python3
"""adds the State object 'Lousisiana' to the database"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, insert
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = insert(State).values(name='Louisiana')
    result = session.execute(stmt)
    print(result.inserted_primary_key[0])
    session.commit()
    session.close()
