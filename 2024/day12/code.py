import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

type = "input"
# type='example'
# type='example_1'
# type='example_2'
# type='example_3'

with open(type + ".txt", "r") as file:
    lines = file.readlines()

grid = []
for line in lines:
    grid.append(list(line.strip()))

row_num = len(grid)
col_num = len(grid[0])

# aree=[]
# perimetri=[]

total_price = 0

for row in range(row_num):
    for col in range(col_num):
        value = grid[row][col]
        if value != "#":
            area = 0
            perimetro = 0
            to_see = {(row, col)}
            while to_see:
                new_row, new_col = to_see.pop()
                grid[new_row][new_col] = "#"
                area += 1
                perimetro += 4

                if 0 < new_row and grid[new_row - 1][new_col] == value:
                    to_see.add((new_row - 1, new_col))
                    perimetro -= 2
                if new_row < row_num - 1 and grid[new_row + 1][new_col] == value:
                    to_see.add((new_row + 1, new_col))
                    perimetro -= 2
                if 0 < new_col and grid[new_row][new_col - 1] == value:
                    to_see.add((new_row, new_col - 1))
                    perimetro -= 2
                if new_col < col_num - 1 and grid[new_row][new_col + 1] == value:
                    to_see.add((new_row, new_col + 1))
                    perimetro -= 2

            # print(f'{value}:{area}*{perimetro}={area*perimetro}')
            # aree.append(area)
            # perimetri.append(perimetro)
            total_price += area * perimetro


# total_price = np.sum([i*j for i,j in zip(aree, perimetri)])

print(f"Total price: {total_price}\n")

#########################

grid = []
for line in lines:
    grid.append(list(line.strip()))

n_lati_list = []

total_price = 0

contatore = 0

for row in range(row_num):
    for col in range(col_num):
        value = grid[row][col]
        if value > str(contatore) and not value.isdigit():
            area = 0
            num_angoli_esterni = 0
            num_angoli_interni = 0

            to_see = {(row, col)}
            while to_see:
                new_row, new_col = to_see.pop()
                grid[new_row][new_col] = str(contatore)
                area += 1

                confinanti = 0
                direzioni = ["^", ">", "v", "<"]
                direz_vuote = ["^", ">", "v", "<"]
                posizioni_diagonali = {
                    "^>": [-1, 1],
                    ">v": [1, 1],
                    "v<": [1, -1],
                    "<^": [-1, -1],
                }

                if 0 < new_row:
                    if grid[new_row - 1][new_col] == value:
                        to_see.add((new_row - 1, new_col))
                        direz_vuote.remove("^")  # up
                    if grid[new_row - 1][new_col] == str(contatore):
                        direz_vuote.remove("^")  # up

                if new_col < col_num - 1:
                    if grid[new_row][new_col + 1] == value:
                        to_see.add((new_row, new_col + 1))
                        direz_vuote.remove(">")  # right
                    if grid[new_row][new_col + 1] == str(contatore):
                        direz_vuote.remove(">")  # right

                if new_row < row_num - 1:
                    if grid[new_row + 1][new_col] == value:
                        to_see.add((new_row + 1, new_col))
                        direz_vuote.remove("v")  # down
                    if grid[new_row + 1][new_col] == str(contatore):
                        direz_vuote.remove("v")  # down

                if 0 < new_col:
                    if grid[new_row][new_col - 1] == value:
                        to_see.add((new_row, new_col - 1))
                        direz_vuote.remove("<")  # left
                    if grid[new_row][new_col - 1] == str(contatore):
                        direz_vuote.remove("<")  # left

                for i in range(len(direzioni)):
                    if (
                        direzioni[i] in direz_vuote
                        and direzioni[(i + 1) % 4] in direz_vuote
                    ):
                        num_angoli_esterni += 1
                        print(new_row, new_col, direzioni[i], direzioni[(i + 1) % 4])

                    if (
                        direzioni[i] not in direz_vuote
                        and direzioni[(i + 1) % 4] not in direz_vuote
                    ):  # entrambe piene
                        pos_diag = posizioni_diagonali[
                            direzioni[i] + direzioni[(i + 1) % 4]
                        ]
                        if grid[new_row + pos_diag[0]][new_col + pos_diag[1]] not in [
                            value,
                            str(contatore),
                        ]:
                            num_angoli_interni += 1

            n_lati = num_angoli_esterni + num_angoli_interni
            print(f"{value}:A {area} * L {n_lati}={area*n_lati}")
            total_price += area * n_lati

            contatore += 1
            print()
            print("contatore", contatore)

# print(grid)

print(f"Total price: {total_price}")
