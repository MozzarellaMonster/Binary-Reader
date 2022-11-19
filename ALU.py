# Class that acts as the Arithmetic Processing Unit of the CPU

class alu:
    def add(num1, num2):
        result = int(num1) + int(num2)
        return result
    
    def subtract(num1, num2):
        result = int(num1) - int(num2)
        return result

    def multiply(num1, num2):
        result = int(num1) * int(num2)
        return result
    
    def divide(num1, num2):
        if int(num1) == 0:
            print("Cannot divide by zero")
            result = 0
        else:
            result = int(num1) // int(num2)
        return result
