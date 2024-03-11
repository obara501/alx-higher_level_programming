#!/usr/bin/python3

"""Module containing test cases for the Base class"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Set up"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tear down"""
        pass

    def test_base__id(self):
        """Test that id is set correctly"""
        self.base1 = Base()
        self.assertEqual(self.base1.id, 1)

    def test_base_with_id(self):
        """Test that id is set correctly when passed in as an argument"""
        self.base2 = Base(50)
        self.assertEqual(self.base2.id, 50)

    def test_base_nb_objects(self):
        """Test that nb_objects is set correctly"""
        self.base1 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_base_object_instance(self):
        """Test that object is an instance of Base"""
        self.base_object = Base()
        self.assertIsInstance(self.base_object, Base)

    def test_base_id_increment(self):
        """Test that id is incremented correctly"""
        self.base1 = Base()
        self.base2 = Base()
        self.assertEqual(self.base2.id, 2)

    def test_base_id_increment_with_id(self):
        """Test that id is incremented correctly when passed in as an argument"""
        self.base1 = Base(50)
        self.base2 = Base()
        self.assertEqual(self.base2.id, 1)

    def test_base_id_increment_with_id_2(self):
        """Test that id is incremented correctly when passed in as an argument"""
        self.base1 = Base(50)
        self.base2 = Base(50)
        self.assertEqual(self.base2.id, 50)

    def test_base_to_json_string(self):
        """Test that to_json_string returns the correct JSON string"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([{"id": 1}, {"id": 2}]),
                         '[{"id": 1}, {"id": 2}]')

    def test_base_from_json_string(self):
        """Test that from_json_string returns the correct list of instances"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{"id": 1}, {"id": 2}])


    def test_base_load_from_file(self):
        """Test that load_from_file returns the correct list of instances"""
        self.new_rectangle = Rectangle(2, 3)
        self.new_rectangle2 = Rectangle(4, 5)
        Rectangle.save_to_file([self.new_rectangle, self.new_rectangle2])
        self.assertIsInstance(Rectangle.load_from_file()[0], Rectangle)

    def test_base_save_to_csv_file(self):
        """Test that save_to_file_csv saves to correct file"""
        self.new_rectangle = Rectangle(2, 3)
        self.new_rectangle2 = Rectangle(4, 5)
        Rectangle.save_to_file_csv([self.new_rectangle, self.new_rectangle2])
        self.assertIsInstance(Rectangle.load_from_file_csv()[0], Rectangle)

    def test_base_load_from_csv_file(self):
        """Test that load_from_file_csv returns the correct list of instances"""
        self.new_rectangle = Rectangle(2, 3)
        self.new_rectangle2 = Rectangle(4, 5)
        Rectangle.save_to_file_csv([self.new_rectangle, self.new_rectangle2])
        self.assertIsInstance(Rectangle.load_from_file_csv()[0], Rectangle)
