class Animal:
    def __init__(self,name):
        self.name = name
    def makeSound(self):
        print(f"Sound made by the {self.name}")


class Cat(Animal):

    def makeSound(self):
        print("Sound made by the Cat")


d = Cat("Cat")
d.makeSound()
print(d.name)
a = Animal("Dog")
a.makeSound()
print(a.name)
