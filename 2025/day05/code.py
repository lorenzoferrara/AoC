import numpy as np
import pandas as pd
import re
import os


# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    fresh_lists = []
    available_ingriedients = []
    fresh_flag = True

    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if len(line) == 0:
                fresh_flag = False
                continue
            if fresh_flag:
                fresh_lists.append([int(i) for i in line.split("-")])
            else:
                available_ingriedients.append(int(line))

    return [fresh_lists, available_ingriedients]


####################################################

def part1(dataset):

    fresh_lists, available_ingriedients = dataset
    fresh_count = 0

    for num in available_ingriedients:
        for start, end in fresh_lists:
            if start <= num <= end:
                fresh_count += 1
                break


    return fresh_count

####################################################
       
def part2(dataset):

    fresh_lists, _ = dataset

    def merge_overlapping_list(new_list, merged_lists):
        
        for merged_list in merged_lists:
            # Check for overlap
            if (new_list[1] >= merged_list[0] and new_list[0] <= merged_list[1]):
                # Merge the two lists
                new_minimum = min(new_list[0], merged_list[0])
                new_maximum = max(new_list[1], merged_list[1])

                merged_lists.remove(merged_list)
                new_list = [new_minimum, new_maximum]

        merged_lists.append(new_list)
            
        return merged_lists
    
    # Initial merge pass
    merged_lists = []
    for new_list in fresh_lists:
        merged_lists = merge_overlapping_list(new_list, merged_lists)

    # Continue merging until no changes occur
    retry = True
    counter=0
    while retry:
        initial_merged_lists = merged_lists
        counter += 1

        for new_list in merged_lists:
            merged_lists = merge_overlapping_list(new_list, merged_lists)
        
        if initial_merged_lists == merged_lists:
            retry = False

    total_count = 0
    for list in merged_lists:
        total_count += (list[1]-list[0]+1)

    print(f"retry counter: {counter}")

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
        print("Part 2:", part2(dataset))