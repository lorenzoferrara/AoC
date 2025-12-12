import os
from functools import lru_cache

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type, part):
    with open(test_type + "_" + str(part) + ".txt", "r") as file:
        lines = file.readlines()
    
    sides = {}

    for line in lines:
        line = line.strip().split()
        start = line[0][:-1]
        ends = line[1:]
        sides[start] = ends
   
    return sides

def part1(dataset):

    sides = dataset
    starting_point = "you"

    @lru_cache(maxsize=None)
    def count_paths(start):
        if start == "out":
            return 1
        count=0
        next_points = sides[start]
        for next_point in next_points:
            count += count_paths(next_point)

        return count
                
    num_paths = count_paths(starting_point)
    return num_paths

def part2(dataset):
    sides = dataset
    starting_point = "svr"

    @lru_cache(maxsize=None)
    def count_paths(start, seen_dac, seen_fft):
        if start == "out":
            if seen_dac and seen_fft:
                return 1
            else:
                return 0

        if start == "dac":
            seen_dac = True
        if start == "fft":
            seen_fft = True
        
        count=0
        next_points = sides[start]
        for next_point in next_points:
            count += count_paths(next_point, seen_dac, seen_fft)

        return count
                
    num_paths = count_paths(starting_point, False, False)
    return num_paths

####################################################

if __name__ == "__main__":
    test_types = [
        'example', 
        'input'
        ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset(test_type,1)
        print("Part 1:", part1(dataset))

        dataset = get_cleaned_dataset(test_type,2)
        print("Part 2:", part2(dataset))