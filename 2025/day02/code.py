import numpy as np
import pandas as pd
import re
import os


# set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def part1(lines):

    def is_invalid(number: int):
        string_number = str(number)

        L=len(string_number)
        if L%2==1:
            return False
        
        halfL = int(L/2)
        for iter in range(halfL):
            if string_number[iter] != string_number[iter+halfL]:
                return False
        return True

    invalid_id_list = []

    num_ranges = line.split(",")
    for num_range in num_ranges:
        start, end = num_range.split("-")
        for i in range(int(start), int(end)+1):
            if is_invalid(i):
                invalid_id_list.append(i)
  
    return np.sum(invalid_id_list)


       
def part2(lines):

    def is_invalid(number: int):
        string_number = str(number)

        L=len(string_number)

        #trovo i divisori
        for series_length in range(1, L):
            if L%series_length==0:

                repetead_flag=True

                num_blocks = int(L/series_length)

                for block in range(num_blocks-1):
                    for iter in range(series_length):
                        if repetead_flag and string_number[block*series_length + iter] != string_number[(block+1)*series_length + iter]:
                            repetead_flag = False
                
                if repetead_flag:
                    return True
        return False

    invalid_id_list = []

    num_ranges = line.split(",")

    for num_range in num_ranges:
        start, end = num_range.split("-")
        for i in range(int(start), int(end)+1):
            if is_invalid(i):
                invalid_id_list.append(i)
  
    return np.sum(invalid_id_list)


if __name__ == "__main__":


    test_types = [
        'example',
        "input",
    ]


    for test_type in test_types:
        print(f"\nTest type: {test_type}")
        with open(test_type + ".txt", "r") as file:
            line = file.read()


        print("Part 1:", part1(line))
        print("Part 2:", part2(line))

