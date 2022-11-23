# Class that acts as the Arithmetic Logic Unit of the CPU

class alu:
    def add(self, num1, num2):
        print("Adding...")
        result = num1 + num2
        return result
    
    def subtract(self, num1, num2):
        print("Subtracting...")
        result = num1 - num2
        return result

    def multiply(self, num1, num2):
        print("Multiplying...")
        result = num1 * num2
        return result
    
    def divide(self, num1, num2):
        print("Dividing...")
        if num2 == 0:
            print("Cannot divide by zero")
            result = 0
        else:
            result = num1 // num2
        return result
