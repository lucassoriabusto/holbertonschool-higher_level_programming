#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size

    def update(self, *args, **kwargs):
        """Updates the Scuare class by assigning an argument to each attribute
        zip(): function takes iterables,
        aggregates them in a tuple, and returns it.
        setattr():"""
        if len(args) > 0:
            new_list = ["id", "size", "x", "y"]
            for a, b in zip(new_list, args):
                setattr(self, a, b)
        else:
            """.items():
            Return the dictionary's key-value pairs"""
            for a, b in kwargs.items():
                setattr(self, a, b)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
