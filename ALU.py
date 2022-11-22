# Class that acts as the Arithmetic Logic Unit of the CPU

class alu:
    def add(num1, num2):
        result = int(num1, 2) + int(num2, 2)
        return result
    
    def subtract(num1, num2):
        result = int(num1, 2) - int(num2, 2)
        return result

    def multiply(num1, num2):
        result = int(num1, 2) * int(num2, 2)
        return result
    
    def divide(num1, num2):
        if int(num2, 2) == 0:
            print("Cannot divide by zero")
            result = 0
        else:
            result = int(num1, 2) // int(num2, 2)
        return result
