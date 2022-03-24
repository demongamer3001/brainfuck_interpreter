import keyboard, sys
from time import sleep

with open("code.bf", "r") as f:
    script = f.read()
    script_length = len(script)

program_pointer = 0
pointer = 0
tape = []
tape_size = 16

for _ in range(tape_size):
    tape.append(0)

while True:
    if program_pointer == script_length:
        sys.stdout.flush()
        exit(0)
    
    _ = script[program_pointer]

    if tape[pointer] < 0:
        tape[pointer] = 255
    if tape[pointer] > 255:
        tape[pointer] = 0

    program_pointer += 1