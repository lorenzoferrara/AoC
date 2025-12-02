import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

type='input'
# type='example'

with open(type+'.txt', 'r') as file:
    lines = file.readlines()

locks=[]
keys=[]

ind=0
while ind < len(lines):
    shape=[]
    for col in range(5):
        shape.append(len([line[col] for line in lines[(ind+1):(ind+6)] if line[col]=='#']))

    if lines[ind][0]=='#':
        locks.append(shape)
    else:
        keys.append(shape)

    ind+=8

def check_fit(lock, key):

    for i in range(5):
        if lock[i]+key[i]>5:
            return False
    return True

total=0
for lock in locks:
    for key in keys:
        if check_fit(lock, key):
            total+=1

print(f'Total fitting pairs: {total}')
