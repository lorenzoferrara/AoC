import numpy as np
import os
from collections import Counter


# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):

    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

    return lines


####################################################

def part1(dataset, test_type):

    lines = dataset

    def compute_distance(coord_i, coord_j):
        return np.sqrt(np.sum((coord_i-coord_j)**2))

    clusters = [] 
    coordinates_list = [] 

    if test_type == "example":
        junction_number = 10
    elif test_type == "input":
        junction_number = 1000

    L = len(lines)

    for ind, line in enumerate(lines):
        coordinates = line.split(",")
        clusters.append(ind) 
        coordinates_list.append(np.array(coordinates, dtype=np.float64))

    clusters = np.array(clusters)

    distance_matrix = np.zeros((L,L))  
    distance_matrix += np.inf

    for ind_i, coord_i in enumerate(coordinates_list):
        for ind_j, coord_j in enumerate(coordinates_list):
            if ind_i > ind_j:
                distance_matrix[ind_i, ind_j] = compute_distance(coord_i, coord_j) 

    for i in range(junction_number):
        flattened_index = np.argmin(distance_matrix)
        row = flattened_index // L
        col = flattened_index % L 
        distance_matrix[row, col] = np.inf

        if clusters[row] != clusters[col]:
            clusters[clusters == clusters[row]] = clusters[col]

        counter = Counter(clusters) 
        counts = [count for val, count in counter.most_common(3)] 

    return np.prod(counts)


####################################################
       
def part2(dataset):

    lines = dataset

    def compute_distance(coord_i, coord_j):
        return np.sqrt(np.sum((coord_i-coord_j)**2))

    clusters = [] 
    coordinates_list = [] 

    L = len(lines)

    for ind, line in enumerate(lines):
        coordinates = line.split(",")
        clusters.append(ind) 
        coordinates_list.append(np.array(coordinates, dtype=np.float64))

    clusters = np.array(clusters)

    distance_matrix = np.zeros((L,L))  
    distance_matrix += np.inf

    for ind_i, coord_i in enumerate(coordinates_list):
        for ind_j, coord_j in enumerate(coordinates_list):
            if ind_i > ind_j:
                distance_matrix[ind_i, ind_j] = compute_distance(coord_i, coord_j) 

    while len(set(clusters))>1:
        flattened_index = np.argmin(distance_matrix)
        row = flattened_index // L
        col = flattened_index % L 
        distance_matrix[row, col] = np.inf

        if clusters[row] != clusters[col]:
            clusters[clusters == clusters[row]] = clusters[col]
    
    return int(coordinates_list[row][0] * coordinates_list[col][0])



    
####################################################

if __name__ == "__main__":

    test_types = [
        'example',
        "input",
    ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset(test_type)
        print("Part 1:", part1(dataset, test_type))

        print("Part 2:", part2(dataset))