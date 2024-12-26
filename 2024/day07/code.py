import numpy as np
import pandas as pd
import re
import copy

with open("input.txt", "r") as file:
    # with open("example.txt", "r") as file:
    lines = file.readlines()


def is_line_ok_binary(expected_result, numbers):

    num_operators = len(numbers) - 1

    for comb in range(2**num_operators):
        binario = str(format(comb, "0" + str(num_operators) + "b"))

        obtained_result = numbers[0]
        for ind in range(num_operators):
            if binario[ind] == "0":
                obtained_result += numbers[ind + 1]
            else:
                obtained_result *= numbers[ind + 1]

        if obtained_result == expected_result:
            return True

    return False


total = 0

for line in lines:
    expected_result = int(line.split(":")[0])
    numbers = [int(i) for i in line.strip().split()[1:]]
    if is_line_ok_binary(expected_result, numbers):
        total += expected_result

print(f"Total number of correct: {total}")


###################### PART 2

lista_1 = []


def is_line_ok_ternary(expected_result, numbers):

    num_operators = len(numbers) - 1

    for comb in range(3**num_operators):
        ternario = str(np.base_repr(comb, 3))

        ternario = ternario.zfill(num_operators)  # Pad to 3 digits
        # print(f"spazi {num_operators}, comb {comb}, ternario {ternario}")
        obtained_result = numbers[0]

        for ind in range(num_operators):
            if ternario[ind] == "0":
                obtained_result += numbers[ind + 1]
            elif ternario[ind] == "1":
                obtained_result *= numbers[ind + 1]
            elif ternario[ind] == "2":
                obtained_result = int(str(obtained_result) + str(numbers[ind + 1]))
            else:
                raise ValueError

        if obtained_result == expected_result:
            # print('obtained')
            lista_1.append(obtained_result)
            return True

    # print('not obtained')
    return False


total = 0

for line in lines:
    expected_result = int(line.split(":")[0])
    numbers = [int(i) for i in line.strip().split()[1:]]
    if is_line_ok_ternary(expected_result, numbers):
        total += expected_result

print(f"Total number of correct: {total}")
