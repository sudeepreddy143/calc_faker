from decimal import Decimal

class Calculator:
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return a + b

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return a - b

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return a * b

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
