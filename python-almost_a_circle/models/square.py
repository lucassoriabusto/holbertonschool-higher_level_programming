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
