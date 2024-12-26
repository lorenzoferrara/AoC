import numpy as np
import pandas as pd
import re

with open("input.txt", "r") as file:
    content = file.read()

print(content)

############## PART 1

pattern = r"mul\((\d+),(\d+)\)"

total = 0
matches = re.findall(pattern, content)
for pair in matches:
    total += int(pair[0]) * int(pair[1])

print(f"Total parte 1: {total}")

############## PART 2

pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

total = 0
matches = re.finditer(pattern, content)

dont_flag = False

for ind, match in enumerate(matches):

    a = match.group()
    print(a)

    if dont_flag == False:
        if a == "don't()":
            dont_flag = True
        elif a[0] == "m":
            pair = re.findall(r"mul\((\d+),(\d+)\)", a)[0]
            total += int(pair[0]) * int(pair[1])
    else:
        if a == "do()":
            dont_flag = False


print(f"Total parte 2: {total}")
