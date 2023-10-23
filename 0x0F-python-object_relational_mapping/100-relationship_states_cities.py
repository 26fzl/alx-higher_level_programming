#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a Database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
"""
    Access to database,start creating new State object (California) and a
    new City object (San Francisco), make a relationship between
    them, to finally commit the changes to the database.
"""
    database = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(database)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)
    sess.add(cal_state)
    sess.commit()
    sess.close()
