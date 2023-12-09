
# import numpy as np

# file = open("day8_data.txt", "r")

# lines = file.readlines()

# moves = lines[0][:-1]
# L=len(moves)

# dictionary = dict()
# for line in lines[2:]:
#     dictionary[line[:3]] = dict({'L': line[7:10], 'R': line[12:15]})

# next_word = 'AAA'

# cur=0
# tot_cur=0
# while next_word != 'ZZZ':
#     move = moves[cur%L]
#     cur+=1
#     tot_cur+=1
#     next_word = dictionary[next_word][move]

# print(tot_cur)

########################################

file = open("day8_data.txt", "r")

lines = file.readlines()

moves = lines[0][:-1]
L = len(moves)

dictionary = dict()
for line in lines[2:]:
    dictionary[line[:3]] = dict({'L': line[7:10], 'R': line[12:15]})

next_words = [word for word in dictionary if word[-1] == 'A']
print(next_words)

numbers = []
for next_word in next_words:
    cur = 0
    tot_cur = 0

    while next_word[-1] != 'Z':
        move = moves[cur % L]
        cur += 1
        tot_cur += 1

        next_word = dictionary[next_word][move]

    print(tot_cur)
    numbers.append(tot_cur)

from math import gcd
from functools import reduce

def lcm(x, y):
    return x * y // gcd(x, y)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

result = lcm_of_list(numbers)
print(result)
