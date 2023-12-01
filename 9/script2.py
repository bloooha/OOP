class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type")

# Створення об'єктів
obj1 = MyClass(10)
obj2 = MyClass(20)

# Виклик методу __str__
print(obj1)  # Output: MyClass instance with value: 10

# Виклик методу __add__
result = obj1 + obj2
print(result)  # Output: MyClass instance with value: 30
