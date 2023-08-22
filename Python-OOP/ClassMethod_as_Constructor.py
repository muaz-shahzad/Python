class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

    def info(self):
        print(f"The name of the Employee {self.name} & the Salary is {self.salary}")


string = "Muaz-1200"
Emp = Employee.fromStr(string)
Emp.info()
