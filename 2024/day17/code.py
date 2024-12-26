import numpy as np
import pandas as pd
import re
import copy
import time
from pydantic.dataclasses import dataclass
from typing import List, Tuple

type = "input"
# type='example'

with open(type + ".txt", "r") as file:
    lines = file.readlines()

for line in lines:
    if "A" in line:
        reg_A = int(line.strip().split(": ")[1])
    if "B" in line:
        reg_B = int(line.strip().split(": ")[1])
    if "C" in line:
        reg_C = int(line.strip().split(": ")[1])
    if "P" in line:
        program = line.strip().split(": ")[1].split(",")

program = [int(i) for i in program]


def combo(num):
    if 0 <= num <= 3:
        return num
    if num == 4:
        return reg_A
    if num == 5:
        return reg_B
    if num == 6:
        return reg_C
    else:
        raise ValueError


print("program:", program)

pointer = 0
outputs = []

reg_A = 117440

while pointer < len(program):

    instruction = program[pointer]
    operand = program[pointer + 1]

    if instruction == 0:
        reg_A = int(reg_A / (2 ** combo(operand)))

    elif instruction == 1:
        reg_B = reg_B ^ operand

    elif instruction == 2:
        reg_B = combo(operand) % 8

    elif instruction == 3:
        if reg_A != 0:
            pointer = operand - 2

    elif instruction == 4:
        reg_B = reg_B ^ reg_C

    elif instruction == 5:
        outputs.append(str(combo(operand) % 8))

    elif instruction == 6:
        reg_B = int(reg_A / (2 ** combo(operand)))

    elif instruction == 7:
        reg_C = int(reg_A / (2 ** combo(operand)))

    pointer += 2

print(",".join(outputs))

###################################################

for line in lines:
    if "B" in line:
        start_reg_B = int(line.strip().split(": ")[1])
    if "C" in line:
        start_reg_C = int(line.strip().split(": ")[1])
    if "P" in line:
        program = line.strip().split(": ")[1].split(",")

program = [int(i) for i in program]

start_reg_A = 0
found = False
# found=True
max_contatore = 0
L = len(program)

while not found:

    print(f"max_contatore: {max_contatore}/{L}", "reg_A: ", start_reg_A, end="\r")
    reg_A = start_reg_A
    reg_B = start_reg_B
    reg_C = start_reg_C
    contatore = 0
    pointer = 0
    stai_dentro = True
    # outputs=[]

    while pointer < len(program) and stai_dentro:

        instruction = program[pointer]
        operand = program[pointer + 1]
        # print(instruction, operand)

        if instruction == 0:
            reg_A = int(reg_A / (2 ** combo(operand)))

        elif instruction == 1:
            reg_B = reg_B ^ operand

        elif instruction == 2:
            reg_B = combo(operand) % 8

        elif instruction == 3:
            if reg_A != 0:
                pointer = operand - 2

        elif instruction == 4:
            reg_B = reg_B ^ reg_C

        elif instruction == 5:
            if contatore >= len(program):
                stai_dentro = False
            elif combo(operand) % 8 != program[contatore]:
                stai_dentro = False
            else:
                # print('combo', combo(operand)%8)
                # outputs.append(combo(operand)%8)
                contatore += 1

        elif instruction == 6:
            reg_B = int(reg_A / (2 ** combo(operand)))

        elif instruction == 7:
            reg_C = int(reg_A / (2 ** combo(operand)))

        pointer += 2

    if stai_dentro == True and contatore == len(program):
        found = True
        print()
        print(start_reg_A)
    else:
        start_reg_A += 1
        max_contatore = max(max_contatore, contatore)
        # print(outputs)


# print(f'Minimum distance part 1: \n')
