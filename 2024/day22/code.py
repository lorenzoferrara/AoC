import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations
from functools import lru_cache

type='input'
# type='example'


@lru_cache(maxsize=None) 
def next_secret_number(num):
    temp = num*64
    num = num ^ temp
    num = num % 16777216 #2^24

    temp = int(num/32)
    num = num ^ temp
    num = num % 16777216

    temp = num*2048
    num = num ^ temp
    num = num % 16777216

    return num

with open(type+'.txt', 'r') as file:
    lines = file.readlines()

total=0
for line in lines:
    start = int(line.strip())
    num=start

    for i in range(2000):
        num=next_secret_number(num)

    total+=num

    # print(start, num)

print(f'Final secret number: {total}\n')

############################################

#first i save all possible sequences of 4 differnces

sequences = dict()

for line in lines:
    start = int(line.strip())
    num=start

    sequence=[]
    for i in range(2000):
        new_num=next_secret_number(num)

        new_price = new_num%10 
        diff = new_price - (num%10)
        num=new_num
        sequence.append(diff)
        if i>3:
            sequence.pop(0)
            if tuple(sequence) not in sequences:
                sequences[tuple(sequence)]=[start]
            else:
                sequences[tuple(sequence)].append(start)
        elif i==3:
            if tuple(sequence) not in sequences:
                sequences[tuple(sequence)]=[start]
            else:
                sequences[tuple(sequence)].append(start)

    total+=num

L=len(sequences)
print(f'{L} sequenze')

# then i inspect all sequences and see the outcome

max_result=0

for ind,chosen_sequence in enumerate(sequences):

    print(f'max:{max_result}, {ind}/{L}', end='\r')
    result=0

    for line in lines:
        start = int(line.strip())

        if start in sequences[chosen_sequence]:
            num=start

            sequence=[]
            for i in range(2000):
                new_num=next_secret_number(num)

                new_price = new_num%10 
                diff = new_price - (num%10)
                num=new_num

                sequence.append(diff)
                if i>3:
                    sequence.pop(0)

                if i>=3:
                    if tuple(sequence)==chosen_sequence:
                        result+=new_price
                        break

    max_result = max(max_result, result)

    # print(start, num)

print()
print(f'Final secret number: {max_result}')


