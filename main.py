import sys, os
from time import sleep

tape_size = 8
file_name = "code.bf"

try:
    file_name = sys.argv[1]
except:
    pass

program_pointer = 0
pointer = 0
tape = []
loop_stack = []
output_ascii = False

script = ""
with open(file_name, "r") as f:
    content = f.read()
    if "ASCII" in content.split("\n")[0]:
        output_ascii = True
    
    for _ in content:
        if _ in "<>+-.,[]":
            script += _
    script_length = len(script)


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
        sleep(0.001)
    elif _ == ",":
        tape[pointer] = ord(input()[0])
    
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