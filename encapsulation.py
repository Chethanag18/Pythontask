class Program:
    def __init__(self):
        self.name = "Chethana"
        self._age = 22
        self.__salary = 35000
    def display_name(self):
        print("The name is ",self.name)
    def display_age(self):
        print("The age is",self._age)
    def display_salary(self):
        return f"The salary is {self.__salary}"
obj1 = Program()
obj1.display_name()
obj1.display_age()
print(obj1.display_salary())