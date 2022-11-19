# Codecademy Computer Architecture Portfolio Project
# by MozzarellaMonster
from ALU import alu
from Registers import registers

# OPCODES and FUNCTION CODES are loosely based on MIPS R-type

# |---------------------|
# |       OPCODES       |
# | 000000 - ARITHMETIC |
# | 000011 ------ OTHER |
# |---------------------|

# |---------------------|
# |    FUNCTION CODES   |
# | 000001 -------- ADD | 
# | 000010 --- SUBTRACT |
# | 000011 --- MULTIPLY |
# | 000100 ----- DIVIDE |
# | 000101 ------- LOAD |
# | 000110 ------ STORE |
# |---------------------|

class binary_reader:
    def __init__(self):
        self.opcode = ""
        self.num1_reg = ""
        self.num2_reg = ""
        self.destination_reg = ""
        self.bit_shift = ""
        self.func = ""
        self.alu = alu()
        self.register = registers()
        

    def read(self, seq):
        if len(seq) != 32:
            print("Invalid input, not 32-bit length.")
            return
        else:
            self.opcode = seq[:6]
            self.num1_reg = seq[6:11]
            self.num2_reg = seq[11:16]
            self.destination_reg = seq[16:21]
            self.bit_shift = seq[21:26]
            self.func = seq[26:31]

        # Arithmetic operations
        if self.opcode == "0000000":
            if self.func == "000001":
                return self.alu.add(self.register.load(int(self.num1_reg, 2)), self.register.load(int(self.num2_reg, 2)))
            elif self.func == "000010":
                return self.alu.subtract(self.register.load(int(self.num1_reg, 2)), self.register.load(int(self.num2_reg, 2)))
            elif self.func == "000011":
                return self.alu.multiply(self.register.load(int(self.num1_reg, 2)), self.register.load(int(self.num2_reg, 2)))
            elif self.func == "000100":
                return self.alu.divide(self.register.load(int(self.num1_reg, 2)), self.register.load(int(self.num2_reg, 2)))
            else:
                print("Invalid input, unrecognized function code.")
                return
        elif self.opcode == "000011":
            if self.func == "000101":
                return self.register.load(int(self.destination_reg, 2))
            elif self.func == "000110":
                self.register.store(int(self.num1_reg, 2), int(self.destination_reg, 2))
                print(f"Value {int(self.num1_reg, 2)} stored in register {int(self.destination_reg, 2)}.")
            else:
                print("Invalid input, unrecognized function code.")
                return
        else:
            print("Invalid input, unrecognized operation code.")
            return