#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest
import pep8
from models.base_model import BaseModel


class test_review(test_basemodel):
    """ """

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
        # f1 = 'review.py'
        # f2 = 'tests/test_console.py'
        # result = style.check_files([f1, f2])
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")
        # self.assertEqual(True,True)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    # def test_place_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.place_id), str)

    # def test_user_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.user_id), str)

    # def test_text(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.text), str)


if __name__ == '__main__':
    unittest.main()
