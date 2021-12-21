#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref='state',
        cascade="all, delete",
        passive_deletes=True)

    @property
    def cities(self):
        """ Getter instance method """
        all_cities = storage.all(City)
        city_list = []

        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)

        return city_list
