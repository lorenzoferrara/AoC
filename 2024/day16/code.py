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

grid = []
for row, line in enumerate(lines):
    grid.append(list(line.strip()))
    if "S" in line:
        start = (row, line.index("S"))
    if "E" in line:
        end = (row, line.index("E"))

row_num = len(grid)
col_num = len(grid[0])

dir_to_coord = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

score = 0
# score, position, direction
percorsi_da_seguire = [[score, start, "<"]]

minimum_length = np.inf

while len(percorsi_da_seguire) > 0:
    p = percorsi_da_seguire.pop()
    row, col = p[1]
    d = np.abs(row - end[0]) + np.abs(col - end[1])

    print(f"percorsi: {len(percorsi_da_seguire)}, dist: {d}", end="\r")

    if grid[row][col] == "E":
        minimum_length = np.min([minimum_length, p[0]])
    else:
        grid[row][col] = p[0]
        for new_dir in ["^", ">", "v", "<"]:
            delta = dir_to_coord[new_dir]
            new_row = row + delta[0]
            new_col = col + delta[1]

            if grid[new_row][new_col] != "#":
                if p[2] == new_dir:
                    new_score = p[0] + 1
                else:
                    new_score = p[0] + 1001

                # potrei essere arrivato s una casella con meno score, ma con una direzione diversa, devo memorizza anche la direzione nella casella
                if (
                    grid[new_row][new_col] in [".", "E"]
                    or grid[new_row][new_col] > new_score
                ):
                    percorsi_da_seguire.append([new_score, (new_row, new_col), new_dir])


# def print_grid(grid):

#     texts = []
#     for row in grid:
#         texts.append(''.join(row))
#     final_text='\n'.join(texts)
#     print(final_text)

print()
print(f"Minimum distance part 1: {minimum_length}\n")
