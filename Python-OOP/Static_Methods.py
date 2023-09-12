class Math:
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
        self.num = self.num+n

    # self nhi lgana hota static method m
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b



a  = Math(5)
print(a.num)
a.addtonum(5)
print(Math.add(2,2))