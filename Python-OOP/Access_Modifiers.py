# Public
class Employee:
    def __init__(self, name):
        self.name = name


a = Employee("Shahab")


# print(a.name)
# Private
class Employee1:
    def __init__(self):
        self.__name = "Shahab"


b = Employee1()
# print(b.__name)  # cannot access directly
print(b._Employee1__name)  # can be access indirectly
# Protected
