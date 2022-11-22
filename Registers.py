# Class that serves as the registers used for memory storage

class registers:
    def __init__(self):
        self.reg = [0] * 8
    
    def store(self, value, index):
        self.reg[int(index, 2)] = int(value, 2)

    def load(self, index):
        return self.reg[int(index, 2)]
    
    def reset(self, index):
        self.reg[int(index, 2)] = 0
# Need to update to better portray the function of an actual collection of registers.