# Class that serves as the registers used for memory storage

class registers:
    def __init__(self):
        self.reg = [0] * 8
    
    def store(self, value, index):
        self.reg[index] = value

    def load(self, index):
        return self.reg[index]
    
    def reset(self, index):
        self.reg[index] = 0