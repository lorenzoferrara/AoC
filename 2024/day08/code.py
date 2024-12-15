import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

with open("input.txt", "r") as file:
# with open("example.txt", "r") as file:
    lines = file.readlines()

grid=[]
coords=dict()
for line in lines:
    grid.append(list(line.strip()))
    # letters.update(line.strip())
# letters.remove('.')

row_num=len(grid)
col_num=len(grid[0])

for row in range(row_num):
    for col in range(col_num):
        lettera = grid[row][col]
        if lettera != '.':
            if lettera in coords:
                coords[lettera].append((row,col))
            else:
                coords[lettera] = [(row,col)]

antinodes=set()

def find_antinodes(pair):
    p_high=np.array(pair[0])
    p_low=np.array(pair[1])
    diff = p_high - p_low
    result=set()
    p_lowlow = p_low - diff
    if 0<=p_lowlow[0]<row_num and 0<=p_lowlow[1]<col_num:
        result.add(tuple(p_lowlow))
    p_highhigh = p_high + diff
    if 0<=p_highhigh[0]<row_num and 0<=p_highhigh[1]<col_num:
        result.add(tuple(p_highhigh))

    return result


for lettera in coords:
    pairs = list(combinations(coords[lettera], 2))

    for pair in pairs:
        antinodes.update(find_antinodes(pair))


print(f"NUmber of antinodes: {len(antinodes)}")


###########################

def find_resonant_antinodes(pair):

    result=set()
    result.add(pair[0])
    result.add(pair[1])

    p_high=np.array(pair[0])
    p_low=np.array(pair[1])
    diff = p_high - p_low

    p_lowlow = p_low - diff
    while 0<=p_lowlow[0]<row_num and 0<=p_lowlow[1]<col_num:
        result.add(tuple(p_lowlow))
        p_lowlow -= diff

    p_highhigh = p_high + diff
    while 0<=p_highhigh[0]<row_num and 0<=p_highhigh[1]<col_num:
        result.add(tuple(p_highhigh))
        p_highhigh += diff

    return result


for lettera in coords:
    pairs = list(combinations(coords[lettera], 2))

    for pair in pairs:
        antinodes.update(find_resonant_antinodes(pair))


print(f"NUmber of antinodes: {len(antinodes)}")

