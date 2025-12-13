import os
import numpy as np

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
    
    dimension_list = []
    present_list= []
    form_list = []

    local_form = []

    for line in lines:
        line = line.strip()

        if not line:
            form_list.append(np.array(local_form))
            local_form = []

        if "x" in line:
            dimensions, presents = line.split(":")
            dimensions = dimensions.split("x")
            dimension_list.append(np.array(dimensions, dtype=np.int32))
            presents = presents.split()
            present_list.append(np.array(presents, dtype=np.int32))
        
        if line.startswith(".") or line.startswith("#"):
            map = {".": 0, "#": 1}
            line_list = [map[i] for i in line]
            local_form.append(line_list)

    return form_list, present_list, dimension_list

def part1(dataset):

    form_list, present_list, dimension_list = dataset

    form_sum = []
    for form in form_list:
        form_sum.append(np.sum(form))
    form_sum = np.array(form_sum)

    ok=0

    for presents,dimensions in zip(present_list, dimension_list):
        area = np.prod(dimensions)
        total_cover = np.sum(form_sum*presents)
        if area > total_cover:
            ok += 1

    return ok

def part2(dataset):

    return 0
            
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