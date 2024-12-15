import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

with open("input.txt", "r") as file:
# with open("example.txt", "r") as file:
    line = file.read()

numbers = [int(i) for i in line.strip().split()]

print(numbers)

def get_new_list(numbers):

    result=[]
    for n in numbers:
        L=len(str(n))
        if n==0:
            result.append(1)
        elif L%2==0:
            result.append(int(str(n)[:L//2]))
            result.append(int(str(n)[L//2:]))
        else:
            result.append(n*2024)

    return result

blinks=25
for i in range(blinks):
    print(f"{i+1}/{blinks}, {len(numbers)}")
    numbers = get_new_list(numbers)
    # print(numbers)

print(f"Total stones part 1: {len(numbers)}\n")

######################

numbers = [int(i) for i in line.strip().split()]

frequencies=dict()

def add_frequency(dictionary, value, freq=1):
    if value not in dictionary:
        dictionary[value]=freq
    else:
        dictionary[value] += freq
    return dictionary

for n in numbers:
    frequencies=add_frequency(frequencies, n)

def get_new_frequencies(frequencies):

    result=dict()
    for n in frequencies:
        L=len(str(n))
        if n==0:
            # print('0')
            result = add_frequency(dictionary=result, value=1, freq=frequencies[n])
            # print('result', result)
        elif L%2==0:
            result = add_frequency(dictionary=result, value=int(str(n)[:L//2]), freq=frequencies[n])
            result = add_frequency(dictionary=result, value=int(str(n)[L//2:]), freq=frequencies[n])

        else:
            result = add_frequency(dictionary=result, value=n*2024, freq=frequencies[n])

    return result


blinks=75
for i in range(blinks):
    # print(f"{i+1}/{blinks}, {len(frequencies)}")
    # print(frequencies)
    frequencies = get_new_frequencies(frequencies)

total=0
for n in frequencies:
    total+=frequencies[n]
print(f"Total stones part 1: {total}")
