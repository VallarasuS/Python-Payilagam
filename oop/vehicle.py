class Vehicle:

    def start(self):
        print("vehicle:: started")

    def stop(self):
        print("vehicle:: stopped")

    def drive(self):
        print("vehicle:: driving")


vehicle = Vehicle()
# vehicle.start()
# vehicle.stop()
# vehicle.drive()


class Car(Vehicle):

    def honk():
        print("Car:: honking")


car = Car()
car.start()
car.drive()
car.stop()
