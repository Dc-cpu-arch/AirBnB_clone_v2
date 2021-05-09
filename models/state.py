#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all,delete', backref='state')
    else:
        @property
        def cities(self):
            """Getter for cities from the same state"""
            instance_list = []
            for key, val in models.storage.all().items():
                if val.__class__.__name__ == 'City'
                and val.state._id == self.id:
                    instance_list.append(val)
            return instance_list
