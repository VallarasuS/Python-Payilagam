class Circle:

    # class level attribute
    PI = 3.14

    # class level method
    @classmethod
    def area(cls, radius):
        return Circle.PI * (radius**2)

    # def area(self, radius):
    #     return Circle.PI * (radius**2)


area_of_circle = Circle.area(5)
