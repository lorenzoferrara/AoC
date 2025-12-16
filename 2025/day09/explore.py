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

        #load best points from file
        with open(f"best_points_{test_type}.txt", "r") as file:
            lines = file.readlines()
            point1 = np.array(lines[0].strip().split(","), dtype=np.int64)
            point2 = np.array(lines[1].strip().split(","), dtype=np.int64)

        diagonal_points = (point1, point2)
        anchor_point = (min(diagonal_points[0][0], diagonal_points[1][0]), min(diagonal_points[0][1], diagonal_points[1][1]))
        width = abs(diagonal_points[0][0]-diagonal_points[1][0])
        height = abs(diagonal_points[0][1]-diagonal_points[1][1])
        rectangle = plt.Rectangle(anchor_point, width, height, fill=False, edgecolor="green", linewidth=1)
        plt.gca().add_patch(rectangle)

        plt.scatter(np_dataset[:,0], np_dataset[:,1], s=2, c="red")

        plt.savefig(f"points_{test_type}.png")

        #######################

        5301,67727
        94865,50110

        colliding_sides = []

        right_x = 94865
        bottom_y = 50110

        for side in sides:
            a,b = side
            xa, ya = a
            xb, yb = b

            min_x = min(xa, xb)
            max_x = max(xa, xb)

            if min_x <= right_x <= max_x:
                if ya == yb and min_x > 50000:
                    # horizontal line
                    colliding_sides.append(side)

        print("Colliding sides at x =", right_x)
        print(colliding_sides)

        for side in colliding_sides:

            found_sides=[]
            top_y = side[0][1]

            for new_side in sides:
                a,b = new_side
                xa, ya = a
                xb, yb = b

                min_y = min(ya, yb)
                max_y = max(ya, yb)

                if min_y <= top_y <= max_y:
                    if xa == xb and min(xa, xb) < 50000:
                        # vertical line
                        found_sides.append(new_side)

            found_side = found_sides[0]
            left_x = found_side[0][0]

            print("area = ", (right_x - left_x + 1) * (bottom_y - top_y + 1))
            



        # colliding_sides = [i for i in colliding_sides if i[0]>50110 ]




