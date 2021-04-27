#!/usr/bin/python3
""" Engine to handle objects with ORM SQLAlchemy """

from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
classes = [State, City, User, Review, Place]

class DBStorage:
    """ SQLAlchemy database storage class """

    __engine = None
    __session = None

    classes = {
        'User': User, 'Place': Place, 'State': State,
        'City': City,  # 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        """ DBStorage: Instantance initialization """

        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session depending of the class name"""

        objs_dict = {}
        if cls:
            my_query = self.__session.query(cls).all()
            for obj in my_query:
                objs_dict[cls + "." + obj.id] = obj
        else:
            for key, value in self.classes.items():
                my_query = self.__session.query(value).all()
                for obj in my_query:
                    objs_dict[key + "." + obj.id] = obj

        return objs_dict

    def new(self, obj):
        """ Adds the object to the current SQL session """
        self.__session.add(obj)

    def save(self):
        """ Commit changes comming from the current SQL session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the object from the current SQL session """
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """ Creates the current database session and all its tables """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''closses the sqlalchemy session'''
        self.__session.close()
