# Codecademy Computer Architecture Portfolio Project
# by MozzarellaMonster
from ALU import alu
from Registers import registers

# OPCODES and FUNCTION CODES are loosely based on MIPS R-type
#  _____________________
# |       OPCODES       |
# | 000000 - ARITHMETIC |
# | 000011 ------ OTHER |
# |_____________________|

#  _____________________
# |    FUNCTION CODES   |
# | 000001 -------- ADD | 
# | 000010 --- SUBTRACT |
# | 000011 --- MULTIPLY |
# | 000100 ----- DIVIDE |
# | 000101 ------- LOAD |
# | 000110 ------ STORE |
# |_____________________|

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
            print("Invalid input, not 32-bit length.\n")
            return
        elif set(c for c in seq) != {'0', '1'}:
            print("Invalid input, not binary.\n")
            return
        else:
            self.opcode = seq[:6]
            self.num1_reg = seq[6:11]
            self.num2_reg = seq[11:16]
            self.destination_reg = seq[16:21]
            self.bit_shift = seq[21:26]
            self.func = seq[26:]

        # Arithmetic operations
        if self.opcode == "000000":
            if self.func == "000001":
                result = self.alu.add(self.register.load(self.num1_reg), self.register.load(self.num2_reg))
                self.register.store(f'{result:05b}', self.destination_reg)
                print(result, "\n")
            elif self.func == "000010":
                result = self.alu.subtract(self.register.load(self.num1_reg), self.register.load(self.num2_reg))
                self.register.store(f'{result:05b}', self.destination_reg)
                print(result, "\n")
            elif self.func == "000011":
                result = self.alu.multiply(self.register.load(self.num1_reg), self.register.load(self.num2_reg))
                self.register.store(f'{result:05b}', self.destination_reg)
                print(result, "\n")
            elif self.func == "000100":
                result = self.alu.divide(self.register.load(self.num1_reg), self.register.load(self.num2_reg))
                self.register.store(f'{result:05b}', self.destination_reg)
                print(result, "\n")
            else:
                print("Invalid input, unrecognized function code.\n")
                return
        # Load and store operations
        elif self.opcode == "000011":
            if self.func == "000101":
                return self.register.load(self.destination_reg)
            elif self.func == "000110":
                if self.destination_reg == "00000":
                    self.register.store_oldest(self.num1_reg)
                else:
                    self.register.store(self.num1_reg, self.destination_reg)
            else:
                print("Invalid input, unrecognized function code.\n")
                return
        else:
            print("Invalid input, unrecognized operation code.\n")
            return

bin_reader = binary_reader()
bin_reader.read("00001100101000000000100000000110")
bin_reader.read("00001100011000000001000000000110")
bin_reader.read("00000000001000010010000000000011")
bin_reader.read("00000000001000100010100000000011")
bin_reader.read("00000000100000010011000000000100")
bin_reader.read("00000000001000100001100000000001")
bin_reader.read("00000000101000110011100000000010")

bin_reader.read("28190839402905290432984920384290")
bin_reader.read("00101010101111110010110111110102")
bin_reader.read("                                ")
bin_reader.read("fjdsklfjodskjfioofioewjdfoijiods")
bin_reader.read("10110000110011110100110101000111100100")
