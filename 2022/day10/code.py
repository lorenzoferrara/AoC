import os
import numpy as np
import copy

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

        actions = []
        for line in lines:
            line = line.strip().split()
            actions.append(line)

    return actions


def part1(dataset):

    value = 1
    cycle = 1
    total_strength = 0

    for line in dataset:
        cycle += 1
        if cycle in [20,60,100,140,180,220]:
            total_strength += value * cycle       
        
        if len(line) == 2:
            change = int(line[1])
            value += change
            cycle += 1
            if cycle in [20,60,100,140,180,220]:
                total_strength += value * cycle
    
    return total_strength


def part2(dataset, test_type):

    value = 1
    cycle = 1

    result_matrix = np.full((6, 40), ".")

    for line in dataset:

        pos = cycle - 1
        row = pos // 40
        col = pos % 40

        if col in [value-1, value, value+1]:
            result_matrix[row,col] = "#"

        cycle += 1

        ###########################
        
        if len(line) == 2:
            pos = cycle - 1
            row = pos // 40
            col = pos % 40

            if col in [value-1, value, value+1]:
                result_matrix[row,col] = "#"

            change = int(line[1])
            value += change
            cycle += 1


    result_matrix = ["".join(line) for line in result_matrix]
    result_matrix = "\n".join(result_matrix)
    print(result_matrix)
    
    with open(f"output_{test_type}.txt", "w") as file:
        file.write(result_matrix)

    return


####################################################

if __name__ == "__main__":
    test_types = [
        # 'example',
        'example1',
        'input'
        ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset(test_type)
        print("Part 1:", part1(dataset))
        print("Part 2:", part2(dataset, test_type))