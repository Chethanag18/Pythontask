#Polymorphism : It is Object oriented programming concept in which it has same method name present in different class which performs the different tasks.
#Method-overriding: The subclass provides a specific implementation that already defined in the parent class
#The child class overrides the method of parent class
class Animal:
    def sound(self):
        return "Animals makes sound"
class Dog(Animal):
    def sound(self):
        return "Dog Barks"
class Bird(Animal):
    def sound(self):
        return "Cripping"
animal1 = Animal()
dog1 = Dog()
bird = Bird()
print(animal1.sound())
print(dog1.sound())
print(bird.sound())
    