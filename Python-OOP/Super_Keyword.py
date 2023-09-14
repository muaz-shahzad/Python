# used to refer parent class

class ParentClass:
    def __init__(self,name):
        self.name = name

    def parentMethod(self):
        print("Parent Method Of parent Class")


class ChildClass(ParentClass):
    def ChildMEthod(self):
        print("Child Method of Child Class")
        # Using super we can access the method of parent class and its method
        super().parentMethod()


# child_obj = ChildClass()
# parent_obj = ParentClass()
# child_obj.ChildMEthod()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        print(f"My name is {self.name} id is {self.id}")


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


obj = Employee("Talha", "120")
obj1 = Programmer("Muaz", "420", "CP")
print(obj1.name)
print(obj1.id)
print(obj1.lang)
print("\nObj ")
print(obj.id)
print(obj.name)
