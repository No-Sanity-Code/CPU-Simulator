from cache import Cache
from memory import Memory

cpu_counter = 0
register_count = 9

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
    

    