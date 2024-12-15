import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

# with open("input.txt", "r") as file:
with open("example.txt", "r") as file:
    lines = file.readlines()

grid=[]
for line in lines:
    grid.append(list(line.strip()))

row_num=len(grid)
col_num=len(grid[0])

def find_reachable_peaks(start):
    reachable=set()
    to_see={start}
    while to_see:

        # print(to_see)
        row,col = to_see.pop()
        value = int(grid[row][col])
        if value==9:
            reachable.add((row,col))
        else:
            if row>=1 and int(grid[row-1][col])==value+1:
                to_see.add((row-1, col))
            if row<=row_num-2 and int(grid[row+1][col])==value+1:
                to_see.add((row+1, col))
            if col>=1 and int(grid[row][col-1])==value+1:
                to_see.add((row, col-1))
            if col<=col_num-2 and int(grid[row][col+1])==value+1:
                to_see.add((row, col+1))

    return len(reachable)

total=0

for row in range(row_num):
    for col in range(col_num):
        if grid[row][col]=='0':
            # print(row, col)
            total += find_reachable_peaks((row, col))
            # print(find_hiking_trails((row, col)))

print(f"Totale hiking trails parte 1: {total}")

#########################

def find_hiking_trails(start):
    totale=0
    to_see=[start]
    while len(to_see)>0:

        # print(to_see)
        row,col = to_see.pop()
        value = int(grid[row][col])
        if value==9:
            totale+=1
        else:
            if row>=1 and int(grid[row-1][col])==value+1:
                to_see.append((row-1, col))
            if row<=row_num-2 and int(grid[row+1][col])==value+1:
                to_see.append((row+1, col))
            if col>=1 and int(grid[row][col-1])==value+1:
                to_see.append((row, col-1))
            if col<=col_num-2 and int(grid[row][col+1])==value+1:
                to_see.append((row, col+1))

    return totale


total=0

for row in range(row_num):
    for col in range(col_num):
        if grid[row][col]=='0':
            # print(row, col)
            total += find_hiking_trails((row, col))
            # print(find_hiking_trails((row, col)))

print(f"Totale hiking trails parte 2: {total}")
