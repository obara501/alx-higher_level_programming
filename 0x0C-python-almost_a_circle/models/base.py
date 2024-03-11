#!/usr/bin/python3

"""A module containing a Base class"""
import json
import csv
import turtle


class Base:
    """A base class

        Attributes:
            __nb_objects (int): Number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class

            Args:
                id (int): Id of a created object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of `list_dictionaries`"""
        if list_dictionaries and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON representation of a shape to a file

            Args:
                list_objs (list): List of object\
                    instances of the `Base` class
        """
        if list_objs is None:
            json_objs = cls.to_json_string([])
        else:
            json_list = [obj.to_dictionary() for obj in list_objs]
            json_objs = cls.to_json_string(json_list)
        with open("{}.json".format(cls.__name__),
                  mode="w", encoding="utf-8") as file:
            file.write(json_objs)

    @staticmethod
    def from_json_string(json_string):
        """Convert the JSON `json_string`

            Args:
                `json_string` (str): a JSON string representing\
                    a list of dictionaries
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a shape instance from `dictionary`"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        cls.update(new_instance, **dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file"""
        instances = []
        try:
            with open(cls.__name__ + ".json",
                      mode="r", encoding="utf-8") as file:
                list_content = cls.from_json_string(file.read())
                for obj in list_content:
                    instances.append(cls.create(**obj))
                return instances
        except FileNotFoundError:
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the CSV representation of a shape to a file

            Args:
                list_objs (list): List of object\
                    instances of the `Base` class
        """
        if list_objs is None:
            return
        with open("{}.csv".format(cls.__name__),
                  mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow(
                        [obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file"""
        instances = []
        try:
            with open(cls.__name__ + ".csv",
                      mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(row[0]), "width": int(row[1]),
                                      "height": int(row[2]), "x": int(row[3]),
                                      "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(row[0]), "size": int(row[1]),
                                      "x": int(row[2]), "y": int(row[3])}
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw the shapes in `list_rectangles` and \
            `list_squares` using the `turtle` module"""
        turtle.Screen().colormode(255)
        turtle.Screen().bgcolor(255, 255, 255)
        turtle.Screen().title("Draw  Rectangles and Squares")
        turtle.Screen().setup(width=800, height=600)

        for a_shape in list_rectangles + list_squares:
            my_turtle = turtle.Turtle()
            my_turtle.pensize(3)
            my_turtle.shape("turtle")
            my_turtle.color("black")
            my_turtle.speed(1)
            my_turtle.penup()
            my_turtle.pendown()
            my_turtle.setpos(a_shape.x, a_shape.y)
            my_turtle.forward(a_shape.width)
            my_turtle.left(90)
            my_turtle.pendown()
            my_turtle.forward(a_shape.height)
            my_turtle.left(90)
            my_turtle.forward(a_shape.width)
            my_turtle.left(90)
            my_turtle.forward(a_shape.height)
            my_turtle.left(90)
            my_turtle.penup()
            my_turtle.hideturtle()
        turtle.done()
