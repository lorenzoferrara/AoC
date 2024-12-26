import numpy as np
import pandas as pd
import re
import copy
import time

type = "input"
type = "example"
type = "example_1"

with open(type + ".txt", "r") as file:
    lines = file.readlines()

grid = []
mosse = []
for row, line in enumerate(lines):
    if line[0] == "#":
        grid.append(list(line.strip()))
        if "@" in line:
            cur = np.array([row, line.index("@")])

    elif len(line) > 2:
        mosse += list(line.strip())

row_num = len(grid)
col_num = len(grid[0])

dir_to_coord = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def print_grid(grid):

    texts = []
    for row in grid:
        texts.append("".join(row))
    final_text = "\n".join(texts)
    print(final_text)


for mossa in mosse:
    vect = np.array(dir_to_coord[mossa])
    # print(mossa, vect, cur)
    temp_cur = copy.deepcopy(cur)
    while grid[temp_cur[0]][temp_cur[1]] not in ["#", "."]:
        temp_cur += vect

    # sono finito contro un muro senza trovare buchi liberi
    # print('mossa:', mossa, 'cur:', cur, 'grid[cur[0]][cur[1]]', grid[cur[0]][cur[1]])
    if grid[temp_cur[0]][temp_cur[1]] != "#":
        cur = temp_cur
        # torno indietro finchè non ritrovo il robot iniziale
        found = False
        while not found:
            next_pos = cur - vect
            # print(next_pos, grid[next_pos[0]][next_pos[1]])
            if grid[next_pos[0]][next_pos[1]] == "@":
                found = True
            grid[cur[0]][cur[1]] = grid[next_pos[0]][next_pos[1]]
            grid[next_pos[0]][next_pos[1]] = "."
            cur -= vect
        cur += vect

    # print('Move', mossa)
    # print_grid(grid)
    # print()


total_distance = 0
for row in range(row_num):
    for col in range(col_num):
        if grid[row][col] == "O":
            total_distance += 100 * row + col

print(f"Total distance part 1: {total_distance}\n")

##############################################################

new_grid = []
mosse = []
for row, line in enumerate(lines):
    if line[0] == "#":
        new_line = re.sub("#", "##", line)
        new_line = re.sub("O", "[]", new_line)
        new_grid.append(list(new_line.strip()))
        if "@" in line:
            cur = np.array([row, line.index("@")])

    elif len(line) > 2:
        mosse += list(line.strip())

row_num = len(new_grid)
col_num = len(new_grid[0])

dir_to_coord = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def can_move(grid, start, mossa):

    vect = np.array(dir_to_coord[mossa])
    to_see = set([start])

    while to_see:
        cur = to_see.pop()
        next_pos = cur + vect
        if grid[next_pos[0]][next_pos[1]] == "[":
            to_see.add(next_pos)
            to_see.add(next_pos + np.array((0, 1)))
        if grid[next_pos[0]][next_pos[1]] == "]":
            to_see.add(next_pos)
            to_see.add(next_pos - np.array((0, 1)))
        if grid[next_pos[0]][next_pos[1]] == "#":
            return False


for mossa in mosse:
    vect = np.array(dir_to_coord[mossa])
    # print(mossa, vect, cur)
    temp_cur = copy.deepcopy(cur)

    if mossa in ["<", ">"]:
        while new_grid[temp_cur[0]][temp_cur[1]] not in ["#", "."]:
            temp_cur += vect

        # sono finito contro un muro senza trovare buchi liberi
        # print('mossa:', mossa, 'cur:', cur, 'new_grid[cur[0]][cur[1]]', new_grid[cur[0]][cur[1]])
        if new_grid[temp_cur[0]][temp_cur[1]] != "#":
            cur = temp_cur
            # torno indietro finchè non ritrovo il robot iniziale
            found = False
            while not found:
                next_pos = cur - vect
                # print(next_pos, new_grid[next_pos[0]][next_pos[1]])
                if new_grid[next_pos[0]][next_pos[1]] == "@":
                    found = True
                new_grid[cur[0]][cur[1]] = new_grid[next_pos[0]][next_pos[1]]
                new_grid[next_pos[0]][next_pos[1]] = "."
                cur -= vect
            cur += vect
    else:
        pass

    # print('Move', mossa)
    # print_grid(new_grid)
    # print()


total_distance = 0
for row in range(row_num):
    for col in range(col_num):
        if new_grid[row][col] == "O":
            total_distance += 100 * row + col

print(f"Total distance part 1: {total_distance}\n")
