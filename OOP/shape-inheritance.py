class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        print("Not implemented")

    def __str__(self):
        return "Shape named :" + self.name

    def __repr__(self):
        return self.name


class Rectangle(Shape):

    def __init__(self, name, width, height):
        super().__init__(name)

        self.width = width
        self.height = height

    def area(self):
        print("Area of", self.name, self.width * self.height)


class Square(Rectangle):

    def __init__(self, name, width, height):
        super().__init__(name, width, height)


shape = Shape("Basic Shape")
print(shape.name)
shape.area()

rect = Rectangle("Rectangle", 10, 3)
print(rect.name, rect.width, rect.height)
rect.area()

square = Square("Square", 10, 10)
square.area()


list = [square, rect, shape]

print(square)
print(rect)
print(shape)
print(list)
