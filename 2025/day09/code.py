import numpy as np
import os

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
    
    coords = []
    for line in lines:
        cleaned = line.strip().split(",")
        coords.append(np.array(cleaned, dtype=np.int64))
    
    return coords


def compute_area(point_i, point_j):
    return np.prod(np.abs(point_i - point_j) + 1)


def part1(dataset):
    
    max_area = 0
    for point_i in dataset:
        for point_j in dataset:
            area = compute_area(point_i, point_j)
            max_area = max(max_area, area)
    return max_area


def part2(dataset, test_type):
        
    L = len(dataset)
    sides = [[dataset[ind], dataset[(ind + 1) % L]] for ind in range(L)]

    def get_extremes(point_i, point_j):
        return [min(point_i[0], point_j[0]), max(point_i[0], point_j[0]),
                min(point_i[1], point_j[1]), max(point_i[1], point_j[1])]
    
    
    def is_there_a_point_inside(point_i, point_j, dataset):
        min_x, max_x, min_y, max_y = get_extremes(point_i, point_j)
        for point_k in dataset:
            if (point_k == point_i).all() or (point_k == point_j).all():
                continue
            if min_x < point_k[0] < max_x and min_y < point_k[1] < max_y:
                return True
        return False
    
    def is_a_side_intersecting(point_i, point_j, sides):
        rect_min_x, rect_max_x, rect_min_y, rect_max_y = get_extremes(point_i, point_j)
        for a, b in sides:
            side_min_x, side_max_x, side_min_y, side_max_y = get_extremes(a, b)
            if (side_max_x > rect_min_x and side_min_x < rect_max_x and
                side_max_y > rect_min_y and side_min_y < rect_max_y):
                return True
        return False

    max_area = 0
    best_points = None

    for i, point_i in enumerate(dataset):
        for j, point_j in enumerate(dataset[i + 1:], i + 1):
            print(f"{i * L + j}/{L * L},      max area: {max_area}", end='\r')
            
            # Skip if points are aligned, since area would be small
            if point_i[0] == point_j[0] or point_i[1] == point_j[1]:
                continue
            
            if is_there_a_point_inside(point_i, point_j, dataset):
                continue
            
            if is_a_side_intersecting(point_i, point_j, sides):
                continue
            
            new_area = compute_area(point_i, point_j)
            if new_area > max_area:
                max_area = new_area
                best_points = (point_i, point_j)

    with open(f"best_points_{test_type}.txt", "w") as file:
        file.write(f"{best_points[0][0]},{best_points[0][1]}\n")
        file.write(f"{best_points[1][0]},{best_points[1][1]}\n")
    
    return max_area

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

        print("Part 2:", part2(dataset, test_type))