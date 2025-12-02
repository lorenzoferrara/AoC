import numpy as np
import pandas as pd
import re
import copy
import time
from pydantic.dataclasses import dataclass
from typing import List, Tuple

type = "input"
# type='example'
# type='example_1'

with open(type + ".txt", "r") as file:
    lines = file.readlines()

M = 1e6
map_grid=[]

grid = []
for row, line in enumerate(lines):
    map_grid.append(list(line.strip()))

    new_line=[]
    for cell in list(line.strip()):
        if cell == '#':
            new_line.append({'v':-M, 'h':-M})
        else:
            new_line.append({'v': M, 'h': M})

    grid.append(new_line)
    if "S" in line:
        start = (row, line.index("S"))
    if "E" in line:
        end = (row, line.index("E"))

row_num = len(grid)
col_num = len(grid[0])

grid[start[0]][start[1]]={'v':1000, 'h': 0} #vertical, horizontal
to_see = {start}

while to_see:
    elem = to_see.pop()
    row, col = elem

    if (row, col)==end:
        continue
    else:
        for new_row in [row-1, row+1]:
            if grid[new_row][col]['v'] > grid[row][col]['v']+1 :
                grid[new_row][col]['v'] = grid[row][col]['v']+1
                grid[new_row][col]['h'] = grid[row][col]['v']+1001
                to_see.add((new_row,col))
            if grid[new_row][col]['v'] > grid[row][col]['h']+1001 :
                grid[new_row][col]['v'] = grid[row][col]['v']+1
                grid[new_row][col]['h'] = grid[row][col]['v']+1001
                to_see.add((new_row,col))
        for new_col in [col-1, col+1]:
            if grid[row][new_col]['h'] > grid[row][col]['h']+1 :
                grid[row][new_col]['h'] = grid[row][col]['h']+1
                grid[row][new_col]['v'] = grid[row][col]['h']+1001
                to_see.add((row,new_col))
            if grid[row][new_col]['h'] > grid[row][col]['v']+1001 :
                grid[row][new_col]['h'] = grid[row][col]['h']+1
                grid[row][new_col]['v'] = grid[row][col]['h']+1001
                to_see.add((row,new_col))


if grid[end[0]][end[1]]['v'] > grid[end[0]][end[1]]['h']:
    shortest_dir = 'h'
else:
    shortest_dir = 'v'

print(f"Shortest path part 1: {grid[end[0]][end[1]][shortest_dir]}, {shortest_dir}\n")


########################################################################################

seen=set()
to_see = {end}

if type=='example_1' or type=='input':
    grid[end[0]][end[1]-1]['v']=0
    grid[end[0]][end[1]-1]['h']=0

while to_see:
    elem = to_see.pop()
    row, col = elem

    # if abs(grid[new_row][col]['v']-grid[new_row][col]['h'])==1000:
    seen.add(elem)

    if (row, col)==start:
        continue
    else:
        for new_row in [row-1, row+1]:
            if grid[new_row][col]['v'] == grid[row][col]['v']-1 :
                to_see.add((new_row,col))
            if grid[new_row][col]['h'] == grid[row][col]['h']-1001 and \
            grid[new_row][col]['v']-1000 == grid[new_row][col]['h']:
                to_see.add((new_row,col))
        for new_col in [col-1, col+1]:
            
            if grid[row][new_col]['h'] == grid[row][col]['h']-1 :
                to_see.add((row,new_col))
            if grid[row][new_col]['h'] == grid[row][col]['v']-1001 and\
            grid[row][new_col]['h']-1000 == grid[row][new_col]['v']:
                to_see.add((row,new_col))


for cella in seen:
    if map_grid[cella[0]][cella[1]] not in ['S', 'E']:
        map_grid[cella[0]][cella[1]]='O'

texts = []
with open(f"output_{type}.show", "w") as file:
    for row in map_grid:
        texts.append(''.join(row))
    final_text='\n'.join(texts)
    # print(final_text)
    file.write(final_text)


print(f"Number of cells part 2: {len(seen)}\n")



def pr(i,j):
    print(f'riga {i}, col {j}: {grid[i][j]}')
pr(-5, 45)
pr(-4, 45)
pr(-4, 44)

for i in range(37,44):
    pr(-10, i)

for i in range(-10, -4):
    pr(i, 41)

for i in range(69,72):
    pr(-4, i)

########################################################################################

# percorsi_corretti=[]

# lista_percorsi = [[start]]

# if type=='example_1' or type=='input':
#     grid[end[0]][end[1]-1]['v']=0
#     grid[end[0]][end[1]-1]['h']=0

# while lista_percorsi:
#     percorso = lista_percorsi.pop(0)
#     print(len(lista_percorsi), end='\r')
#     row, col = percorso[-1]

#     if (row, col)==end:
#         percorsi_corretti.extend(percorso)
#     else:
#         for new_row in [row-1, row+1]:
#             if grid[new_row][col]['v'] == grid[row][col]['v']+1 :
#                 lista_percorsi.append(percorso+[(new_row,col)])
#             if grid[new_row][col]['v'] == grid[row][col]['h']+1001 :
#                 lista_percorsi.append(percorso+[(new_row,col)])
#         for new_col in [col-1, col+1]:
#             if grid[row][new_col]['h'] == grid[row][col]['h']+1 :
#                 lista_percorsi.append(percorso+[(row,new_col)])
#             if grid[row][new_col]['h'] == grid[row][col]['v']+1001 :
#                 lista_percorsi.append(percorso+[(row,new_col)])

# set_celle = set(percorsi_corretti)
# print(f"Shortest path part 1: {len(set_celle)}\n")

# for cella in set_celle:
#     if map_grid[cella[0]][cella[1]] not in ['S', 'E']:
#         map_grid[cella[0]][cella[1]]='O'

# texts = []
# for row in map_grid:
#     texts.append(''.join(row))
# final_text='\n'.join(texts)
# print(final_text)

