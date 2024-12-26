import numpy as np
import pandas as pd
import re
import copy
from itertools import combinations

with open("input.txt", "r") as file:
    # with open("example.txt", "r") as file:
    line = file.read()

text = []
contatore_id = 0
block_flag = True
for number in line:
    if block_flag:
        for i in range(int(number)):
            text.append(str(contatore_id))
        contatore_id += 1
        block_flag = False
    else:
        for i in range(int(number)):
            text.append(".")
        block_flag = True
# print(text)

cur_forw = 0
cur_backw = len(text) - 1
while cur_forw < cur_backw:
    while cur_forw < cur_backw and text[cur_forw] == ".":
        if text[cur_backw] != ".":
            text[cur_forw] = text[cur_backw]
            text[cur_backw] = "."

        cur_backw -= 1

    cur_forw += 1

# print(''.join(text))

total = 0
for ind, num in enumerate(text):
    if num != ".":
        total += ind * int(num)

print(f"Totale checksum parte 1: {total}\n")

##############################


class block_group:
    def __init__(self, id: int, lunghezza: int):
        self.id = id
        self.lunghezza = lunghezza

    def print(self):
        print(f"id: {self.id}, lunghezza: {self.lunghezza}")


text = []
contatore_id = 0
block_flag = True
blocchi = []
spazi = []

for number in line:
    if block_flag:
        blocchi.append(block_group(contatore_id, int(number)))
        contatore_id += 1
        block_flag = False
    else:
        block_flag = True
        spazi.append(int(number))


def get_newtext(blocchi, spazi, print_flag=True):

    new_text = []
    for ind in range(len(blocchi)):
        b = blocchi[ind]
        for i in range(b.lunghezza):
            new_text.append(b.id)
        for i in range(spazi[ind]):
            new_text.append(".")

    if print_flag:
        print("".join([str(i) for i in new_text]))

    return new_text


# get_newtext(blocchi, spazi)

cur_backw = len(blocchi) - 1
spazi.append(0)

while 0 < cur_backw:
    cur_forw = 0
    while cur_forw < cur_backw:
        # print(f"cur_back: {cur_backw}, cur_forw: {cur_forw}, id: {blocchi[cur_backw].id}")
        if blocchi[cur_backw].lunghezza <= spazi[cur_forw]:
            b_moved = blocchi.pop(cur_backw)
            old_spazio = spazi.pop(cur_backw - 1)
            spazi[cur_backw - 1] += old_spazio + b_moved.lunghezza
            spazi[cur_forw] -= b_moved.lunghezza
            spazi.insert(cur_forw, 0)
            blocchi.insert(cur_forw + 1, b_moved)
            cur_forw = 0
        else:
            cur_forw += 1

    cur_backw -= 1
    # get_newtext(blocchi, spazi)


total = 0
for ind, num in enumerate(get_newtext(blocchi, spazi, print_flag=False)):
    if num != ".":
        total += ind * int(num)

print(f"Totale checksum parte 2: {total}")
