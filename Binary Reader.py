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
        self.num1 = ""
        self.num2 = ""
        self.constant = ""
        self.func = ""
        self.apu = apu()
        self.register = registers()
        

    def read(self, seq):
        if len(seq) != 32:
            print("Invalid input")
            return
        else:
            self.opcode = seq[:6]
            self.num1 = seq[6:11]
            self.num2 = seq[11:16]
            self.constant = seq[16:26]
            self.func = seq[26:31]

        if self.opcode == "000001":
            return self.apu.add(int(self.num1), int(self.num2))
        elif self.opcode == "000010":
            return self.apu.add(int(self.num1), int(self.num2))
        elif self.opcode == "000011":
            return self.apu.add(int(self.num1), int(self.num2))
        elif self.opcode == "000100":
            return self.apu.add(int(self.num1), int(self.num2))
        else:
            print("Invalid input")
        return
