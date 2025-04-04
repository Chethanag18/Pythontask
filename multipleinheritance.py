#Multiple Inheritance : one child class inherits from more than one parent class
class Engine:
    def start(self):
        print("Engine started")
class Radio: 
    def play(self):
        print("Radio playing")
class Car(Engine,Radio):
    def drive(self):
        print("start driving")
car = Car()
car.drive()
car.start()
car.drive()