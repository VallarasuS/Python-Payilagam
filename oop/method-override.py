# method overriding


class Animal:
    def speak(self):
        print("hello")

    def walk(self):
        print("Walk")


animal = Animal()
animal.speak()


class Dog(Animal):
    def speak(self):
        print("Barks")


dog = Dog()
dog.speak()


class Cow(Animal):

    def speak(self):
        print("Mooo!")


cow = Cow()
cow.speak()
cow.walk()
