list = [1, 2, 3, 4, 5]

# print(dir(list))
# print(list.__add__)


# dir shows the  avalable for that object

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"My name is {self.name}")


p = Person("M Muaz")
# dict shows the available variables and values for that class
print(p.__dict__)
