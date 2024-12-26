import numpy as np
import pandas as pd
import re
import copy
import time
from pydantic.dataclasses import dataclass
from typing import List, Tuple

dataset = "input"
# dataset='example'

with open(dataset + ".txt", "r") as file:
    lines = file.readlines()

if dataset == "input":
    size = 70
    firstlines = 1024
else:
    size = 6
    firstlines = 12

coords = []

grid = np.ones((size + 1, size + 1)) * size**2

for line in lines[:firstlines]:
    row, col = line.strip().split(",")
    row = int(row)
    col = int(col)
    coords.append([row, col])
    grid[row, col] = -size

# print(grid)

start = (0, 0)
grid[0, 0] = 0
end = (size, size)


def add_adjacent(row, col, new_row, new_col):

    # print(f'from ({row},{col})={grid[row,col]} to ({row},{col})={grid[new_row,new_col]}')

    if grid[new_row, new_col] > grid[row, col] + 1:
        grid[new_row, new_col] = grid[row, col] + 1
        to_see.add((new_row, new_col))


to_see = {start}
while to_see:
    row, col = to_see.pop()
    if (row, col) == end:
        continue

    if row > 0:
        add_adjacent(row, col, row - 1, col)
    if row < size:
        add_adjacent(row, col, row + 1, col)
    if col > 0:
        add_adjacent(row, col, row, col - 1)
    if col < size:
        add_adjacent(row, col, row, col + 1)

print(f"Shortest path: {grid[size,size]}\n")

#####################################################

still_accessible = True
while still_accessible:
    firstlines += 1
    print(f"iteration {firstlines}", end="\r")

    grid = np.ones((size + 1, size + 1)) * size**2

    for line in lines[:firstlines]:
        row, col = line.strip().split(",")
        row = int(row)
        col = int(col)
        coords.append([row, col])
        grid[row, col] = -size

    # print(grid)

    start = (0, 0)
    grid[0, 0] = 0
    end = (size, size)

    def add_adjacent(row, col, new_row, new_col):

        # print(f'from ({row},{col})={grid[row,col]} to ({row},{col})={grid[new_row,new_col]}')

        if grid[new_row, new_col] > grid[row, col] + 1:
            grid[new_row, new_col] = grid[row, col] + 1
            to_see.add((new_row, new_col))

    to_see = {start}
    while to_see:
        row, col = to_see.pop()
        if (row, col) == end:
            continue

        if row > 0:
            add_adjacent(row, col, row - 1, col)
        if row < size:
            add_adjacent(row, col, row + 1, col)
        if col > 0:
            add_adjacent(row, col, row, col - 1)
        if col < size:
            add_adjacent(row, col, row, col + 1)

    if grid[size, size] == size**2:
        still_accessible = False
        wrong_firstlines = firstlines - 1

print()
print(f"Blocking piece: {lines[wrong_firstlines]}")


# print(f'Minimum distance part 1: \n')
