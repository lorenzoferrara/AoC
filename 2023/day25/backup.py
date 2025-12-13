import numpy as np
import os
from itertools import combinations

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
				sides.append([start, end])
				points.add(end)
				
	# print(sides, points)

	return sides, points


####################################################


def part1(dataset):
	sides, points = dataset
	P = len(points)

	def are_separated(sides):
		to_see = set([sides[0][0]])
		seen = set()

		while to_see:
			point = to_see.pop()
			seen.add(point)

			for start, end in sides:
				if point == start and end not in seen:
					to_see.add(end)
				if point == end and start not in seen:
					to_see.add(start)

		if len(seen) == P:
			return 0, None
		else:
			prod = len(seen)*(P-len(seen))
			# print(f"seen {len(seen)}, not seen {P-len(seen)}, prod {prod}")
			return 1, prod
	
	print("here 1")

	comb = combinations(sides, 3)
	LC = len(list(comb))

	print("here 2")

	for ind, avoid_sides in enumerate(comb):
		print(f"{ind}/{LC}")
		temp_sides = [i for i in sides.copy() if i not in avoid_sides]
		result, prod = are_separated(temp_sides)
		if result:
			return prod


####################################################


def part2(dataset):

	count = 0
	return count


####################################################

if __name__ == "__main__":

	test_types = [
		"example",
		"input",
	]

	for test_type in test_types:
		print(f"\nTest type: {test_type}")

		# Load and parse the grid data
		dataset = get_cleaned_dataset(test_type)

		# Part 1: Initial count of accessible rolls
		print("Part 1:", part1(dataset))

		# Part 2: Total removable rolls (note: modifies dataset)
		print("Part 2:", part2(dataset))
