# Codecademy Computer Architecture Portfolio Project
# by MozzarellaMonster
from APU import apu
from Registers import registers

# |---------------------|
# |   FUNCTION CODES    |
# | 001100 - ARITHMETIC |
# |---------------------|

# |---------------------|
# |       OPCODES       |
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
        self.apu = apu()
        self.register = registers()
        

    def read(self, seq):
        if len(seq) != 32:
            print("Invalid input")
            return
        else:
            self.opcode = seq[:6]
            self.num1_reg = seq[6:11]
            self.num2_reg = seq[11:16]
            self.destination_reg = seq[16:21]
            self.bit_shift = seq[21:26]
            self.func = seq[26:31]

        # Arithmetic operations
        if self.opcode == "000001":
            return self.apu.add(self.register.load(int(self.num1_reg, 2)), self.register.load(int(self.num2_reg, 2)))
        elif self.opcode == "000010":
            return self.apu.subtract(self.register.load(int(self.num1_reg, 2)), self.register.load(int(self.num2_reg, 2)))
        elif self.opcode == "000011":
            return self.apu.multiply(self.register.load(int(self.num1_reg, 2)), self.register.load(int(self.num2_reg, 2)))
        elif self.opcode == "000100":
            return self.apu.divide(self.register.load(int(self.num1_reg, 2)), self.register.load(int(self.num2_reg, 2)))
        else:
            print("Invalid input")
            return
