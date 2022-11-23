# Class that serves as the registers used for memory storage

class registers:
    def __init__(self):
        self.reg = [0] + [None]*31
        self.count = 1

    def __repr__(self) -> str:
        return str(self.reg)
    
    def store(self, value, index):
        print(f"Value {int(value, 2)} stored in register {int(index, 2)}.")
        self.reg[int(index, 2)] = int(value, 2)

    # Function similar to store() that stores a value at the oldest index.
    # Will overwrite the value at the oldest index based on a count.
    def store_oldest(self, value):
        if None in self.reg:
            self.reg[self.reg.index(None)] = int(value, 2)
        else:
            if self.count > 31:
                self.count = 1
            self.reg[self.count] = int(value, 2)
            self.count += 1

    def load(self, index):
        number = self.reg[int(index, 2)]
        if number == None:
            number = 0
        print(f"Retrieved {number} from register {int(index, 2)}.")
        return number
    
    def reset(self, index):
        self.reg[int(index, 2)] = None
