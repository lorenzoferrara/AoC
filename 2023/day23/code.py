
import numpy as np
from typing import List
import copy


# PART 1

with open("input.txt", "r") as file:
# with open("example.txt", "r") as file:
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



to_visit=[[start]]
max_length=0

while len(to_visit)>0:

	temp_grid=copy.deepcopy(grid)
	chain=to_visit.pop()
	# print(chain)
	for point in chain[:-1]:
		temp_grid[point[0]][point[1]]='O'
	row,col=chain[-1]

	if [row,col]==end:
		max_length = max(max_length, len(chain)-1)
		print_grid('---')
		print_grid(temp_grid)
	else:
		if temp_grid[row][col]=='.':
			if row>0 and temp_grid[row-1][col] not in ['#', 'O']:
				to_visit.append(chain+[[row-1, col]])
			if col>0 and temp_grid[row][col-1] not in ['#', 'O']:
				to_visit.append(chain+[[row, col-1]])
			if row<row_num-1 and temp_grid[row+1][col] not in ['#', 'O']:
				to_visit.append(chain+[[row+1, col]])
			if col<col_num-1 and temp_grid[row][col+1] not in ['#', 'O']:
				to_visit.append(chain+[[row, col+1]])
		elif temp_grid[row][col]=='>':
			if temp_grid[row][col+1] not in ['#', 'O']:
				to_visit.append(chain+[[row, col+1]])
		elif temp_grid[row][col]=='<':
			if temp_grid[row][col-1] not in ['#', 'O']:
				to_visit.append(chain+[[row, col-1]])
		elif temp_grid[row][col]=='v':
			if temp_grid[row+1][col] not in ['#', 'O']:
				to_visit.append(chain+[[row+1, col]])
		elif temp_grid[row][col]=='^':
			if temp_grid[row-1][col] not in ['#', 'O']:
				to_visit.append(chain+[[row-1, col]])
		else:
			raise ValueError(f"In {row},{col} vale: {temp_grid[row][col]}")

	# temp_grid[row][col]='O'


print(max_length)






