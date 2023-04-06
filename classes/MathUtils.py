class MathUtils:
    @staticmethod
    def add(a, b):
        return (a + b)
    
    @staticmethod
    def subtract(a, b):
        return (a - b)
    
    @staticmethod
    def multiply(a, b):
        return (a * b)
    
    @staticmethod
    def divide(a, b):
        if b != 0:
            return (a / b)
        else:
            raise ValueError("Division by zero is undefined.")