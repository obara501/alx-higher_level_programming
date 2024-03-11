# Python classes with tests

## Description

This project is about creating classes and testing them with unittest.

## Table of contents

Files | Description
------|------------
[tests](./tests) | Folder containing all the tests
[tests/test_models](./tests/test_models) | Folder containing all the tests for the models
[tests/test_models/test_base.py](./tests/test_models/test_base.py) | Test for the Base class
[tests/test_models/test_rectangle.py](./tests/test_models/test_rectangle.py) | Test for the Rectangle class
[tests/test_models/test_square.py](./tests/test_models/test_square.py) | Test for the Square class
[models](./models) | Folder containing all the classes
[models/base.py](./models/base.py) | Class Base
[models/rectangle.py](./models/rectangle.py) | Class Rectangle
[models/square.py](./models/square.py) | Class Square
[models/__init__.py](./models/__init__.py) | File that makes the folder a module

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- PEP 8 style
- All the files must be executable

## Compilation

`cd` int
Make sure all the files are executable:
`$ chmod u+x *.py`

## Execution

### Run tests

From the root folder of the project, run:
`$ python3 -m unittest discover tests`

### Run main files

From the root folder of the project, run:
`$ ./<name_of_the_file>.py` # All the main files are executable

## Author

- __Andrew Maina__ - [Andrew-Maina](https://github.com/KingMaina)
