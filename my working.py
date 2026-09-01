import math

class Calculator:
    universal_num = 100
    def __init__(self):
        print("Welcome calculator")

    def add(self, a, b):
        return a + b + self.universal_num

    def sub(self, a, b):
        return a - b - self.universal_num

    def multiply(self, a, b):
        return a * b * self.universal_num

    def divide(self, a, b):
        return a / b / self.universal_num

# Calculator object creation (no arguments)
obj = Calculator()
# Calculator method call (takes arguments)
print(obj.add(1, 2))

class ScientificCalculator(Calculator):
    def __init__(self, a, b):
        super().__init__()
        print("Welcome to scientific calculator")
        self.a = a
        self.b = b

    def power(self, a=None, b=None):
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        return self.a ** self.b

# ScientificCalculator object creation (takes arguments)
obj2 = ScientificCalculator(2, 3)
# ScientificCalculator method call (no arguments)
print(obj2.power())
# Inherited Calculator method call (takes arguments)
print(obj2.add(5, 3))

class SuperScientificCalculator(ScientificCalculator):
    def __init__(self):
        # SuperScientificCalculator does not take arguments, so we pass default values (0, 0)
        # to the ScientificCalculator constructor.
        super().__init__(0, 0)
        print("Welcome to super scientific calculator")

    def sine(self, a):
        return math.sin(math.radians(a))

# SuperScientificCalculator object creation (no arguments)
obj3 = SuperScientificCalculator()
print(obj3.sine(45))
print(obj3.add(10, 20))

obj4 = SuperScientificCalculator()
print(obj4.power(3, 2))