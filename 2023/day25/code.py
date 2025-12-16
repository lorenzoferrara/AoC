import numpy as np
import os

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import scipy.sparse as sp
from gurobi_optimods.qubo import solve_qubo

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_cleaned_dataset(test_type):

	with open(test_type + ".txt", "r") as file:
		lines = file.readlines()
		sides = []
		points = set()
		for line in lines:
			line = line.strip().split()
			start = line[0][:-1]
			ends = line[1:]
			points.add(start)

			for end in ends:
				sides.append((start, end))
				points.add(end)
				
	# print(sides, points)

	return sides, points


####################################################


def part1(dataset):
	sides, points = dataset
	P = len(points)

	print(sides)

	adjacency_matrix = np.zeros((P,P))

	for ind1, p1 in enumerate(points):
		for ind2, p2 in enumerate(points):
			if (p1,p2) in sides or (p2,p1) in sides:
				adjacency_matrix[ind1, ind2] = 1
				adjacency_matrix[ind2, ind1] = 1

	print(adjacency_matrix)

	assert (adjacency_matrix == adjacency_matrix.T).all()

	qubo_matrix = -np.ones((P,P)) * adjacency_matrix

	for i in range(P):
		qubo_matrix[i, i] = 2*np.sum(adjacency_matrix[i,:])

	print(qubo_matrix)

	result = solve_qubo(qubo_matrix)
	print(result)
	print(result.solution)



	return 0

####################################################


def part2(dataset):

	count = 0
	return count


####################################################

if __name__ == "__main__":

	test_types = [
		"example",
		# "input",
	]

	for test_type in test_types:
		print(f"\nTest type: {test_type}")

		# Load and parse the grid data
		dataset = get_cleaned_dataset(test_type)

		# Part 1: Initial count of accessible rolls
		print("Part 1:", part1(dataset))

		# Part 2: Total removable rolls (note: modifies dataset)
		print("Part 2:", part2(dataset))
