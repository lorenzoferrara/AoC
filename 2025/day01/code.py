import numpy as np
import pandas as pd
import re
import os

# set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def part1(lines):
    current = 50
    counter = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        if direction == 'L':
            end = current - steps
        elif direction == 'R':
            end = current + steps

        current = end % 100

        if current == 0:
            counter += 1
        
    return counter

def part2(lines):
    current = 50
    counter = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        if direction == 'L':
            end = current - steps
            rounds = np.abs(end//100)
            if current == 0:
                rounds -= 1
        elif direction == 'R':
            end = current + steps
            rounds = end // 100

        current = end % 100
        if direction == 'L' and current == 0:
            counter += 1

        counter += rounds
        
    return counter

if __name__ == "__main__":

    test_types = [
        'example',
        "input",
    ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")
        with open(test_type + ".txt", "r") as file:
            lines = file.readlines()

        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))