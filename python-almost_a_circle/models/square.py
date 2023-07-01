#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor.
        Calls the super class with id, x, y, width, and height."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """String representation of Square."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """Updates the values of each attribute."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y,}
