class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello from ", self.name)


p1 = Person("John")


class Student(Person):

    def __init__(self, name, degree):
        super().__init__(name)
        self.degree = degree


class Staff(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


staff = Staff("Mike", "Algorithms")
staff.hello()
print(staff.subject)

s1 = Student("Dave", "CS")
s1.hello()
print(s1.degree)
