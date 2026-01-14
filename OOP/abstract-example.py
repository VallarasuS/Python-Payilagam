from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("Rectangle Area")


# can not instantiate an abstract class
# shape = Shape()
# shape.area()

rectangle = Rectangle()
rectangle.area()
