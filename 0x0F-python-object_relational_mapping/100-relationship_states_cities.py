#!/usr/bin/python3
"""lists all City objects from database"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City
    from sys import argv

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = select(State.name, City).join(State, City.state_id == State.id) \
        .order_by(City.id)

    for row in session.execute(stmt).all():
        print(f'{row[0]}: ({row[1].id}) {row[1].name}')
    session.close()
