class Employee:

    def __init__(self, id, fname, lname):
        self.id = id
        self.__fname = fname
        self.__lname = lname
        self.name = self.__fname + " " + self.__lname

    def say_hello(self):
        print("Hello from", self.name)


####################

emp_1 = Employee("100", "John", "Smith")
emp_2 = Employee("101", "Dave", "Richard")

emp_1.say_hello()
emp_2.say_hello()

print(emp_1.name)
