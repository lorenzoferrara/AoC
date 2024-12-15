import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

# with open("input.txt", "r") as file:
with open("example.txt", "r") as file:
    lines = file.readlines()

grid=[]
for line in lines:
    grid.append(list(line.strip()))

row_num=len(grid)
col_num=len(grid[0])

# aree=[]
# perimetri=[]

total_price=0

for row in range(row_num):
    for col in range(col_num):
        value=grid[row][col]
        if value != '#':
            area=0
            perimetro=0
            to_see={(row,col)}
            while to_see:
                new_row, new_col=to_see.pop()
                grid[new_row][new_col]='#'
                area+=1
                perimetro+=4

                if 0<new_row and grid[new_row-1][new_col]==value:
                    to_see.add((new_row-1, new_col))
                    perimetro-=2
                if new_row<row_num-1 and grid[new_row+1][new_col]==value:
                    to_see.add((new_row+1, new_col))
                    perimetro-=2
                if 0<new_col and grid[new_row][new_col-1]==value:
                    to_see.add((new_row, new_col-1))
                    perimetro-=2
                if new_col<col_num-1 and grid[new_row][new_col+1]==value:
                    to_see.add((new_row, new_col+1))
                    perimetro-=2

            # print(f'{value}:{area}*{perimetro}={area*perimetro}')
            # aree.append(area)
            # perimetri.append(perimetro)
            total_price += area*perimetro


# total_price = np.sum([i*j for i,j in zip(aree, perimetri)])

print(f'Total price: {total_price}\n')

#########################

grid=[]
for line in lines:
    grid.append(list(line.strip()))

n_lati_list=[]

total_price=0

contatore=0

for row in range(row_num):
    for col in range(col_num):
        value=grid[row][col]
        if value > str(contatore):
            area=0
            n_lati=0
            to_see={(row,col)}
            while to_see:
                new_row, new_col=to_see.pop()
                grid[new_row][new_col]=str(contatore)
                area+=1
   
                confinanti=0
                direz_vuote=[1,2,3,4]

                if 0<new_row:
                    if grid[new_row-1][new_col]==value:
                        to_see.add((new_row-1, new_col))
                        direz_vuote.remove(1) #up
                    if grid[new_row-1][new_col]==str(contatore):
                        direz_vuote.remove(1) #up

                if new_col<col_num-1:
                    if grid[new_row][new_col+1]==value:
                        to_see.add((new_row, new_col+1))
                        direz_vuote.remove(2) #right
                    if grid[new_row][new_col+1]==str(contatore):
                        direz_vuote.remove(2) #right

                if new_row<row_num-1:
                    if grid[new_row+1][new_col]==value:
                        to_see.add((new_row+1, new_col))
                        direz_vuote.remove(3) #down
                    if grid[new_row+1][new_col]==str(contatore):
                        direz_vuote.remove(3) #down

                if 0<new_col:
                    if grid[new_row][new_col-1]==value:
                        to_see.add((new_row, new_col-1))
                        direz_vuote.remove(4) #left
                    if grid[new_row][new_col-1]==str(contatore):
                        direz_vuote.remove(4) #left


                if len(direz_vuote)>1:
                    diff = np.diff(direz_vuote)
                    print(f'({new_row},{new_col}), direz:', direz_vuote, 'diff', diff)
                    if 1 in diff or 3 in diff:
                        if 1 in direz_vuote and 2 in direz_vuote:
                            if new_row<row_num-1 and new_col>0\
                                and grid[new_row+1][new_col-1] in [value,str(contatore)]:
                                # angolo pieno
                                n_lati+=1
                            else:
                                #angolo vuoto
                                n_lati+=2
                        if 2 in direz_vuote and 3 in direz_vuote:
                            if new_row>0 and new_col>0\
                                and grid[new_row-1][new_col-1] in [value,str(contatore)]:
                                # angolo pieno
                                n_lati+=1
                            else:
                                #angolo vuoto
                                n_lati+=2
                        if 3 in direz_vuote and 4 in direz_vuote:
                            if new_row>0 and new_col<col_num-1\
                                and grid[new_row-1][new_col+1] in [value,str(contatore)]:
                                # angolo pieno
                                n_lati+=1
                            else:
                                #angolo vuoto
                                n_lati+=2
                        if 4 in direz_vuote and 1 in direz_vuote:
                            if new_row<row_num-1 and new_col<col_num-1\
                                and grid[new_row+1][new_col+1] in [value,str(contatore)]:
                                # angolo pieno
                                n_lati+=1
                            else:
                                #angolo vuoto
                                n_lati+=2
                else:
                    print(f'({new_row},{new_col}), direz:', direz_vuote)



                # print(confinanti)
                # if confinanti==2:
                #     n_lati+=1
                # if confinanti==1:
                #     n_lati+=1

            print(f'{value}:{area}*{n_lati}={area*n_lati}')
            total_price += area*n_lati

            contatore+=1
            print('contatore', contatore)

print(grid)

print(f'Total price: {total_price}')

