import numpy as np
import pandas as pd
import re
import os


# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):

    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

    return lines


####################################################

def part1(dataset):

    lines = dataset

    start_line = np.array(list(lines[0]))
    current_positions = np.where(start_line == "S")[0]

    total_splittings=0

    for line in lines:
        next_positions = set() 
        line = np.array(list(line))
        split_positions = np.where(line == "^")[0]
        
        for pos in current_positions:
            if pos in split_positions:
                total_splittings += 1
                next_positions.add(pos-1)
                next_positions.add(pos+1) 
            else:
                next_positions.add(pos)

        current_positions = next_positions

    return total_splittings





####################################################
       
def part2(dataset):

    lines = dataset

    start_line = np.array(list(lines[0]))
    current_positions = np.where(start_line == "S")[0]
    current_positions = { i:1 for i in current_positions} 

    for line in lines:
        next_positions = dict() 
        line = np.array(list(line))
        split_positions = np.where(line == "^")[0]
        
        for pos,value in current_positions.items():
            if pos in split_positions:
                if (pos-1) not in next_positions:
                    next_positions[pos-1] = value
                else:
                    next_positions[pos-1] += value
                if (pos+1) not in next_positions:
                    next_positions[pos+1] = value
                else:
                    next_positions[pos+1] += value
            
            else:
                if pos not in next_positions:
                    next_positions[pos] = value
                else:
                    next_positions[pos] += value

        current_positions = next_positions

    total_timelines = np.sum([value for pos, value in current_positions.items()])

    return total_timelines



    
####################################################

if __name__ == "__main__":

    test_types = [
        'example',
        "input",
    ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset(test_type)
        print("Part 1:", part1(dataset))

        print("Part 2:", part2(dataset))