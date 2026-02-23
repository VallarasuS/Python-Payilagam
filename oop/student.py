class Student:

    # dunder methods
    # constructor / Initializer
    def __init__(self, name, standard):
        self.name = name
        self.standard = standard

    def print(self):
        print(self.name)
        print(self.standard)


# def initialize(student, name, standard):
#     student.name = name
#     student.standard = standard


s1 = Student("John", "12A")
# s1.name = "John"
# s1.standard = "12A"
# initialize(s1, "John", "12A")


s2 = Student("Dave", "12A")
# s2.name = "Dave"
# s2.standard = "12A"
# initialize(s2, "Dave", "12A")


s3 = Student("Mike", "12A")
# s3.name = "Mike"
# s3.standard = "12A"
# initialize(s3, "Mike", "12A")


# print(s1.name)
# print(s1.standard)

# print(s2.name)
# print(s2.standard)

# print(s3.name)
# print(s3.standard)

s1.print()
s2.print()
s3.print()
