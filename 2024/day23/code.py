import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

type='input'
# type='example'

with open(type+'.txt', 'r') as file:
    lines = file.readlines()

connections=dict()

for line in lines:
    first,second = line.strip().split('-')

    if first not in connections:
        connections[first]=[second]
    else:
        connections[first].append(second)
    if second not in connections:
        connections[second]=[first]
    else:
        connections[second].append(first)

# for pc in connections:
#     print(pc, connections[pc])

def is_group_connected(group):
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            if group[j] not in connections[group[i]]:
                return False
    return True


ok_groups=set()

for pc, connected_pcs in connections.items():
    if pc[0]=='t':
        new_set = set(connected_pcs)

        coppie = list(combinations(new_set, 2))

        for coppia in coppie:
            trio = coppia + tuple([pc])
            # print(trio)
            if is_group_connected(trio):
                ok_groups.add(tuple(sorted(trio)))

print(f'Total: {len(ok_groups)}\n') 

#####################################################


groups_found = True

rank=2
while groups_found:

    print(f'Current rank: {rank}')
    
    ok_groups=set()

    found_a_group = False
    for pc, connected_pcs in connections.items():

        if not found_a_group:
            new_set = set(connected_pcs)
            new_set.add(pc)

            groups = list(combinations(new_set, rank))

            for group in groups:
                if is_group_connected(group):
                    ok_groups.add(tuple(sorted(group)))
                    found_a_group = True

    if len(ok_groups)>0:
        max_ok_groups = ok_groups
        rank += 1
    else:
        groups_found = False

        print(f'Max rank: {rank-1}, group: {max_ok_groups}')

lista = max_ok_groups.pop()

print(f'Final code: {','.join(lista)}')

