#!/usr/bin/python3
"""creates the State 'California' with the City 'San Francisco'"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)
    california = State(name='California')
    california.cities = [City(name='San Francisco')]
    session.add(california)
    session.commit()
    session.close()
