import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

type='input'
type='example'

with open(type+'.txt', 'r') as file:
    lines = file.readlines()

wire_values=dict()

not_done=[]

def check_connection(ind):
    line=lines[ind]
    first, operand, second, _, result = line.strip().split() 
    if first in wire_values and second in wire_values:
        if operand=='AND':
            wire_values[result]=wire_values[first] and wire_values[second]
        elif operand=='OR':
            wire_values[result]=wire_values[first] or wire_values[second]
        elif operand=='XOR':
            wire_values[result]=wire_values[first] ^ wire_values[second]
        else:
            raise ValueError
    else:
        not_done.append(ind)


for ind,line in enumerate(lines):
    if len(line)==7:
        wire, value = line.strip().split(':')
        wire_values[wire]=int(value)
    elif len(line)>7:
        check_connection(ind)  

while len(not_done)>0:
    ind = not_done.pop(0)
    check_connection(ind)

ordered_wire_values = dict(sorted(wire_values.items(), reverse=True))


final_result=[]
for wire in ordered_wire_values:
    if wire[0]=='z':
        final_result.append(str(ordered_wire_values[wire]))

binary_number = ''.join(final_result)
final_number = int(binary_number, 2)
# print(wire_values)
print(f'Final code: {final_number}\n')


#########################################################


wire_values=dict()

not_done=[]

for ind,line in enumerate(lines):
    if len(line)==7:
        wire, value = line.strip().split(':')
        wire_values[wire]=int(value)
    elif len(line)>7:
        check_connection(ind)  

while len(not_done)>0:
    ind = not_done.pop(0)
    check_connection(ind)

ordered_wire_values = dict(sorted(wire_values.items(), reverse=True))

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

bin_difference = bin((x_number+y_number)^z_number)[2:]
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


# for 


for i in final_z:
    print(f'{i}: {final_z[i]}')

da_cambiare=set()
for wire in final_z:

    for i in range(len(bin_difference)):
        if bin_difference[-(1+i)] == '0':
            i_string = str(i)
            if len(i_string)==1:
                i_string='0'+i_string
            z_string = 'z'+i_string
            if final_z[wire][0]==z_string:
                da_cambiare.add(wire)

print('da_cambiare', da_cambiare)



# for final_z

# print(wire_values)
# print(f'Final code: {binary_number}, {final_number}\n')

