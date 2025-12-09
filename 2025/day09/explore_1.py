import numpy as np
import os
import matplotlib.pyplot as plt

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


if __name__ == "__main__":

    test_types = [
        # 'example',
        "input",
    ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset(test_type)
        L = len(dataset)

        sides = []

        for ind in range(L):
            sides.append([dataset[ind], dataset[ (ind+1)%L]])

        np_dataset = np.array(dataset)
        plt.plot(np_dataset[:,0], np_dataset[:,1], c="blue")

        #######################

        5301,67727
        94865,50110

        main_point = (94865, 50110)

        colliding_sides = []

        for side in sides:
            a,b = side
            xa, ya = a
            xb, yb = b

            min_x = min(xa, xb)
            max_x = max(xa, xb)

            if min_x <= main_point[0] <= max_x:
                if ya == yb and min_x > 50000:
                    # horizontal line
                    colliding_sides.append(side)
        print(f"Colliding sides: {colliding_sides}")


        def compute_area(point_i, point_j):
            return np.prod(np.abs(point_i - point_j) + 1)
        
        max_area = 0

        for x, y in dataset:
            if x < 40000 and 67976 >= y > 50110:
                area = compute_area(np.array(main_point), np.array([x, y]))
                if area > max_area:
                    max_area = area
                    best_point = (x, y)

        print("Best point found:", best_point)
        print("Max area found:", max_area)

        diagonal_points = (main_point, best_point)

        anchor_point = (min(diagonal_points[0][0], diagonal_points[1][0]), min(diagonal_points[0][1], diagonal_points[1][1]))
        width = abs(diagonal_points[0][0]-diagonal_points[1][0])
        height = abs(diagonal_points[0][1]-diagonal_points[1][1])
        rectangle = plt.Rectangle(anchor_point, width, height, fill=False, edgecolor="green", linewidth=1)
        plt.gca().add_patch(rectangle)

        plt.scatter(np_dataset[:,0], np_dataset[:,1], s=2, c="red")

        plt.savefig("prova.png")


        



