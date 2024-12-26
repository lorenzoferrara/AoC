import numpy as np
import pandas as pd
import re
import copy
import time

type = "input"
# type='example'

with open(type + ".txt", "r") as file:
    lines = file.readlines()

if type == "example":
    x_num = 11
    y_num = 7
if type == "input":
    x_num = 101
    y_num = 103


quadr = {}
for i in range(1, 5):
    quadr[i] = 0

for line in lines:
    match = re.search(r"p=(\d+),(\d+)", line)
    x = int(match.group(1))
    y = int(match.group(2))

    match = re.search(r"v=(-?\d+),(-?\d+)", line)
    vx = int(match.group(1))
    vy = int(match.group(2))

    print(x, y, vx, vy)
    for step in range(100):
        x = (x + vx) % x_num
        y = (y + vy) % y_num
    if x < (x_num - 1) / 2 and y > (y_num - 1) / 2:
        quadr[4] += 1
    if x < (x_num - 1) / 2 and y < (y_num - 1) / 2:
        quadr[3] += 1
    if x > (x_num - 1) / 2 and y > (y_num - 1) / 2:
        quadr[1] += 1
    if x > (x_num - 1) / 2 and y < (y_num - 1) / 2:
        quadr[2] += 1

total_guards = np.prod([quadr[i] for i in quadr])
print(f"Total guards: {total_guards}")

###############################################################


def create_grid():
    # grid=[]

    # for i in range(x_num):
    #     grid.append( list('.'*y_num)*x_num )
    # return grid

    return np.zeros((x_num, y_num))


def print_grid(grid):

    texts = []
    for row in grid:
        texts.append("".join(row))
    final_text = "\n".join(texts)
    print(final_text)
    print()
    print()


class robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x = (self.x + self.vx) % x_num
        self.y = (self.y + self.vy) % y_num

    def update_grid(self, grid):
        # grid[self.x][self.y]='#'
        grid[self.x, self.y] = 1
        return grid


robots = []

import tkinter as tk

ratio = 5

# Create the main window

square_size = ratio

min_step = 100

for line in lines:
    match = re.search(r"p=(\d+),(\d+)", line)
    x = int(match.group(1))
    y = int(match.group(2))
    match = re.search(r"v=(-?\d+),(-?\d+)", line)
    vx = int(match.group(1))
    vy = int(match.group(2))
    robots.append(robot(x, y, vx, vy))

# for step in range(20):
# window = tk.Tk()
# window.title("Square Visualization")
# window.geometry(str(x_num*ratio)+"x"+str(y_num*ratio)+'+500+300')
# label = tk.Label(window, text=f"step: {step}", font=("Arial", 24, "bold"))
# label.pack(pady=10)

# canvas = tk.Canvas(window, width=x_num*ratio, height=y_num*ratio, bg="white")
# canvas.pack()

# for robot in robots:
#     robot.move()
#     canvas.create_rectangle(robot.x*ratio, robot.y*ratio, \
#         robot.x*ratio + square_size, robot.y*ratio + square_size, \
#         fill="blue", outline="black")

# window.after(300, window.destroy)
# window.mainloop()


def find_square(x, y, grid):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if grid[x + i, y + j] != 1:
                return False
    return True


def find_tree():

    grid = create_grid()

    for step in range(1, 10000):

        grid *= 0
        print(step)
        for robot in robots:
            robot.move()
            grid = robot.update_grid(grid)

        for x in range(x_num):
            for y in range(y_num):
                if 0 < x < x_num - 1 and 0 < y < y_num - 1:
                    if find_square(x, y, grid):

                        print(f"############ {step} ##########")

                        window = tk.Tk()
                        window.title("Square Visualization")
                        window.geometry(
                            str(x_num * ratio) + "x" + str(y_num * ratio) + "+500+300"
                        )

                        label = tk.Label(
                            window, text=f"step: {step}", font=("Arial", 24, "bold")
                        )
                        label.pack(pady=10)

                        canvas = tk.Canvas(
                            window,
                            width=x_num * ratio,
                            height=y_num * ratio,
                            bg="white",
                        )
                        canvas.pack()

                        for robot in robots:

                            canvas.create_rectangle(
                                robot.x * ratio,
                                robot.y * ratio,
                                robot.x * ratio + square_size,
                                robot.y * ratio + square_size,
                                fill="blue",
                                outline="black",
                            )

                        window.mainloop()
                        return step


find_tree()
