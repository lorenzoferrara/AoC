import numpy as np
import pandas as pd
import re
import copy

with open("input.txt", "r") as file:
# with open("example.txt", "r") as file:
    lines = file.readlines()

######################### PART 1

def print_grid(name='grid', file=None):

    if file is not None:
        grid=file

    texts = []
    for row in grid:
        texts.append("".join([i for i in row]))
    final_text="\n".join(texts)
    print(final_text)

grid=[]
for ind,line in enumerate(lines):
    if '^' in line:
        cur=np.array([ind,line.index('^')])
    grid.append(list(line.strip()))

grid[cur[0]][cur[1]]='X'
row_num=len(grid)
col_num=len(grid[0])

direc='U' #goes upwards

change_dir = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}
dir_to_coord = {'U': [-1,0], 'R':[0,1], 'D':[1,0], 'L':[0,-1]}

blocked=False
while not blocked:
    next_pos = cur + dir_to_coord[direc]
    if next_pos[0] in [row_num, -1] or next_pos[1] in [col_num, -1]:
        blocked=True
    else:
        if grid[next_pos[0]][next_pos[1]] == '#':
            direc = change_dir[direc]
        else:
            cur = next_pos
            grid[cur[0]][cur[1]] = 'X'




    # with open(name+".show", "w") as file:
    #     file.write(final_text)

# print_grid()

totale=0
for row in grid:
    for letter in row:
        if letter == 'X':
            totale += 1
print(f"Number of touched cells: {totale}")

########################## part 2


change_dir = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}
dir_to_coord = {'U': [-1,0], 'R':[0,1], 'D':[1,0], 'L':[0,-1]}
dir_to_line = {'U': '^', 'R':'>', 'D':'v', 'L':'<'}

direc='U' #goes upwards

grid=[]
for ind,line in enumerate(lines):
    if '^' in line:
        cur=np.array([ind,line.index('^')])
    grid.append(list(line.strip()))

row_num=len(grid)
col_num=len(grid[0])

new_obstacles=[]

blocked=False
while not blocked:
    next_pos = cur + dir_to_coord[direc]
    if next_pos[0] in [row_num, -1] or next_pos[1] in [col_num, -1]:
        blocked=True
    else:
        if grid[next_pos[0]][next_pos[1]] == '#':
            direc = change_dir[direc]
        else:
            cur = next_pos
            if grid[cur[0]][cur[1]] == '.':
                grid[cur[0]][cur[1]] = dir_to_line[direc] #ogni cella contiene le direzioni prese finora
            else:
                grid[cur[0]][cur[1]] += dir_to_line[direc]

            # mi giro di colpo a destra e proseguo fino a che non trovo muro o una cella percorsa con la stessa direzione
            new_dir = change_dir[direc]
            temp_cur = copy.deepcopy(cur)
            found=False
            while not found and temp_cur[0] not in [row_num, -1] \
                    and temp_cur[1] not in [col_num, -1] \
                    and grid[temp_cur[0]][temp_cur[1]] != '#':
                if dir_to_line[new_dir] in grid[temp_cur[0]][temp_cur[1]]:
                    found=True
                temp_cur += dir_to_coord[new_dir]
            if found:
                new_obstacles.append(tuple(cur+dir_to_coord[direc]))

print(f"Possible new obstacles: {len(new_obstacles)}")

# print_grid()




########################## part 2 con brute force


change_dir = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}
dir_to_coord = {'U': [-1,0], 'R':[0,1], 'D':[1,0], 'L':[0,-1]}
dir_to_line = {'U': '^', 'R':'>', 'D':'v', 'L':'<'}

direc='U' #goes upwards

grid=[]
for ind,line in enumerate(lines):
    if '^' in line:
        start_cur=np.array([ind,line.index('^')])
    grid.append(list(line.strip()))

row_num=len(grid)
col_num=len(grid[0])

new_obstacles=[]

for row in range(row_num):
    print(f"{row}/{row_num}", end='\r')
    for col in range(col_num):
        if grid[row][col] not in ['#','^']:
            new_grid = copy.deepcopy(grid)
            new_grid[row][col]='#'

            blocked=False
            loop=False

            direc='U'
            cur=copy.deepcopy(start_cur)
            
            while not blocked and not loop:
                next_pos = cur + dir_to_coord[direc]
                if next_pos[0] in [row_num, -1] or next_pos[1] in [col_num, -1]:
                    blocked=True
                    # print('0:fuori')

                elif dir_to_line[direc] in new_grid[next_pos[0]][next_pos[1]]:
                    loop=True
                    # print('1:loop')

                else:
                    # print('2:mi muovo')
                    if new_grid[next_pos[0]][next_pos[1]] == '#':
                        direc = change_dir[direc]
                        # print('mi giro')
                    else:
                        # print('continuo')
                        cur = next_pos
                        if new_grid[cur[0]][cur[1]] == '.':
                            new_grid[cur[0]][cur[1]] = dir_to_line[direc] #ogni cella contiene le direzioni prese finora
                        else:
                            new_grid[cur[0]][cur[1]] += dir_to_line[direc]

            if loop:
                new_obstacles.append((row,col))
            
            # print_grid(file=new_grid)
            # print()


print(f"Possible new obstacles with brute force: {len(new_obstacles)}")

# print_grid(file=new_grid)


