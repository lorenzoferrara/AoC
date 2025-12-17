import os
import numpy as np
import copy as cp
from functools import lru_cache

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

    return lines
        

def part1(dataset):

    current_dir = ""
    L = len(dataset)
    line_ind = 0

    folder_content = {}
    folders_per_level = []
    for _ in range(8):
        folders_per_level.append([])
    current_level = -1

    while line_ind < L:

        line = dataset[line_ind].strip()
        line_ind += 1

        if line.startswith("$ cd"):
            dir_name = line[5:]

            if dir_name == "..":
                current_dir = os.path.dirname(current_dir)
                current_level -= 1
            else:
                current_dir = os.path.join(current_dir, dir_name)
                current_level += 1

                if current_dir not in folder_content:
                    folder_content[current_dir] = []
                    folders_per_level[current_level].append(current_dir)

        if line.startswith("$ ls"):
            while line_ind<L and dataset[line_ind][0] != "$":
                line = dataset[line_ind].strip()
        
                if line[0].isdigit():
                    item = ["file", int(line.split()[0])] 
                    folder_content[current_dir].append(item)
                if line.startswith("dir"):
                    new_dir = os.path.join(current_dir, line.split()[1])
                    item = ["folder", new_dir] 
                    folder_content[current_dir].append(item)
                line_ind += 1

    @lru_cache(maxsize=None)     
    def compute_folder_size(folder):
        total_size = 0
        for type, value in folder_content[folder]:
            if type == "file":
                total_size += value
            else:
                total_size += compute_folder_size(value)
        return total_size

    total_size = 0
    folders_per_level.reverse()
    for folder_list in folders_per_level:
        for folder in folder_list:
            # print(folder)
            folder_size = compute_folder_size(folder)
            if folder_size <= 100000:
                total_size += folder_size

    return total_size

def part2(dataset):


    current_dir = ""
    L = len(dataset)
    line_ind = 0

    folder_content = {}
    folders_per_level = []
    for _ in range(8):
        folders_per_level.append([])
    current_level = -1

    while line_ind < L:

        line = dataset[line_ind].strip()
        line_ind += 1

        if line.startswith("$ cd"):
            dir_name = line[5:]

            if dir_name == "..":
                current_dir = os.path.dirname(current_dir)
                current_level -= 1
            else:
                current_dir = os.path.join(current_dir, dir_name)
                current_level += 1

                if current_dir not in folder_content:
                    folder_content[current_dir] = []
                    folders_per_level[current_level].append(current_dir)

        if line.startswith("$ ls"):
            while line_ind<L and dataset[line_ind][0] != "$":
                line = dataset[line_ind].strip()
        
                if line[0].isdigit():
                    item = ["file", int(line.split()[0])] 
                    folder_content[current_dir].append(item)
                if line.startswith("dir"):
                    new_dir = os.path.join(current_dir, line.split()[1])
                    item = ["folder", new_dir] 
                    folder_content[current_dir].append(item)
                line_ind += 1

    @lru_cache(maxsize=None)     
    def compute_folder_size(folder):
        total_size = 0
        for type, value in folder_content[folder]:
            if type == "file":
                total_size += value
            else:
                total_size += compute_folder_size(value)
        return total_size

    folders_per_level.reverse()
    folder_sizes = []
    for folder_list in folders_per_level:
        for folder in folder_list:            
            folder_sizes.append(compute_folder_size(folder))

    initial_free_space = 70000000 - np.max(folder_sizes)
    final_free_space = initial_free_space + np.array(folder_sizes)
    final_free_space = final_free_space[final_free_space>30000000]
    optimal_size = np.min(final_free_space)- initial_free_space

    return optimal_size

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