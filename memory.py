class Memory:
    def __init__(self):
        self.size = 128
        #using a dictionary for key=address, value=value
        self.memory = {}
        self.__init__memory()

    #Initialize memory by looping from 0 to size of memory(128) and converts iterated value to binary string
    def __init__memory(self):
        for i in range(self.size):
            self.memory['{0:08b}'.format(i)] = 0

    def read(self, address):
        if self.memory.get(address) is not None:
            return self.memory.get(address)
        return None
        
    def write(self, address, value):
        if self.memory.get(address) is not None:
            self.memory[address] = value             