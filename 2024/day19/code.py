import numpy as np
import pandas as pd
import re
import copy
import time
from pydantic.dataclasses import dataclass
from typing import List, Tuple

dataset = "input"
# dataset = "example"

with open(dataset + ".txt", "r") as file:
    lines = file.readlines()

first_part = True
patterns = []

for line in lines:
    if len(line) < 3:
        first_part = False
    elif first_part:
        towels = line.strip().split(", ")
    else:
        patterns.append(line.strip())


def check_pattern(pattern):

    L = len(pattern)

    to_see = set()
    for towel in towels:
        if towel[0] == pattern[0] and len(towel) <= L:
            to_see.add((0, towel))

    while to_see:
        cur, towel = to_see.pop()
        ok_flag = True
        for temp_cur in range(len(towel)):
            if towel[temp_cur] != pattern[cur + temp_cur]:
                ok_flag = False

        if ok_flag:
            cur += len(towel)
            if cur == L:
                return True

            for towel in towels:
                if towel[0] == pattern[cur] and len(towel) + cur <= L:
                    to_see.add((cur, towel))
    return False


total = 0
for pattern in patterns:
    if check_pattern(pattern):
        total += 1
    # print(pattern, check_pattern(pattern))

print(f"Total possible patterns: {total}")

##################################################

import functools

@functools.cache
def count_combinations(pattern):

    total_combinations = 0
    L = len(pattern)

    for towel in towels:
        if len(towel) <= L:
            ok_flag = True
            for cur in range(len(towel)):
                if ok_flag and towel[cur] != pattern[cur]:
                    ok_flag = False

            if ok_flag:
                if len(towel)==L:
                    total_combinations += 1
                else:
                    total_combinations += count_combinations(pattern[len(towel):]) 

    return total_combinations


total_combinations = 0
for ind,pattern in enumerate(patterns):
    print(f'pattern {ind}')
    num_comb = count_combinations(pattern)
    total_combinations += num_comb

print(f"Total possible combinations: {total_combinations}")
