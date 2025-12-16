import os
from functools import lru_cache

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
    
    calories = []
    elf_calories = []
    
    for line in lines:
        line = line.strip()
        if not line:
            calories.append(elf_calories)
            elf_calories = []
        else:
            elf_calories.append(int(line))
    calories.append(elf_calories)  # Append the last elf's calories

    return calories

def part1(dataset):

    max_sum =0
    for list in dataset:
        max_sum = max(max_sum, sum(list))

    return max_sum

def part2(dataset):

    sum_list = []
    for list in dataset:
        sum_list.append(sum(list))

    sum_list.sort(reverse=True)
    return sum(sum_list[:3])

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