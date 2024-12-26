import numpy as np
import pandas as pd
import re
import copy

with open("input.txt", "r") as file:
    # with open("example.txt", "r") as file:
    lines = file.readlines()

total_cost = 0
single_costs = np.array([3, 1])

for line in lines:
    if len(line) > 1:
        if "A" in line:
            x_a = re.search(r"X\+(\d+)", line).group(1)
            y_a = re.search(r"Y\+(\d+)", line).group(1)
        if "B" in line:
            x_b = re.search(r"X\+(\d+)", line).group(1)
            y_b = re.search(r"Y\+(\d+)", line).group(1)
        if "P" in line:
            x_p = re.search(r"X=(\d+)", line).group(1)
            y_p = re.search(r"Y=(\d+)", line).group(1)

            A = np.array([[int(x_a), int(x_b)], [int(y_a), int(y_b)]])

            B = np.array([int(x_p), int(y_p)])

            X = np.linalg.solve(A, B)
            if np.sum(np.abs(X - np.round(X))) < 1e-6:
                cost = np.dot(X, single_costs)
                total_cost += cost

print(f"Total price: {total_cost}\n")

###################################

total_cost = 0

for line in lines:
    if len(line) > 1:
        if "A" in line:
            x_a = re.search(r"X\+(\d+)", line).group(1)
            y_a = re.search(r"Y\+(\d+)", line).group(1)
        if "B" in line:
            x_b = re.search(r"X\+(\d+)", line).group(1)
            y_b = re.search(r"Y\+(\d+)", line).group(1)
        if "P" in line:
            x_p = re.search(r"X=(\d+)", line).group(1)
            y_p = re.search(r"Y=(\d+)", line).group(1)

            A = np.array([[int(x_a), int(x_b)], [int(y_a), int(y_b)]])

            B = np.array([10000000000000 + int(x_p), 10000000000000 + int(y_p)])

            X = np.linalg.solve(A, B)
            if np.sum(np.abs(X - np.round(X))) < 1e-2:
                cost = np.dot(np.round(X), single_costs)
                total_cost += cost


print(f"Total price: {total_cost}\n")
