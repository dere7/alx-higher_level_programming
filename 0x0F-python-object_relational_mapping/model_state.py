#!/usr/bin/python3
"""contains the class definition of a State and an instance"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """definition of State class with states database table
    with attributes id and name"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f'<State(id={self.id}, name={self.name})>'
