import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations
import functools

type='input'
# type='example'
# type='example2'

with open(type+'.txt', 'r') as file:
    lines = file.readlines()

wire_values=dict()

not_done=[]

@functools.lru_cache(maxsize=None)
def get_result_value(first, operand, second) -> bool:
    if operand=='AND':
        return wire_values[first] and wire_values[second]
    if operand=='OR':
        return  wire_values[first] or wire_values[second]
    if operand=='XOR':
        return wire_values[first] ^ wire_values[second]
    raise ValueError


# def check_connection(ind, switches):
#     line=lines[ind]
#     first, operand, second, _, result = line.strip().split() 
#     if first in wire_values and second in wire_values:
#         if switches is not None:
#             for pair in switches:
#                 if first in pair or 

#         wire_values[result] = get_result_value(first, operand, second)

table=[]
for ind,line in enumerate(lines):
    if len(line)==7:
        wire, value = line.strip().split(':')
        wire_values[wire]=int(value)
    elif len(line)>7:
        first, operand, second, _, result = line.strip().split() 
        table.append([first, operand, second, result])

def get_ordered_wire_values(table, switches=None):

    if switches is not None:
        # for pair in switches:
        #         if first in pair or
        pass
    else:
        new_table=table

    for ind,line in enumerate(new_table):
        first, operand, second, result = line
        if first in wire_values and second in wire_values:
            wire_values[result] = get_result_value(first, operand, second)
        else:
            not_done.append(ind)

    while not_done:
        ind = not_done.pop(0)
        first, operand, second, result = new_table[ind]
        if first in wire_values and second in wire_values:
            wire_values[result] = get_result_value(first, operand, second)
        else:
            not_done.append(ind)

    return dict(sorted(wire_values.items(), reverse=True))

ordered_wire_values = get_ordered_wire_values(table)


final_result=[]
for wire in ordered_wire_values:
    if wire[0]=='z':
        final_result.append(str(ordered_wire_values[wire]))

binary_number = ''.join(final_result)
final_number = int(binary_number, 2)
# print(wire_values)
print(f'Final code: {final_number}\n')


#########################################################


def obtain_bin_difference(ordered_wire_values):

    def obtain_int_number(letter):
        final_result=[]
        for wire in ordered_wire_values:
            if wire[0]==letter:
                print(wire)
                final_result.append(str(ordered_wire_values[wire]))
        binary_number = ''.join(final_result)
        final_number = int(binary_number, 2)
        return final_number

    z_number=obtain_int_number('z')
    x_number=obtain_int_number('x')
    y_number=obtain_int_number('y')

    if type=='input':
        bin_difference = bin((x_number+y_number)^z_number)[2:]
    else:
        bin_difference = bin((x_number&y_number)^z_number)[2:]

    return bin_difference

bin_difference=obtain_bin_difference(ordered_wire_values)



# print(f'{x_number}+{y_number}=={z_number}, {x_number+y_number==z_number}, {x_number+y_number-z_number}, {bin(abs(x_number+y_number-z_number))}')

connections=dict()
for ind,line in enumerate(lines):
    if len(line)>7:
        first, _, second, _, result = line.strip().split() 
        for wire in [first, second]:
            if wire not in connections:
                connections[wire]=[result]
            else:
                connections[wire].append(result)

final_z=dict()
for wire in wire_values:
    if wire[0]!='z':
        to_see={wire}
        while to_see:
            cur_wire=to_see.pop()
            while cur_wire[0]!='z':
                for i in connections[cur_wire]:
                    to_see.add(i)
                cur_wire=to_see.pop()

            
            if wire not in final_z:
                final_z[wire]=[cur_wire]
            else:
                final_z[wire].append(cur_wire)


for wire in final_z:
    print(f'{wire} finisce in {final_z[wire]}')

da_cambiare=set()
for wire in final_z:

    if wire[0] not in ['x', 'y']:
        L=len(bin_difference)
        for i in range(L):
            if bin_difference[L-1-i] == '0':
                i_string = str(i)
                if len(i_string)==1:
                    i_string='0'+i_string
                z_string = 'z'+i_string
                if z_string in final_z[wire]:
                    da_cambiare.add(wire)

print('da_cambiare', da_cambiare)

coppie=list(combinations(da_cambiare, 2))
# print(coppie)

# for final_z

# print(wire_values)
# print(f'Final code: {binary_number}, {final_number}\n')

