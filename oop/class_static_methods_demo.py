class Calculator:
    # Class attribute: shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method doesn't need access to self or cls
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method has access to the class via cls
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
