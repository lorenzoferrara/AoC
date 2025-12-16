import numpy as np
import pandas as pd
import re
import os


# set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
    return lines

####################################################

def part1(dataset):

    total_sum = 0
   
    for line in dataset:  
        line = line.replace("\n", "")
        digit_list = [int(i) for i in line]
        
        #dont consider last digit
        max_first_digit=-1
        for first_iter, digit in enumerate(digit_list[:-1]):
            if digit > max_first_digit:
                max_first_digit = digit
                pos_first_digit = first_iter

        max_second_digit = np.max(digit_list[pos_first_digit+1:])
           
        total_sum += (10*max_first_digit+max_second_digit)

    return total_sum

####################################################
       
def part2(dataset):
    total_sum = 0
   
    for line in dataset:  
        line = line.replace("\n", "")
        digit_list = [int(i) for i in line]
        L = len(digit_list)
        chosen_digits=[]
        
        minimum_pos = -1
        #dont consider last digit
        for digit_position in range(1,12+1):

            digit_mancanti= 12-digit_position

            max_digit=-1
            for iter in range(minimum_pos+1, L-digit_mancanti):
                digit = digit_list[iter]
                if digit > max_digit:
                    max_digit = digit
                    pos_digit = iter

            minimum_pos = pos_digit
            chosen_digits.append(str(max_digit))

        final_number = int("".join(chosen_digits))

        total_sum += final_number

    return total_sum

####################################################

if __name__ == "__main__":


    test_types = [
        'example',
        "input",
    ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset(test_type)

        print("Part 1:", part1(dataset))
        print("Part 2:", part2(dataset))

