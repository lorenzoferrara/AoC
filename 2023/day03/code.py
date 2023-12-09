
import numpy as np

file = open("day3_data.txt", "r")
content = file.read()
file.close()
symbols = list(set(content))
symbols = [i for i in symbols if not i.isdigit()]
symbols.remove('.')
symbols.remove('\n')

#################################

file = open("day3_data.txt", "r")

lines = file.readlines()


def check(lines, ind_line, start, end):
    for index in range(start-1, end+1):
        if lines[ind_line][index] in symbols:
            return True
        if ind_line<len(lines)-1:
            if lines[ind_line+1][index] in symbols:
                return True
        if ind_line>0:
            if lines[ind_line-1][index] in symbols:
                return True

    return False


somma = 0
for ind_line, line in enumerate(lines):

    cur=0
    start=None
    end=None
    temp = []
    while cur < len(line):
        if line[cur].isdigit():
            start = cur
            while line[cur].isdigit():
                cur += 1
            end = cur
            temp.append([start, end])
        cur +=1

    for start, end in temp:
        if check(lines, ind_line, start, end):
            somma += int(line[start:end])


                # if check_2(lines, pos)

file.close()

# print(somma)


##################################################

file = open("day3_data.txt", "r")

lines = file.readlines()

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


sum_of_products = 0

for ind_line, line in enumerate(lines):

    found_indices = find_all(line, '*')
    if len(found_indices) == 0:
        continue

    for index in found_indices:

        counter = 0
        product = 1

        for line_delta in [-1,0,1]:

            cur=0
            while cur < index+2:
                if lines[ind_line+line_delta][cur].isdigit():
                    start = cur
                    while lines[ind_line+line_delta][cur].isdigit():
                        cur += 1
                    end = cur-1
                    if np.abs(start-index)<=1 or np.abs(end-index)<=1:
                        product *= int(lines[ind_line+line_delta][start:end+1])
                        counter += 1
                cur +=1

        if counter==2:
            sum_of_products += product

file.close()

print(sum_of_products)


