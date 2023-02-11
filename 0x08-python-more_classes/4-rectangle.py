#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """The Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """Instance methods that return the area
        and perimeter of a rectangle"""
    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    """Prints out a rectangle in string form"""
    def __str__(self):
        rect = ""

        if self.width == 0 or self.height == 0:
            return rect
        for i in range(self.height):
            for j in range(self.width):
                rect += '#'

            if i != self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
