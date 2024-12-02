
import numpy as np
from typing import List
import copy


# PART 1

with open("input.txt", "r") as file:
# with open("example.txt", "r") as file:
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
for i in range(1, max_vec[2]+1):
	pieces_per_level[i] = np.zeros((max_vec[0]+1, max_vec[1]+1))
	# anche i valori=0 sono ammissibili come coordinate per x e y


def fill_map(parte1: List[int], parte2: List[int], piece_num: int):
	x1,y1,z1=parte1
	x2,y2,z2=parte2

	if x1==x2:
		if y1==y2:
			z_max = max(z1, z2)
			z_min = min(z1, z2)
			for z in range(z_min, z_max+1):
				pieces_per_level[z][x1, y1] = piece_num
			return [[x1,y1,z] for z in range(z_min, z_max+1)], True
		
		else:
			#qui avro z1=z2 e y diverse
			y_max = max(y1, y2)
			y_min = min(y1, y2)
			for y in range(y_min, y_max+1):
				pieces_per_level[z1][x1, y] = piece_num
			return [[x1,y,z1] for y in range(y_min, y_max+1)], False

	else:
		#qui avro z1=z2,y1=y2 e x diverse
		x_max = max(x1, x2)
		x_min = min(x1, x2)
		for x in range(x_min, x_max+1):
			pieces_per_level[z1][x, y1] = piece_num
		return [[x,y1,z1] for x in range(x_min, x_max+1)], False


pieces = dict()
vertical = dict()

for ind,line in enumerate(lines):

	parts = line.split('~')
	for j, part in enumerate(parts):
		parts[j] = [int(i) for i in part.split(',')]

	pieces[ind+1], vertical[ind+1] = fill_map(parts[0], parts[1], ind+1)

for i in pieces_per_level:
	print(i, "\n", pieces_per_level[i])

##### PIECES FALL
def libero_sotto(piece_num: int, map3d=None, lista_pezzi=None):

	steps=0

	if map3d is None:
		map3d=pieces_per_level

	if lista_pezzi is None:
		lista_pezzi=pieces

	min_z = lista_pezzi[piece_num][0][2]

	if vertical[piece_num]:
		block = lista_pezzi[piece_num][0] #guardo solo il pezzo piu in basso
		while min_z-1-steps>0:
			if map3d[block[2]-1-steps][block[0], block[1]] != 0:
				return steps
			steps+=1
		return steps

	else:
		while min_z-1-steps>0:
			for block in lista_pezzi[piece_num]:
				if map3d[block[2]-1-steps][block[0], block[1]] != 0:
					return steps
			steps+=1
		return steps

def apply_caduta(piece_num: int, steps: int, map3d=None, lista_pezzi=None):

	if map3d is None:
		map3d=pieces_per_level

	if lista_pezzi is None:
		lista_pezzi=pieces

	for ind,block in enumerate(lista_pezzi[piece_num]):
		lista_pezzi[piece_num][ind] = [block[0], block[1], block[2]-steps]
		map3d[block[2]][block[0], block[1]]=0
		map3d[block[2]-steps][block[0], block[1]]=piece_num


#al liv 0 c'è il suolo, chi è al 1 non puo cadere, è ia al suolo
# parto dal livello 2 e li facico cadere controllando se sotto c'è qualcosa
for z_level in range(2, max_vec[2]+1):
	list_of_pieces = np.unique(pieces_per_level[z_level])
	for piece_num in list_of_pieces:
		if piece_num!=0:
			steps = libero_sotto(piece_num)
			# print(f"pezzo: {piece_num}, steps: {steps}")
			if steps>0:
				apply_caduta(piece_num, steps)

for i in pieces_per_level:
	print(i, "\n", pieces_per_level[i])

def is_stable(piece_target: int):
	new_pieces_per_level = copy.deepcopy(pieces_per_level)
	for block in pieces[piece_target]:
		new_pieces_per_level[block[2]][block[0],block[1]]=0

	for z_level in range(2, max_vec[2]+1):
		list_of_pieces = np.unique(new_pieces_per_level[z_level])
		for piece_num in list_of_pieces:
			if piece_num!=0:
				steps = libero_sotto(piece_num, new_pieces_per_level)
				if steps>0:
					return False
	return True




total=0
for piece_num in pieces.keys():
	if is_stable(piece_num):
		# print(f"{piece_num} stable")
		total += 1
	# else:
		# print(f"{piece_num} not stable")


print(f"total stables: {total}")


##############

def how_many_fall(piece_target: int):

	tot_fallen=set()

	new_pieces_per_level = copy.deepcopy(pieces_per_level)
	new_pieces = copy.deepcopy(pieces)

	for block in new_pieces[piece_target]:
		new_pieces_per_level[block[2]][block[0],block[1]]=0

	for z_level in range(block[2]+1, max_vec[2]+1):
		list_of_pieces = np.unique(new_pieces_per_level[z_level])
		for piece_num in list_of_pieces:
			if piece_num!=0:
				steps = libero_sotto(piece_num, new_pieces_per_level, new_pieces)
				if steps>0:
					tot_fallen.add(piece_num)
					apply_caduta(piece_num, steps, new_pieces_per_level, new_pieces)

	return len(tot_fallen)

total=0
for piece_num in pieces.keys():
	total += how_many_fall(piece_num)

print(f"total reaction chain: {total}")