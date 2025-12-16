import os
import numpy as np
import copy as cp

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

        movements = []
        columns = []

        for line in lines:
            if line.startswith("m"):
                parts = line.strip().split()
                times = int(parts[1])
                start = int(parts[3]) -1 
                end = int(parts[5]) - 1
                movements.append([times, start, end])

        lines.reverse()

        for line in lines:

            stripped_line = line.strip()
            if stripped_line.startswith("1"):
                numbers = stripped_line.split("   ")
                columns_number = np.max([int(i) for i in numbers])
                # intialize columns
                for _ in range(columns_number):
                    columns.append([])


            if stripped_line.startswith("["):
                for index in range(columns_number):
                    position = 1 + index*4
                    if len(line) > position and line[position]!=" ":
                        columns[index].append(line[position])


    return columns, movements
        

def part1(dataset):

    columns, movements = cp.deepcopy(dataset)

    for times, start, end in movements:
        for _ in range(times):
            element = columns[start].pop()
            columns[end].append(element)

    message = []
    for c in columns:
        top_element = c.pop()
        message.append(top_element)

    return "".join(message)

def part2(dataset):

    columns, movements = cp.deepcopy(dataset)

    for number, start, end in movements:
        tail = columns[start][-number:]
        columns[end].extend(tail)
        columns[start] = columns[start][:-number]

    message = []
    for c in columns:
        top_element = c.pop()
        message.append(top_element)

    return "".join(message)

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