import numpy as np

# file = open("example.txt", "r")
file = open("input.txt", "r")

num_list = []

lines = file.readlines()

def find_first_number(s):
    for char in s:
        if char.isdigit():
            return int(char)

def find_last_number(s):
    for char in s[::-1]:
        if char.isdigit():
            return int(char)

somma = 0
for line in lines:
    first_number = find_first_number(line)
    last_number = find_last_number(line)
    number = 10*first_number+last_number
    somma += number

file.close()

# print(somma)

###################################################

file = open("input.txt", "r")

num_list = []

lines = file.readlines()

numbers = dict({'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9})

def find_first_number(s):

    min_index = len(s)*2
    which_number = None
    for number in numbers:
        index = s.find(number)
        if index!=-1:
            if index<min_index:
                min_index = index
                which_number = numbers[number]

    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            break

    if min_index<first_digit_index:
        return which_number
    else:
        return int(s[first_digit_index])

def find_last_number(s):

    reverse_s = s[::-1]
    min_index = len(s)+1
    which_number = None
    for number in numbers:
        index = reverse_s.find(number[::-1])
        if index!=-1:
            if index<min_index:
                min_index = index
                which_number = numbers[number]

    for i, char in enumerate(reverse_s):
        if char.isdigit():
            first_digit_index = i
            break

    if min_index<first_digit_index:
        return which_number
    else:
        return int(reverse_s[first_digit_index])

somma = 0
for line in lines:
    first_number = find_first_number(line)
    last_number = find_last_number(line)
    number = 10*first_number+last_number
    somma += number

    print(line, number)

file.close()

print(somma)
