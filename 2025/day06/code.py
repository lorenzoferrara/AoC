import numpy as np
import os


# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):

    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

    grid = []

    for line in lines[:-1]:
        line = line.strip()
        grid.append([int(i) for i in line.split()])

    operations = lines[-1].strip().split()

    grid = np.array(grid)

    return grid, operations

def get_cleaned_dataset_part2(test_type):

    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

    grid = []

    for line in lines[:-1]:
        line = line.replace("\n", "")
        grid.append([i for i in line])

    operations = lines[-1].strip().split()

    grid = np.array(grid)

    return grid, operations



####################################################

def part1(dataset):

    grid, operations = dataset
    total_count = 0

    for ind, operation in enumerate(operations):
        if operation == "*":
            total_count += np.prod(grid[:,ind])
        elif operation == "+":
            total_count += np.sum(grid[:,ind])

    return total_count


####################################################
       
def part2(dataset):

    grid, operations = dataset

    groups =[]
    local_group=[]
    total_count = 0

    for col_index in range(grid.shape[1]):
        col = list(grid[:,col_index])
        col = [i for i in col if i != ' ']
        if len(col)==0:
            groups.append(local_group)
            local_group=[]
        else:
            number = int("".join(col))
            local_group.append(number)

    groups.append(local_group)


    for ind, operation in enumerate(operations):
        if operation == "*":
            total_count += np.prod(groups[ind])
        elif operation == "+":
            total_count += np.sum(groups[ind])

    return total_count
    
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

        dataset_part2 = get_cleaned_dataset_part2(test_type)
        print("Part 2:", part2(dataset_part2))