class Car(object):
    def __init__(self, maker, color):
        self.maker = maker
        self.color = color

    def drive(self):
        print("I am driving a car made by " + self.maker)

    def park(self):
        print("I am parking a " + self.color + " car")


if __name__ == "__main__":
    # instance 1
    toyota = Car("Toyota", "Red")
    toyota.drive()
    toyota.park()

    # instance 2
    ford = Car("Ford", "Blue")
    ford.drive()
    ford.park()

