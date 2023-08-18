class Person:
    name = "M Muaz "
    occupation = "Software Developer"
    networth = "1000"
    def info(self):
        print(f"Person Name is {self.name} and occupation is  {self.occupation}")



a = Person()
# a.name = "Shahab"
# a.occupation = "Developer"
# print(a.name , a.occupation)

# info fucntion in class and directly print info of a Person
a.info()