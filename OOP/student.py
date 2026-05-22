# Student
    # Name
    # id
    # marks
    # department


class Student:
    
    def __init__(self, name, id, mark, department):
        self.name = name
        self.id = id
        self.mark = mark
        self.department = department

    def display(self):
        print(self.name, self.id, self.mark, self.department)


sanjay = Student("Sanjay", "ID100", 500, "BCA")
sanjay.display()

john = Student("John", "ID213", 234, "BSC")
john.display()