#!/usr/bin/python3
"""Console Test Module"""
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
# from console import classes
classes = {"BaseModel": BaseModel, "User": User, "City": City, "State": State,
           "Amenity": Amenity, "Review": Review, "Place": Place}


class ConsoleTest(unittest.TestCase):
    '''Class to test the Console'''
    def test_00_create(self):
        '''Checks the command create'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            str_test = f.getvalue().rstrip()

        str_exp = "** class name missing **"
        self.assertEqual(str_test, str_exp)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create test")
            str_test = f.getvalue().rstrip()

        str_exp = "** class doesn't exist **"
        self.assertEqual(str_test, str_exp)
