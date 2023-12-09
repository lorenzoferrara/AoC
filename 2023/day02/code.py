import numpy as np

file = open("input.txt", "r")

lines = file.readlines()

colors = ['red', 'green', 'blue']

max_numbers = [12, 13, 14]

def find_all(string, substring):
    index = 0
    found = []
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        found.append(index)
        index += len(substring)
    return found

def is_possible(line):
    for max_number, color in zip(max_numbers, colors):
        found = find_all(line, color)
        for index in found:
            number = int(line[index-3:index])
            if number>max_number:
                return False
    return True


somma = 0
for line in lines:
    if is_possible(line):
        game_index = line.find('Game')
        game_number = int(line[game_index+5:game_index+8].replace(":", ""))
        somma += game_number

# print( somma )

#################################################################

import numpy as np

file = open("input.txt", "r")

lines = file.readlines()

colors = ['red', 'green', 'blue']

max_numbers = [12, 13, 14]

def find_all(string, substring):
    index = 0
    found = []
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        found.append(index)
        index += len(substring)
    return found

def find_power(line):

    print(line)
    power = 1
    for color in colors:
        max_number_found = 0
        found = find_all(line, color)
        for index in found:
            number = int(line[index-3:index])
            max_number_found = np.max([number, max_number_found])

        print(color, max_number_found)
        power *= max_number_found


    return power

somma = 0
for line in lines:
    somma += find_power(line)

print( somma )
