import os
import numpy as np
import copy as cp

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

        matrix = []
        for line in lines:
            line = list(line.strip())
            matrix.append(line)

    matrix = np.array(matrix, dtype = np.int32)
    return matrix
        

def part1(dataset):

    num_rows, num_cols = dataset.shape
    print(num_rows, num_cols)
    total_count = (num_rows-1)*4

    for row in range(1, num_rows-1):
        for col in range(1, num_cols-1):
            max_left = np.max(dataset[row , :col])
            max_right = np.max(dataset[row , col+1:])
            max_up = np.max(dataset[:row , col])
            max_down = np.max(dataset[row+1: , col])
            global_max = np.min([max_left, max_right, max_up, max_down])
            if dataset[row,col] > global_max:
                total_count += 1

            # print(row, col, dataset[row,col], global_max, total_count)

    return total_count


def part2(dataset):

    num_rows, num_cols = dataset.shape
    highest_score = 0

    for row in range(1, num_rows-1):
        for col in range(1, num_cols-1):

            up = 1
            while row - up > 0 and dataset[row-up, col] < dataset[row,col]:
                up += 1
            
            down = 1
            while row + down < num_rows-1 and dataset[row+down, col] < dataset[row,col]:
                down += 1

            left = 1
            while col - left > 0 and dataset[row, col-left] < dataset[row,col]:
                left += 1

            right = 1
            while col + right < num_cols-1 and dataset[row, col + right] < dataset[row,col]:
                right += 1

            score = np.prod([up, down, left, right])
            # print(row, col,dataset[row,col], up, down, left, right, score)
            highest_score = max(score, highest_score)

    return highest_score

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