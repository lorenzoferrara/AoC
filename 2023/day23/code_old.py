
import numpy as np
from typing import List
import copy


# PART 1

# with open("input.txt", "r") as file:
with open("example.txt", "r") as file:
	lines = file.readlines()

grid=[]
for line in lines:
	grid.append(list(line))

start=[0,1]
row_num=len(grid)
col_num=len(grid)
end=[row_num-1, col_num-2]

def print_grid(grid):

	texts = []
	for row in grid:
		texts.append("".join([str(i) for i in row]))
	final_text="\n".join(texts)
	print(final_text)


def find_longest_path(point, grid):

	if point==end:
		return 0

	row,col=point
	options=[]

	max_length=0

	if grid[row][col]=='.':
		if row>0 and grid[row-1][col] not in ['#', 'O']:
			options.append([row-1, col])
		if col>0 and grid[row][col-1] not in ['#', 'O']:
			options.append([row, col-1])
		if row<row_num-1 and grid[row+1][col] not in ['#', 'O']:
			options.append([row+1, col])
		if col<col_num-1 and grid[row][col+1] not in ['#', 'O']:
			options.append([row, col+1])
	elif grid[row][col]=='>':
		if grid[row][col+1] not in ['#', 'O']:
			options.append([row, col+1])
	elif grid[row][col]=='<':
		if grid[row][col-1] not in ['#', 'O']:
			options.append([row, col-1])
	elif grid[row][col]=='v':
		if grid[row+1][col] not in ['#', 'O']:
			options.append([row+1, col])
	elif grid[row][col]=='^':
		if grid[row-1][col] not in ['#', 'O']:
			options.append([row-1, col])
	else:
		raise ValueError(f"In {row},{col} vale: {grid[row][col]}")

	if len(options)==0:
		# print('---------------------------------')
		# print_grid(grid)
		return None

	grid[row][col]='O'

	for option in options:
		path_length=find_longest_path(option, copy.deepcopy(grid))
		if path_length is not None:
			max_length=max(max_length, path_length)

	return 1 + max_length

longest_path = find_longest_path(start, copy.deepcopy(grid))

print(longest_path)






