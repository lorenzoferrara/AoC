import numpy as np
import os
import matplotlib.pyplot as plt
import networkx as nx
from scipy.optimize import linprog
import time

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def bin_to_dec(bin_list):
    result = sum(val * (2 ** idx) for idx, val in enumerate(reversed(bin_list)))
    return int(result)

def dec_to_bin(number):
    result = bin(number)[2:]  # Remove '0b' prefix
    return result

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
    
    dataset = []

    for line in lines:
        cleaned = line.strip().split()
        item = {}
        item["buttons"] = []

        for piece in cleaned:
            if piece.startswith("["):
                lights = piece.strip("[]").replace(".", "0").replace("#", "1")
                item["lights"] = list(map(int, lights))
            elif piece.startswith("("):
                button_set = piece.strip("()").split(",")
                item["buttons"].append([int(i) for i in button_set])
            elif piece.startswith("{"):
                item["joltage"] = list(piece.strip("{}").split(","))

        dataset.append(item)
    
    return dataset


def part1(dataset):

    sum_of_shortest_paths = 0

    for item in dataset:
        binary_target = item["lights"]
        decimal_target = bin_to_dec(binary_target)
        L = len(binary_target)       

        buttons = item["buttons"]

        decimal_buttons = []
        for button_set in buttons:
            binary_button = np.zeros(L)
            binary_button[button_set] = 1
            decimal_buttons.append(bin_to_dec(binary_button))

        N_combinations = 2**L
        sides = []

        for starting_light in range(N_combinations):
            for button in decimal_buttons:
                arriving_light = starting_light ^ button
                sides.append((starting_light, arriving_light))

        distance_vector = np.zeros(N_combinations) + np.inf
        distance_vector[decimal_target] = 0
        to_see = set([decimal_target])

        #BFS ALGORITHM FOR SHORTEST PATH ON UNWEIGHTED GRAPH
        while to_see:
            point = to_see.pop()
            for start, end in sides:
                if start == point and distance_vector[end] > distance_vector[start] + 1:
                    to_see.add(end)
                    distance_vector[end] = distance_vector[start] + 1

        sum_of_shortest_paths += distance_vector[0]        
    
    return sum_of_shortest_paths

def part2(dataset):

    sum_of_shortest_paths = 0

    for item in dataset:
        target = item["joltage"]
        J = len(target)
        buttons = item["buttons"]
        B = len(buttons)

        binary_buttons = []
        for button_set in buttons:
            binary_button = np.zeros(J, dtype=int)
            binary_button[button_set] = 1
            binary_buttons.append(binary_button)

        button_matrix = np.array(binary_buttons)

        # LINEAR PROGRAMMING
        # minimize total_presses = sum_i (press_i) = press dot 1
        # sum_i (press_i * button_i) = button dot press = target

        res = linprog(c = np.ones(B), A_eq=button_matrix.T, b_eq=target, bounds=(0, None), integrality=1)

        sum_of_shortest_paths += res.fun

    return sum_of_shortest_paths


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