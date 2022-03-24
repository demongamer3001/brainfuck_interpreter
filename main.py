import keyboard, sys, os
from time import sleep

file_name = "code.bf"

try:
    file_name = sys.argv[1]
except:
    pass


file_name = "./scripts/" + file_name

script = ""
with open(file_name, "r") as f:
    for _ in f.read():
        if _ in "<>+-.,[]":
            script += _
    script_length = len(script)

program_pointer = 0
pointer = 0
tape = []
loop_stack = []


output_ascii = True
tape_size = 8

for _ in range(tape_size):
    tape.append(0)

while True:
    if program_pointer == script_length:
        sys.stdout.flush()
        break
    
    _ = script[program_pointer]

    if _ == "<":
        pointer -= 1
    elif _ == ">":
        pointer += 1

    elif _ == "+":
        tape[pointer] += 1
    elif _ == "-":
        tape[pointer] -= 1
    
    elif _ == ".":
        if output_ascii:
            print(chr(tape[pointer]), end = "")
            sys.stdout.flush()
        else:
            print(tape[pointer])
        sleep(0.05)
    elif _ == ",":
        tape[pointer] = ord(keyboard.read_key()) # Wait until a key is pressed
        print() # Make a newline
    
    elif _ == "[":
        loop_stack.append(program_pointer + 1)
    elif _ == "]":
        if tape[pointer] != 0:
            program_pointer = loop_stack[-1] - 1
        else:
            loop_stack.pop()


    if pointer < 0:
        pointer = tape_size - 1
    elif pointer > tape_size - 1:
        pointer = 0

    if tape[pointer] < 0:
        tape[pointer] = 255
    elif tape[pointer] > 255:
        tape[pointer] = 0

    program_pointer += 1

print("\nEnd of program.")