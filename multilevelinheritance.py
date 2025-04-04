#Multiple Inheritance : In multiple Inheritance the class inherits from the other class which inherited from other class
class Animal:
    def walks(self):
        print("Animal walks")
class Birds(Animal):
    def eats(self):
        print("Bird eats")
class Mammal(Birds):
    def sounds(self):
        print("Makes sound")
mammal = Mammal()
mammal.walks()
mammal.eats()
mammal.sounds()