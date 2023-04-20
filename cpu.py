from cache import Cache
from memory import Memory

cpu_counter = 0
register_count = 9

def convert_register_to_index(value):
    return int(value[1:])

class CPU:
    # Bulk CPU methods
    def __init__(self):
        self.cpu_counter = cpu_counter
        self.registers = [0] * register_count
        self.cache = Cache()
        self.memory = Memory()
        self.cache_flag = False

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = cpu_counter
    
    def set_cpu_counter(self, value):
        self.cpu_counter = value

    def reset_registers(self):
        for i in range(len(self.registers)):
            self.registers[i] = 0
    
    def set_cache_flag(self, value):
        self.cache_flag = value

    def flush_cache(self):
        self.cache.flush()

    def search_cache(self, address):
        return self.cache.read(address)
    
    def write_cache(self, address, value):
        self.cache.write(address, value)
    
    def search_memory(self, address):
        return self.memory.read(address)
    
    def write_memory(self, address, value):
        self.memory.write(address, value)
    
    # Parser method to read instructions from input file
    def parse_instruction(self, instruction):
        instruction_parsed = instruction.split(",")
        print("Reading instruction: " + instruction)
        self.increment_cpu_counter()
        if instruction_parsed[0] == "ADD":
            self.registers[convert_register_to_index(instruction_parsed[1])] = self.registers[convert_register_to_index(instruction_parsed[2])] + self.registers[convert_register_to_index(instruction_parsed[3])]
        if instruction_parsed[0] == "ADDI":
            self.registers[convert_register_to_index(instruction_parsed[1])] = self.registers[convert_register_to_index(instruction_parsed[2])] + int(instruction_parsed[3])
        if instruction_parsed[0] == "J":
            self.set_cpu_counter(int(instruction_parsed[1]))
        if instruction_parsed[0] == "CACHE":
            if instruction_parsed[1] == 0:
                self.set_cache_flag(False)
            if instruction_parsed[1] == 1:
                self.set_cache_flag(True)
            if instruction_parsed[1] == 3:
                self.flush_cache()
        