#!/usr/bin/python3
"""
Contains State class and Base,
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
         __tablename__ (str): The name of the MySQL table to store States.
        id (int): The state's id.
        name (string): The state's name.
         state_id (int): The state the city belongs to

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
