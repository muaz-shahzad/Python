class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def info(self):
        print(f"Id of and Employee {self.id} and name is {self.name} ")





# Inheritance

class Programmer(Employee):
    def showLanguage(self):
        print("THe language is Pyhon")


obj = Employee("Muaz" , 2)
obj.info()
obj_1 = Employee("Talha " ,3)
obj_1.info()
# Inheritance class 
obj_1 = Programmer("Shahab",4)
obj_1.info()
obj_1.showLanguage()
