import numpy as np
import pandas as pd
import copy
import functools

dataset = "input"
# dataset = "example"

with open(dataset + ".txt", "r") as file:
    lines = file.readlines()

num_coords={'7':(0,0), '8':(0,1), '9':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), \
            '1':(2,0), '2':(2,1), '3':(2,2), '0':(3,1), 'A':(3,2)}

frecce_coords={'^':(0,1), 'A':(0,2), '<':(1,0), 'v':(1,1), '>':(1,2)}

# @functools.cache
@functools.lru_cache(maxsize=None)
def find_commands(start, end, mode, level):

    if mode=='numbers':
        row_1, col_1 = num_coords[start]
        row_2, col_2 = num_coords[end]
    if mode=='frecce':
        row_1, col_1 = frecce_coords[start]
        row_2, col_2 = frecce_coords[end]

    row_delta=row_2-row_1
    col_delta=col_2-col_1

    commands_oriz_vert=[]
    for i in range(abs(col_delta)):
        if col_delta>0:
            commands_oriz_vert.append('>')
        elif col_delta<0:
            commands_oriz_vert.append('<')

    for i in range(abs(row_delta)):
        if row_delta>0:
            commands_oriz_vert.append('v')
        elif row_delta<0:
            commands_oriz_vert.append('^')
    commands_oriz_vert.append('A')

    commands_vert_oriz=[]
    for i in range(abs(row_delta)):
        if row_delta>0:
            commands_vert_oriz.append('v')
        elif row_delta<0:
            commands_vert_oriz.append('^')

    for i in range(abs(col_delta)):
        if col_delta>0:
            commands_vert_oriz.append('>')
        elif col_delta<0:
            commands_vert_oriz.append('<')
    commands_vert_oriz.append('A')

    # ne scelgo unoa caso, tanto sono uguali
    if row_delta*col_delta==0:
        return commands_oriz_vert

    #condizioni per evitare di toccare la sezione vuota del tastierino
    if mode=='numbers' and row_1==3 and col_2==0:
        return commands_vert_oriz
    if mode=='numbers' and col_1==0 and row_2==3:
        return commands_oriz_vert

    if mode=='frecce' and row_1==0 and col_2==0:
        return commands_vert_oriz
    if mode=='frecce' and col_1==0 and row_2==0:
        return commands_oriz_vert

    return ['doppio', commands_oriz_vert, commands_vert_oriz]

@functools.lru_cache(maxsize=None)
def count_final_commands(target: tuple, mode:str, level:int):

    if level==0:
        return len(target)

    old_num='A'
    total_length=0
    for ind,num in enumerate(target):
        new_commands = find_commands(old_num, num, mode, level)
        if new_commands[0]!='doppio':
            total_length += count_final_commands(tuple(new_commands), 'frecce', level-1)
        else:
            len_1 = count_final_commands(tuple(new_commands[1]), 'frecce', level-1)
            len_2 = count_final_commands(tuple(new_commands[2]), 'frecce', level-1)
            total_length += min(len_1, len_2)
        old_num=num

    return total_length


###################################### PART 1

def solve_problem(part):

    if part == 1:
        robots_number=2+1
    else:
        robots_number=25+1

    total=0
    for row, line in enumerate(lines):
        numerical_code = list(line.strip())
        length = count_final_commands(tuple(numerical_code), 'numbers', robots_number)

        numeric_part= int(''.join([i for i in numerical_code if i.isnumeric()]))
        print(f'{''.join(numerical_code)}: {length} x {numeric_part} = {length*numeric_part}')
        total+=length*numeric_part

    print(f"Total complexity parte {part}: {total}\n")

for part in [1,2]:
    solve_problem(part)
