#!/usr/bin/python3
"""Class Rectangle that inherits from Base."""


from models.base import Base


class Rectangle(Base):
    """Inherits Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor.
        super() calls a method of the inherited Base class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints a Rectangle.
           x and y control the print position of the rectangle."""
        for y in range(self.__y):
            print()
        for y in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}")

    def update(self, *args):
        """enumerate() iterar sobre una secuencia y proporcionar tanto el
        índice como el valor correspondiente en cada iteración.

        setattr() establece el valor de un atributo en un objeto.
        Toma tres argumentos: el objeto al que asignar el atributo,
        el nombre del atributo y el valor a asignar.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)
