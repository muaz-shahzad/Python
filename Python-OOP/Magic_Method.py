class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"
    # __repr__() provides a more technical representation:
    # which is used to define a string representation of an object that's more suitable for developers and debugging.
    def __repr__(self):
        return f"MyClass({self.value})"


# When you create an instance of MyClass and use str() or print() on it, the __str__() method will be called
# automatically:
# This method should return a human-readable string representation of the object.
obj = MyClass(42)

obj = MyClass(42)
print(obj)     # Calls __str__(), prints "MyClass instance with value: 42"
print(repr(obj))  # Calls __repr__(), prints "MyClass(42)"



