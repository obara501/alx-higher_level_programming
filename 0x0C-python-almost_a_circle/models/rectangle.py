#!/usr/bin/python3

"""A module containing a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance

            Args:
                width (int): Width of the rectangle
                height (int): Height of the rectangle
                x (int): x coordinates of the rectangle
                y (int): y coordinates of the rectangle

            Returns:
                None
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle

            Args:
                width (int): width of the rectangle

            Returns:
                None

            Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle

            Args:
                height (int): height of the rectangle

            Returns:
                None

            Raises:
                TypeError: height must be an integer
                ValueError: height must be >= 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Gets the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x coordinate of the rectangle

            Args:
                x (int): X-coordinate of the rectangle

            Returns:
                None

            Raises:
                TypeError: x must be an integer
                ValueError: x must be >= 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Gets the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y coordinate of the rectangle

            Args:
                y (int): Y-coordinate of the rectangle

            Returns:
                None

            Raises:
                TypeError: y must be an integer
                ValueError: y must be >= 0
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates area of a rectangle

            Args:
                None

            Returns:
                Area of a rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """Display the shape of a rectangle of `width` and `height`"""
        shape = ""
        area = self.area()
        shape += self.__y * "\n"
        for value in range(area):
            if value == 0:
                shape += self.__x * " "
                shape += "#"
                continue
            if value % self.__width == 0:
                shape += "\n"
                shape += self.__x * " "
            shape += "#"
        print(shape)

    def update(self, *args, **kwargs):
        """Updates the reactangle's properties

            Args:
                *args () : list of properties of the rectangle
        """
        if args or (args and kwargs):
            for index, argument in enumerate(args):
                if index == 0:
                    self.id = argument
                if index == 1:
                    self.__width = argument
                if index == 2:
                    self.__height = argument
                if index == 3:
                    self.__x = argument
                if index == 4:
                    self.__y = argument
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        attrs = ("id", "width", "height", "x", "y")
        rectangle_dict = {}
        for attribute in attrs:
            if hasattr(self, attribute):
                rectangle_dict[attribute] = getattr(self, attribute)
        return rectangle_dict
