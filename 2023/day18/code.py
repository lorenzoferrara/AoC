
import numpy as np
import copy
import re

# PART 1

# with open("example.txt", "r") as file:
with open("input.txt", "r") as file:
	lines = file.readlines()

convert=dict()
convert['U']=[-1,0]
convert['D']=[1,0]
convert['L']=[0,-1]
convert['R']=[0,1]

cur=[0,0]
points=[copy.deepcopy(cur)]

for line in lines:
	direc = line.split()[0]
	step_num = int(line.split()[1])
	change = convert[direc]
	for step in range(step_num):
		cur[0] += change[0]
		cur[1] += change[1]
		points.append(copy.deepcopy(cur))

points=np.array(points)

minima = np.min(points, axis=0)
points[:,0] -= minima[0]
points[:,1] -= minima[1]

row_num, col_num=np.max(points, axis=0)+1
grid=np.zeros((row_num, col_num))
for row,col in points:
	grid[row,col]=1

def flood_fill(start):
	
	pieno=0
	vuoto=1-pieno

	if grid[start[0], start[1]]==vuoto:

		da_riempire={tuple(start)}

		while len(da_riempire)>0:

			row,col = da_riempire.pop()
			grid[row, col]=pieno

			if row_num-1>row and grid[row+1, col]==vuoto:
				da_riempire.add((row+1, col))
			if row>=1 and grid[row-1, col]==vuoto:
				da_riempire.add((row-1, col))
			if col_num-1>col and grid[row, col+1]==vuoto:
				da_riempire.add((row, col+1))
			if col>=1 and grid[row, col-1]==vuoto:
				da_riempire.add((row, col-1))

def print_grid(name):

	texts = []
	for row in grid:
		texts.append("".join([str(int(i)) for i in row]))
	final_text="\n".join(texts)
	final_text = re.sub('0', '.', final_text)
	final_text = re.sub('1', '#', final_text)
	# print(final_text)

	with open(name+".show", "w") as file:
	    file.write(final_text)


print_grid('pre')

len_bordo = np.sum(grid)

# inverto i valori
grid = 1- grid

# riempio l'esterno
for row in range(row_num):
	flood_fill([row, 0])
	flood_fill([row, col_num-1])
for col in range(col_num):
	flood_fill([0, col])
	flood_fill([row_num-1, col])

print_grid('post')

print(f"Area of the polygon: {np.sum(grid)+len_bordo}")


###########################################

# PART 2

cur=[0,0]
vertices=[copy.deepcopy(cur)]
sides=[]

num_to_dir=dict()
num_to_dir['0']='R'
num_to_dir['1']='D'
num_to_dir['2']='L'
num_to_dir['3']='U'

for line in lines:
	codice = line.split('#')[1]
	codice = re.sub('\n', '', codice)
	if len(codice[:-2])!=5:
		raise ValueError
	direc = num_to_dir[codice[-2]]
	step_num = int(codice[:-2], 16)
	sides.append(step_num)
	change = convert[direc]
	cur[0] += change[0]*step_num
	cur[1] += change[1]*step_num
	# if past_direc = 
	# vert_x = 
	vertices.append(copy.deepcopy(cur))
	past_direc = direc

vertices=vertices[:-1]

perimetro = np.sum(sides)

def polygon_area(vertices):
    n = len(vertices)  # Number of vertices
    area = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1)%n]  # Wrap around to the first vertex
        area += x1 * y2 - y1 * x2

    return abs(area) / 2

area = polygon_area(vertices)
print(f"Area of the polygon: {area+perimetro/2+1}")
