
import numpy as np

file = open("input.txt", "r")
lines = file.readlines()

somma = 0

for line in lines:
    line = [int(i) for i in line.split()]

    new_number = 0
    diff = line
    while np.sum(np.abs(diff)) != 0:
        new_number += diff[-1]
        # print(diff)
        diff = np.diff(diff)
    # print(new_number)
    # print()

    somma += new_number

# print(somma)

########################

file = open("input.txt", "r")
lines = file.readlines()

somma = 0

for line in lines:
    line = [int(i) for i in line.split()]

    new_number = 0
    diff = line
    cur=0
    while np.sum(np.abs(diff)) != 0:
        if cur%2 == 0:
            new_number += diff[0]
        if cur%2 != 0:
            new_number -= diff[0]
        cur += 1
        # print(diff)
        diff = np.diff(diff)
    # print(new_number)
    # print()

    somma += new_number

print(somma)


