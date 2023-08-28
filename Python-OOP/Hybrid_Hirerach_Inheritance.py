# Hybrid & hierarchical Inheritance

class Baseclass:
    pass


class DerivedClass(Baseclass):
    pass


class DerivedClass1(DerivedClass):
    pass


class DerivedClass2(DerivedClass):
    pass
    

class DerivedClass3(DerivedClass):
    pass


class DerivedClass4(DerivedClass1, DerivedClass2):
    pass
