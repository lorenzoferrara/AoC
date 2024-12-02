
import numpy as np
from typing import List


# PART 1

with open("example.txt", "r") as file:
	lines = file.readlines()

max_vec=[0,0,0]

for line in lines:
	parte1, parte2 = line.split('~')
	parte1=parte1.split(',')
	parte2=parte2.split(',')
	for i in range(3):
		max_vec[i]=max(int(parte1[i]), max_vec[i])
		max_vec[i]=max(int(parte2[i]), max_vec[i])

pieces_per_level = dict()
for i in range(1, max_vec[2]):
	pieces_per_level[i] = []

def find_pieces_levels(parte1: List[int], parte2: List[int]):
	x1,y1,z1=parte1
	x2,y2,z2=parte2

	if x1==x2:
		if y1==y2:
			z_max = max(z1, z2)
			z_min = min(z1, z2)
			return [[x1,y1,z] for z in range(z_min, z_max+1)], z_min
		
		#qui avro z1=z2 e y diverse
		y_max = max(y1, y2)
		y_min = min(y1, y2)
		return [[x1,y,z1] for y in range(y_min, y_max+1)], z1
		
	#qui avro z1=z2,y1=y2 e x diverse
	x_max = max(x1, x2)
	x_min = min(x1, x2)
	return [[x,y1,z1] for x in range(x_min, x_max+1)], z1

pieces = dict()

for ind,line in enumerate(lines):

	parts = line.split('~')
	for j, part in enumerate(parts):
		parts[j] = [int(i) for i in part.split(',')]

	pieces[ind], level = find_pieces_levels(parts[0], parts[1])

	pieces_per_level[level].append(ind)

print(pieces_per_level)

##### PIECES FALL

#al liv 0 c'è il suolo, chi è al 1 non puo cadere, è ia al suolo
# parto dal livello 2 e li facico cadere controllando se sotto c'è qualcosa
for z_level in range(2, max_vec[2]):
	for piece_num in pieces_per_level[z_level]:
		for cube in pieces[piece_num]:
			



# table_xz = [['.' for _ in range(max_z)] for _ in range(max_x)]
# table_yz = [['.' for _ in range(max_z)] for _ in range(max_y)]

# for line in lines:
# 	punti = find_coord(line[0], line[4], line[6], line[-1])
# 	for punto in punti:
# 		table_xz[punto[0], punto[1]]=




###########################################

# # PART 2

# file = open("example.txt", "r")
# file = open("input.txt", "r")

# content = file.read()
# lines = file.readlines()

# file.close()
