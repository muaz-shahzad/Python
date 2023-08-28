class myClass:
    def __init__(self,value):
        self.values = value

    # Simple Method h jo call krny pay print krdy ga
    def Show(self):
        print(f"value is  {self.values}")

    # Getter h ye property likhny say ye getter ban jata hay
    @property
    def ten_value(self):
        return 2*self.values

    @ten_value.setter
    def ten_value(self,new_value):
        self.values = new_value


obj = myClass(10)
# obj.ten_value = 67 ===> ye error day ga is trhn set nhi krskty value


obj.Show()
print("Before",obj.values)
print("Getter Value",obj.ten_value)
obj.ten_value = 30
# 30 krny k bad getter function phr chl raha h r wo 3 ko 2 say multiply kar k 60 return kr raha
print("Set krny k bad value get horhi " ,obj.ten_value)
print("Last ",obj.values)
obj.Show()
