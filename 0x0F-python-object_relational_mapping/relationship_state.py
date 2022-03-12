#!/usr/bin/python3
"""contains the class definition of a State and an instance"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """definition of State class with states database table
    with attributes id and name"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state',
                          cascade="all, delete, delete-orphan")
