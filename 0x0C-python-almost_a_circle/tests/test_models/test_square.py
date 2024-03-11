#!/usr/bin/python3

"""Module containing test cases for the Square class"""
from models.base import Base
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        pass

    def setUp(self):
        """Set up"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tear down"""
        pass

    def test_square__id(self):
        """Test that id is set correctly"""
        self.square1 = Square(5)
        self.assertEqual(self.square1.id, 1)
    def test_square_with_id(self):
        """Test that id is set correctly when passed in as an argument"""
        self.square2 = Square(3, id=50)
        self.assertEqual(self.square2.id, 50)

    def test_square_nb_objects(self):
        """Test that nb_objects is set correctly"""
        self.square1 = Square(5)
        self.square2 = Square(6)
        self.square3 = Square(7)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_square_object_instance(self):
        """Test that object is an instance of Square"""
        self.square_object = Square(10)
        self.assertIsInstance(self.square_object, Square)

    def test_square_size_valid(self):
        """Test that size is set correctly"""
        self.square3 = Square(5)
        self.assertEqual(self.square3.size, 5)

    def test_square_size_non_int(self):
        """Test that TypeError is raised when size is not an int"""
        with self.assertRaises(TypeError):
            self.square3 = Square(size="5")

    def test_square_size_less_than_0(self):
        """Test that ValueError is raised when size is less than 0"""
        with self.assertRaises(ValueError):
            self.neg_square = Square(size=-5)

    def test_square_size_0(self):
        """Test that ValueError is raised when size is 0"""
        with self.assertRaises(ValueError):
            self.square_zero_size = Square(0)

    def test_square_x_valid(self):
        """Test that x is set correctly"""
        self.square4 = Square(5, 3)
        self.assertEqual(self.square4.x, 3)

    def test_square_x_non_int(self):
        """Test that TypeError is raised when x is not an int"""
        with self.assertRaises(TypeError):
            self.square5 = Square(5, "3")

    def test_square_x_less_than_0(self):
        """Test that ValueError is raised when x is less than 0"""
        with self.assertRaises(ValueError):
            self.neg_square_x = Square(5, -3)

    def test_square_y_valid(self):
        """Test that y is set correctly"""
        self.square6 = Square(5, 3, 4)
        self.assertEqual(self.square6.y, 4)

    def test_square_y_non_int(self):
        """Test that TypeError is raised when y is not an int"""
        with self.assertRaises(TypeError):
            self.square7 = Square(5, 3, "4")

    def test_square_y_less_than_0(self):
        """Test that ValueError is raised when y is less than 0"""
        with self.assertRaises(ValueError):
            self.neg_square_y = Square(5, 3, -4)

    def test_square_area(self):
        """Test that area is calculated correctly"""
        self.square8 = Square(5)
        self.assertEqual(self.square8.area(), 25)

    def test_square_str(self):
        """Test that __str__ returns correct format"""
        self.square10 = Square(5, 3, 4, 50)
        self.assertEqual(self.square10.__str__(), "[Square] (50) 3/4 - 5")

    def test_square_display(self):
        """Test that display prints correct output"""
        self.square11 = Square(5, 3, 4, 50)
        self.assertEqual(self.square11.display(), None)

    def test_square_update_args(self):
        """Test that update method updates attributes using args"""
        self.square12 = Square(5, 3, 4, 50)
        self.square12.update(10, 10, 10, 10)
        self.assertEqual(self.square12.__str__(), "[Square] (10) 10/10 - 10")

    def test_square_update_kwargs(self):
        """Test that update method updates attributes using kwargs"""
        self.square13 = Square(5, 3, 4, 50)
        self.square13.update(id=10, size=10, x=10, y=10)
        self.assertEqual(self.square13.__str__(), "[Square] (10) 10/10 - 10")

    def test_square_update_args_kwargs(self):
        """Test that update method updates attributes using args and kwargs"""
        self.square14 = Square(5, 3, 4, 50)
        self.square14.update(10, 3, 5, 25, id=50, size=10, x=10, y=10)
        self.assertEqual(self.square14.__str__(), "[Square] (10) 5/25 - 3")

    def test_square_to_dictionary(self):
        """Test that to_dictionary method returns correct dictionary"""
        self.square15 = Square(5, 3, 4, 50)
        self.assertEqual(self.square15.to_dictionary(), {'id': 50, 'size': 5, 'x': 3, 'y': 4})

    def test_square_save_to_file(self):
        """Test that save_to_file method saves to correct file"""
        self.new_square = Square(2, 3, 4, 50)
        self.new_square2 = Square(4, 5, 6, 60)
        Square.save_to_file([self.new_square, self.new_square2])
        self.assertIsInstance(Square.load_from_file()[0], Square)

    def test_square_save_to_file_empty(self):
        """Test that save_to_file method saves to correct file"""
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_file(self):
        """Test that load_from_file method returns correct list of instances"""
        self.new_square = Square(2, 3, 4, 50)
        self.new_square2 = Square(4, 5, 6, 60)
        Square.save_to_file([self.new_square, self.new_square2])
        self.assertIsInstance(Square.load_from_file()[0], Square)

    def test_square_load_from_file_empty(self):
        """Test that load_from_file method returns empty list"""
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])



    def test_square_to_json_string(self):
        """Test that to_json_string returns the correct JSON string"""
        self.assertEqual(Square.to_json_string(None), "[]")
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertEqual(Square.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(Square.to_json_string([{"id": 1}, {"id": 2}]),
                         '[{"id": 1}, {"id": 2}]')

    def test_square_from_json_string(self):
        """Test that from_json_string returns the correct list of instances"""
        self.assertEqual(Square.from_json_string(None), [])
        self.assertEqual(Square.from_json_string("[]"), [])
        self.assertEqual(Square.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(Square.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{"id": 1}, {"id": 2}])

    def test_square_create(self):
        """Test that create returns the correct instance"""
        self.new_square_dict = {"id": 1, "size": 2, "x": 3, "y": 4}
        self.assertIsInstance(Square.create(**self.new_square_dict), Square)
        self.assertEqual(Square.create(**self.new_square_dict).__str__(), "[Square] (1) 3/4 - 2")

    def test_square_load_from_file_csv(self):
        """Test that load_from_file_csv returns the correct list of instances"""
        self.new_square = Square(2, 3, 4, 50)
        self.new_square2 = Square(4, 5, 6, 60)
        Square.save_to_file_csv([self.new_square, self.new_square2])
        self.assertIsInstance(Square.load_from_file_csv()[0], Square)

    def test_square_save_to_file_csv(self):
        """Test that save_to_file_csv saves to correct file"""
        self.new_square = Square(2, 3, 4, 50)
        self.new_square2 = Square(4, 5, 6, 60)
        Square.save_to_file_csv([self.new_square, self.new_square2])
        self.assertIsInstance(Square.load_from_file_csv()[0], Square)
