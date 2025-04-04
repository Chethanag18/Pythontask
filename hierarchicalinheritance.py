class Animal:
    def eats(self):
        print("Animal eats food")
class Dog(Animal):
    def barks(self):
        print("Dogs barks")
class Fish(Animal):
    def swims(self):
        print("Fish swims")
dog = Dog()
fish = Fish()
dog.eats()
dog.barks()
fish.eats()
fish.swims()