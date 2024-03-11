#!/usr/bin/python3

"""Module for the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square shape class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square class"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Return the string representation of a square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width or self.height
        )

    @property
    def size(self):
        """Return the size of the square

            Args:
                None

            Return:
                `size` of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """Set the size of the square

            Args:
                size (int): Size of the square

            Return:
                None
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update properties of the square"""
        if args or (args and kwargs):
            for index, argument in enumerate(args):
                if index == 0:
                    self.id = argument
                if index == 1:
                    self.size = argument
                if index == 2:
                    self.x = argument
                if index == 3:
                    self.y = argument
        elif kwargs:
            for argument, value in kwargs.items():
                if argument == "id":
                    self.id = value
                if argument == "size":
                    self.width = value
                    self.height = value
                if argument == "x":
                    self.x = value
                if argument == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a `Square`"""
        attributes = ("size", "x", "y", "id")
        square_dict = {}
        for attribute in attributes:
            if hasattr(self, attribute):
                square_dict[attribute] = getattr(self, attribute)
        return square_dict
