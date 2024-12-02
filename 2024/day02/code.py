import numpy as np
import pandas as pd

import time


t0 = time.time()

with open("input.txt", "r") as file:
    lines = file.readlines()

############## PART 1 

def is_ok(nums):
    differences = np.diff(nums)

    # se hanno segno opposto, sbagliato
    if np.max(differences)*np.min(differences)<0:
        return 0
    if np.min(np.abs(differences))==0:
        return 0
    if np.max(np.abs(differences))>3:
        return 0
    return 1

total=0
for line in lines:
    nums = [int(i) for i in line.split()]
    total += is_ok(nums)
print(total)


############### PART 2

def is_ok_with_removing(nums):
    for i in range(len(nums)):
        new_nums = np.delete(nums, i)
        if is_ok(new_nums)==1:
            return 1
    return 0

total=0
for line in lines:
    nums = [int(i) for i in line.split()]
    total += is_ok_with_removing(nums)
print(total)

###############

print(f"Execution time: {time.time() - t0}")