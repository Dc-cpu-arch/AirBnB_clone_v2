#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref

from os import getenv


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address, password: password for you login
        first_name: first name, last_name: last name
    """
    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review", passive_deletes=True, backref="user")
        places = relationship("Place", backref="user", cascade="all, delete")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
