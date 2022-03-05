#!/usr/bin/python3
"""contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """definition of city class with city database table
    with attributes id and name"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))

    def __repr__(self):
        return f'<City(id={self.id}, name={self.name}), \
            state_id={self.state_id}>'
