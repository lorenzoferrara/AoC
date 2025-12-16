import os
import numpy as np

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

        areas = []
        for line in lines:
            split_line = line.strip().split(",")
            temp = []
            for pair in split_line:
                temp.append(np.array(pair.split("-"), dtype=np.int32))

            areas.append(temp)

    # print(areas)
    return areas
        

def part1(dataset):

    full_contained = 0 

    for first, second in dataset:
        length1 = first[1]-first[0]
        length2 = second[1]-second[0]
        if length1>length2:
            longer = first
            shorter = second
        else:
            longer = second
            shorter = first
        if shorter[0]>=longer[0] and shorter[1]<=longer[1]:
            full_contained += 1

    return full_contained

def part2(dataset):

    overlap = 0 

    for first, second in dataset:
        if first[1] >= second[0] and second[1] >= first[0]:
            overlap += 1

    return overlap


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