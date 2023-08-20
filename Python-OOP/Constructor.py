# class Person:
#     name = "M Muaz "
#     occupation = "Software Developer"
#     networth = "1000"
#     def info(self):
#         print(f"Person Name is {self.name} and occupation is  {self.occupation}")


class Person:
    # syntax of constructor ye har time call hoga jab b ek new object bnaty
    # COnstructor is invoked auto when an object of class created
    # Sepcial method used to create and initialza of an object
    # Slef auto pay pass hojata h self k ilawa values deni prti arguments ki
    def __init__(self,n,o):
        self.name = n
        self.occupation  = o
    def info(self):
        print(f"Person Name is {self.name} & occupation is  {self.occupation}")

a = Person("Muaz" ,"Developer")
b = Person("Shahab", "Cyber ")


a.info()
b.info()