import os
import numpy as np
import copy as cp

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

    return lines
        

def part1(dataset):

    found_indices = []
    for line in dataset:
        line = list(line.strip())
        marker_length = 4
        sequence = []
        for _ in range(marker_length-1):
            sequence.append(line.pop(0))
        
        for ind in range(len(line)):
            sequence.append(line.pop(0))
            # print(set(sequence))
            if len(set(sequence)) == marker_length:
                found_indices.append(marker_length + ind) 
                break
            else:
                sequence.pop(0)

    return found_indices




def part2(dataset):

    found_indices = []
    for line in dataset:
        line = list(line.strip())
        marker_length = 14
        sequence = []
        for _ in range(marker_length-1):
            sequence.append(line.pop(0))
        
        for ind in range(len(line)):
            sequence.append(line.pop(0))
            # print(set(sequence))
            if len(set(sequence)) == marker_length:
                found_indices.append(marker_length + ind) 
                break
            else:
                sequence.pop(0)

    return found_indices

####################################################

if __name__ == "__main__":
    test_types = [
        'example', 
        'input'
        ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset(test_type)
        print("Part 1:", part1(dataset))
        print("Part 2:", part2(dataset))