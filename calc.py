import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return math.pow(a, b)

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)

    def tan(self, a):
        return math.tan(a)

    def log(self, a):
        if a <= 0:
            raise ValueError("Cannot take the logarithm of a non-positive number")
        return math.log(a)

if __name__ == "__main__":
    calculator = Calculator()

    # Example usage
    print(calculator.add(2, 3))
    print(calculator.multiply(4, 5))
    print(calculator.divide(10, 2))
    print(calculator.square_root(16))


