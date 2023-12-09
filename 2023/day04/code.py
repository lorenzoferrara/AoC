
import numpy as np

file = open("day4_data.txt", "r")

lines = file.readlines()

somma = 0

for line in lines:
    ind_1 = line.find(':')
    ind_2 = line.find('|')
    winning = line[ind_1+1:ind_2].split()
    winning = set(winning)
    my_numbers = line[ind_2+1:].split()
    my_numbers = set(my_numbers)

    intersection = winning & my_numbers
    L = len(intersection)

    if L>0:
        somma += 2**(L-1)

# print(somma)

########################################################

file = open("day4_data.txt", "r")

lines = file.readlines()

n_lines = len(lines)
n_cards = np.ones(n_lines)


for ind_line, line in enumerate(lines):

    ind_1 = line.find(':')
    ind_2 = line.find('|')
    winning = line[ind_1+1:ind_2].split()
    winning = set(winning)
    my_numbers = line[ind_2+1:].split()
    my_numbers = set(my_numbers)

    intersection = winning & my_numbers
    L = len(intersection)

    for i in range(ind_line+1, ind_line+1+L):
        n_cards[i] += n_cards[ind_line]

print(n_cards)
print(np.sum(n_cards))


