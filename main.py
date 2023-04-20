from cpu import CPU

# Helper function to read input file
def fetch_instructions():
    with open("instruction_input.txt", "r") as instruction_file:
        instructions = instruction_file.readlines()
    instructions = list(map(lambda s: s.strip(), instructions))
    return instructions

# Helper function to get data for memory initialization
def fetch_data():
    with open("data_input.txt", "r") as data_file:
        data = data_file.readlines()
    data = list(map(lambda s: s.strip(), data))
    return data

# Function to initialize memory with data
def initialize_memory(cpu):
    data_load = fetch_data()
    for data in data_load:
        data_parsed = data.split(",")
        cpu.write_memory(data_parsed[0], data_parsed[1])

# Function to send instructions to CPU
def send_instructions(cpu):
    instructions = fetch_instructions()
    for instruction in instructions:
        cpu.parse_instruction(instruction)

# Pyhton script to run the program
my_cpu = CPU()
print("========================================")
print("Welcome to the CPU Simulator")
print("========================================")
print("Initializing memory from data...")
initialize_memory(my_cpu)
print("Memory initialized.")
print("========================================")
print("Sending instructions to CPU...")
send_instructions(my_cpu)
print("Instructions sent.")
print("========================================")
print("Terminating CPU process...")