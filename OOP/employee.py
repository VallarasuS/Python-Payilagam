# class Employee:
#     pass

# employee_one = Employee()
# print(type(employee_one))

# employee_two = Employee()
# print(type(employee_two))


# class Employee:

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last


# x = Employee("John", "Smith")
# x.hello()


class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def hello(self):
        print(self.first, self.last)

    def increment(self, value):
        self.salary = self.salary + value


x = Employee("John", "Smith", 10000)
x.hello()
x.increment(10000)
print(x.salary)
