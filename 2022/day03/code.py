import os

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
        return lines
        

def part1(dataset):

    total_priority = 0

    for line in dataset:
        L = len(line)
        first = set(line[:L//2])
        second = set(line[L//2:])
        inters = first.intersection(second)
        ascii_value = ord(inters.pop())
        if ascii_value < 96:
            # uppercase
            priority = ascii_value-ord("A")+27 
        else:
            priority = ascii_value-ord("a")+1 

        total_priority += priority

    return total_priority

def part2(dataset):

    total_priority = 0
    counter = 0
    group = []

    for line in dataset:
        
        if counter < 2:
            group.append(set(line.strip()))
            counter += 1
        else:
            
            group.append(set(line.strip()))
            counter = 0
            first, second, third = group
            group = []
            
            inters = first.intersection(second).intersection(third)
            ascii_value = ord(inters.pop())
            if ascii_value < 96:
                # uppercase
                priority = ascii_value-ord("A")+27 
            else:
                priority = ascii_value-ord("a")+1 

            total_priority += priority

    return total_priority


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