
import numpy as np

# PART 1

file = open("example.txt", "r")
# file = open("input.txt", "r")

content = file.read()
lines = content.split('/n')

max_x=0
max_y=0
max_z=0

def find_coord(x1, z1, x2, z2):
	if x1==x2:
		if z1==z2:
			return [[x1, z1]]
		elif z1<z2:
			return [[x1,z] for z in range(z1, z2+1)]
		else:
			return [[x1,z] for z in range(z2, z1+1)]
	elif x1<x2:
		return [[x,z1] for x in range(x1, x2+1)]
	else:
		return [[x,z1] for x in range(x2, x1+1)]


for line in lines:
	max_x=max(max_x, int(line[-5]))
	max_y=max(max_y, int(line[-3]))
	max_z=max(max_z, int(line[-1]))

table_xz = [['.' for _ in range(max_z)] for _ in range(max_x)]
table_yz = [['.' for _ in range(max_z)] for _ in range(max_y)]

for line in lines:
	punti = find_coord(line[0], line[4], line[6], line[-1])
	for punto in punti:
		table_xz[punto[0], punto[1]]=




###########################################

# # PART 2

# file = open("example.txt", "r")
# file = open("input.txt", "r")

# content = file.read()
# lines = file.readlines()

# file.close()
