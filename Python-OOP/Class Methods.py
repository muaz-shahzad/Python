class Employee:
    # Class variable h ye
    companyName = "Microsoft"

    def __init__(self, name, ):
        # Instance Property h ye
        self.name = name
        self.raise_amount = 0.02

    # Ye method actual class variable companyName ko chnage nhi kry ga sirf specific instance pay chnge kary ga
    def changeCompany(self,newCompany):
        self.companyName = newCompany

    # Ye Keyword lgany say
    @classmethod
    # Actual class variable companyName ko chnage  kry ga
    def changeCompany_1(cls,newCompany):
        cls.companyName = newCompany

    def info(self):
        # print(f"\nThe name of the Employee {self.name} & the raise amount is {self.raise_amount}")
        print(f"The company name is  {self.companyName}")


Emp1 = Employee("M Muaz Shahzad")
Emp2 = Employee("Shahzad")
Emp1.info()
Emp2.info()

Emp1.changeCompany("Tesla")
Emp1.info()
Emp1.changeCompany_1("Tesla")
Emp1.info()
print(Employee.companyName)