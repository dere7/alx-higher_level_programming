#!/usr/bin/python3
"""lists all State objects, and corresponding City objects"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base
    from relationship_city import City
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)
    for row in session.query(City).order_by(City.id):
        print(f'{row.id}: {row.name} -> {row.state.name}')
    session.commit()
    session.close()
