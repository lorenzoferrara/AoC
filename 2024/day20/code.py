import numpy as np
import pandas as pd
import copy

dataset = "input"
# dataset = "example"

with open(dataset + ".txt", "r") as file:
    lines = file.readlines()

if dataset=='input':
    threshold=100
else:
    threshold=1

grid = []

L = len(lines[0])
convert = {".": L**2, "#": -L, "S": 0, "E": L**2}

for row, line in enumerate(lines):
    grid.append([convert[i] for i in line.strip()])
    if "S" in line:
        start = (row, line.index("S"))
    if "E" in line:
        end = (row, line.index("E"))

row_num = len(grid)
col_num = len(grid[0])

#risolvi il maze una volta

to_see = {start}
while to_see:
    row, col = to_see.pop()
    if (row, col) == end:
        continue

    if row > 0:
        new_row=row-1
        new_col=col
        if grid[new_row][new_col] > grid[row][col] + 1:
            grid[new_row][new_col] = grid[row][col] + 1
            to_see.add((new_row, new_col))
    if row < row_num-1:
        new_row=row+1
        new_col=col
        if grid[new_row][new_col] > grid[row][col] + 1:
            grid[new_row][new_col] = grid[row][col] + 1
            to_see.add((new_row, new_col))
    if col > 0:
        new_row=row
        new_col=col-1
        if grid[new_row][new_col] > grid[row][col] + 1:
            grid[new_row][new_col] = grid[row][col] + 1
            to_see.add((new_row, new_col))
    if col < col_num-1:
        new_row=row
        new_col=col+1
        if grid[new_row][new_col] > grid[row][col] + 1:
            grid[new_row][new_col] = grid[row][col] + 1
            to_see.add((new_row, new_col))


# ripercorri il maze indagando le posizioni che si trovano a meno di 2 caseele di 
# distanza che siano libere (non #) e che facciano risparmaire almeno 50
# (o 100) caselle


cheat_length=2
total_cheats=0

to_see = {start}
while to_see:
    row, col = to_see.pop()
    if (row, col) == end:
        continue

    for row_delta in range(-cheat_length, cheat_length+1):
        abs_row_delta = np.abs(row_delta)
        for col_delta in range(-(cheat_length-abs_row_delta), (cheat_length-abs_row_delta)+1):
            if 0<=row+row_delta<=row_num-1 and 0<=col+col_delta<=col_num-1:
                if grid[row+row_delta][col+col_delta]>=grid[row][col]+np.abs(row_delta)+np.abs(col_delta)+threshold:
                    total_cheats+=1

    if row > 0:
        new_row=row-1
        new_col=col
        if grid[new_row][new_col] > grid[row][col]:
            to_see.add((new_row, new_col))
    if row < row_num-1:
        new_row=row+1
        new_col=col
        if grid[new_row][new_col] > grid[row][col]:
            to_see.add((new_row, new_col))
    if col > 0:
        new_row=row
        new_col=col-1
        if grid[new_row][new_col] > grid[row][col]:
            to_see.add((new_row, new_col))
    if col < col_num-1:
        new_row=row
        new_col=col+1
        if grid[new_row][new_col] > grid[row][col]:
            to_see.add((new_row, new_col))


print(f"Total cheats parte 1: {total_cheats}")

#################################################

cheat_length=20
total_cheats=0

if dataset=='input':
    threshold=100
else:
    threshold=50


to_see = {start}
while to_see:
    row, col = to_see.pop()    
    if (row, col) == end:
        continue

    for row_delta in range(-cheat_length, cheat_length+1):
        abs_row_delta = np.abs(row_delta)
        for col_delta in range(-(cheat_length-abs_row_delta), (cheat_length-abs_row_delta)+1):
            if 0<=row+row_delta<=row_num-1 and 0<=col+col_delta<=col_num-1:
                if grid[row+row_delta][col+col_delta]>=grid[row][col]+np.abs(row_delta)+np.abs(col_delta)+threshold:
                    total_cheats+=1

    if row > 0:
        new_row=row-1
        new_col=col
        if grid[new_row][new_col] > grid[row][col]:
            to_see.add((new_row, new_col))
    if row < row_num-1:
        new_row=row+1
        new_col=col
        if grid[new_row][new_col] > grid[row][col]:
            to_see.add((new_row, new_col))
    if col > 0:
        new_row=row
        new_col=col-1
        if grid[new_row][new_col] > grid[row][col]:
            to_see.add((new_row, new_col))
    if col < col_num-1:
        new_row=row
        new_col=col+1
        if grid[new_row][new_col] > grid[row][col]:
            to_see.add((new_row, new_col))


print(f"Total cheats parte 2: {total_cheats}")