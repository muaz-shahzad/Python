class Employee:
    # Class variable h ye
    companyName = "Microsoft"

    def __init__(self, name, ):
        # Instance Property h ye
        self.name = name
        self.raise_amount = 0.02

    def info(self):
        print(f"\nThe name of the Employee {self.name} & the raise amount is {self.raise_amount}")
        print(f"The company name is  {self.companyName}")


Emp1 = Employee("M Muaz Shahzad")
Emp1.raise_amount = 0.05
# Emp1.companyName = "Apple"
Emp1.info()
# Yahan Class variable ki value hi change hojay gi
Employee.companyName = "Google"
Emp2 = Employee("Shahzad")
Emp2.info()
print(Employee.companyName)