#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv

storage_engine = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if storage_engine != "db":
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with
            state_id equals to the current State.id"""
            from models import storage
            from models.city import City
            matching_cities = []
            city_instances = storage.all(City).values()
            for city in city_instances:
                if city.state_id == self.id:
                    matching_cities.append(city)
            return (matching_cities)
