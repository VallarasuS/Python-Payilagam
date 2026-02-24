class Student:

    # class level attributes
    # school = "ABC School"

    # @classmethod
    # def create(cls, fname, lname, id):
    #     return Student(fname + " " + lname, id)

    # instance attributes
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # instance methods
    def hello(self):
        print("Hello I'm", self.name, "and my id is", self.id, "from ", self.school)


s1 = Student.create("John", "Abraham", 100)
s1.hello()
print(s1.name, s1.id)

# Student.school = "XYZ School"

s2 = Student.create("Dave", "Adam", 200)
s2.hello()
s2.name = "Adam"
s2.hello()

s3 = Student.create("Rob", "Richard", 300)
s3.hello()
s3.school
