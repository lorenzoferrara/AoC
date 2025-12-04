import numpy as np
import pandas as pd
import re
import os


# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
        grid = []
        for line in lines:
            line = line.replace("\n", "")
            line = line.replace("@", "1")
            line = line.replace(".", "0")
            grid.append(list(line))


    grid = np.array(grid, dtype=np.float32)

    # print(grid)

    return grid

####################################################

def part1(dataset):

    count = 0
    rows, cols = dataset.shape
    
    # Check each position in the grid
    for i in range(rows):
        for j in range(cols):
            # Only check positions with paper rolls
            if dataset[i, j] == 1:
                # Extract the 3x3 neighborhood (or smaller at edges)
                temp_square = dataset.copy()
                temp_square = temp_square[max(i-1, 0):min(i+2, rows), 
                                         max(j-1, 0):min(j+2, cols)]
                
                # If sum < 5, there are fewer than 4 adjacent rolls (including itself)
                # This means the forklift can access this roll
                if temp_square.sum() < 5:
                    count += 1    

    return count

####################################################
       
def part2(dataset):

    count = 0
    rows, cols = dataset.shape

    # Continue processing until no more rolls can be removed
    new_grid = True
    counter = 1
    
    while new_grid:
        # Assume no changes unless we find accessible rolls
        new_grid = False
        counter += 1

        # Check each position in the grid
        for i in range(rows):
            for j in range(cols):
                # Only check positions with paper rolls
                if dataset[i, j] == 1:
                    # Extract the 3x3 neighborhood (or smaller at edges)
                    temp_square = dataset.copy()
                    temp_square = temp_square[max(i-1, 0):min(i+2, rows), 
                                             max(j-1, 0):min(j+2, cols)]
                    
                    # If accessible (fewer than 4 adjacent rolls)
                    if temp_square.sum() < 5:
                        count += 1
                        # Remove this roll from the grid
                        dataset[i, j] = 0
                        # Mark that we made changes (need another iteration)
                        new_grid = True      

    return count

####################################################

if __name__ == "__main__":


    test_types = [
        'example',
        "input",
    ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        # Load and parse the grid data
        dataset = get_cleaned_dataset(test_type)

        # Part 1: Initial count of accessible rolls
        print("Part 1:", part1(dataset))
        
        # Part 2: Total removable rolls (note: modifies dataset)
        print("Part 2:", part2(dataset))

