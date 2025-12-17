import os
import numpy as np
import copy

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

        actions = []
        for line in lines:
            direction, steps = line.strip().split()
            actions.append([direction, int(steps)])

    return actions


def get_movement(direction):
    if direction == 'R':
        movement = np.array((1,0))
    elif direction == 'L':
        movement = np.array((-1,0))
    elif direction == 'U':
        movement = np.array((0,1))
    elif direction == 'D':
        movement = np.array((0,-1))
    return movement

def get_distance(a,b, axis=None):
    if axis is None:
        return np.max(np.abs(a-b))
    
    return (a-b)[axis]


def get_new_tail_position(head, tail):

    H = copy.deepcopy(head)
    T = copy.deepcopy(tail)

    if get_distance(H,T) > 1:
        x_dist = get_distance(H,T,0)
        y_dist = get_distance(H,T,1)

        if x_dist==2:
            T+=get_movement("R")
            if y_dist>0:
                T+=get_movement("U")
            elif y_dist<0:
                T+=get_movement("D")
        elif x_dist==-2:
            T+=get_movement("L")
            if y_dist>0:
                T+=get_movement("U")
            elif y_dist<0:
                T+=get_movement("D")
        elif y_dist==2:
            T+=get_movement("U")
            if x_dist>0:
                T+=get_movement("R")
            elif x_dist<0:
                T+=get_movement("L")
        elif y_dist==-2:
            T+=get_movement("D")
            if x_dist>0:
                T+=get_movement("R")
            elif x_dist<0:
                T+=get_movement("L")

    return T


def part1(dataset):

    H=np.array((0,0))
    T=np.array((0,0))

    seen = set()
    seen.add(tuple(T))

    for direction, steps in dataset:
        movement = get_movement(direction)
        for _ in range(steps):
            H += movement
            T = get_new_tail_position(H, T)
            seen.add(tuple(T))

    return len(seen)


def part2(dataset):    
    
    H=np.array((0,0))
    tails=np.array([(0,0)]*9)

    seen = set()
    seen.add(tuple(tails[-1]))

    for direction, steps in dataset:
        movement = get_movement(direction)
        for _ in range(steps):
            H += movement
            prec = H
            for i in range(9):
                tails[i]  = get_new_tail_position(prec, tails[i])
                prec = tails[i]

            seen.add(tuple(tails[-1]))

    return len(seen)


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