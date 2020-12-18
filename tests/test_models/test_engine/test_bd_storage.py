#!/usr/bin/python3
""" Module for testing db_storage"""
import unittest
import pep8
from models.base_model import BaseModel
from models import storage
import os
from os import getenv


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                 "Skipped because of type of storage")
class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """

    # def test_doc(self):
    #     """
    #     Tests if everything is documented
    #     """
    #     #  Module check
    #     self.assertIsNotNone(console.__doc__)

    #     #  Class check
    #     self.assertIsNotNone(HBNBCommand.__doc__)

    #     # Methods check
    #     for method in dir(HBNBCommand):
    #         self.assertIsNotNone(method.__doc__)

    def test_pep8(self):
        """ Style pep8 """
        style = pep8.StyleGuide(quiet=True)
        # f1 = 'db_storage.py'
        # f2 = 'tests/test_console.py'
        # result = style.check_files([f1, f2])
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")
        # self.assertEqual(True,True)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)


if __name__ == '__main__':
    unittest.main()
