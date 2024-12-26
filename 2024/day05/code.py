import numpy as np
import pandas as pd
import re

with open("input.txt", "r") as file:
    # with open("example.txt", "r") as file:
    lines = file.readlines()

######################### PART 1

prima_parte = True
rules = []
updates = []

for line in lines:
    if len(line) < 3:
        prima_parte = False

    elif prima_parte:
        rules.append(line.strip().split("|"))
    else:
        updates.append(line.strip().split(","))


def is_valid(update):
    for rule in rules:
        try:
            ind_1 = update.index(rule[0])
            ind_2 = update.index(rule[1])
            if ind_1 > ind_2:
                return False
        except:
            pass
    return True


totale = 0
for update in updates:
    if is_valid(update):
        L = len(update)
        print(int(update[L // 2]))
        totale += int(update[L // 2])
print(f"Totale: {totale}")

######################### PART 2


def is_valid(update):
    for rule in rules:
        try:
            ind_1 = update.index(rule[0])
            ind_2 = update.index(rule[1])
            if ind_1 > ind_2:
                return False
        except:
            pass
    return True


def fix_update(update):
    for rule in rules:
        try:
            ind_1 = update.index(rule[0])
            ind_2 = update.index(rule[1])
            if ind_1 > ind_2:
                element = update.pop(ind_2)
                update.insert(ind_1, element)
        except:
            pass
    return update


totale = 0
for update in updates:

    if not is_valid(update):
        while not is_valid(update):
            update = fix_update(update)

        L = len(update)
        print(int(update[L // 2]))
        totale += int(update[L // 2])
print(f"Totale: {totale}")
