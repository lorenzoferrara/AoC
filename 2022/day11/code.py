import os
import numpy as np
import copy

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()

        starting_line = lines.pop(0)
        lines.append(starting_line)

        monkeys = []
        monkey = dict()
        
        for line in lines:
            line = line.strip()
            if line.startswith("Monkey"):
                monkeys.append(monkey)
                monkey = dict()
            elif line.startswith("Starting"):
                _, items = line.split(":")
                items = items.split(", ")
                items = [int(i) for i in items]
                monkey["items"] = items
            elif line.startswith("Operation"):
                _, formula = line.split("=")
                _, sign, number = formula.strip().split()
                if number == "old":
                    sign = "**"
                    number = 2
                monkey["operation"] = [sign, int(number)]
            elif line.startswith("Test"):
                _, factor = line.split("by")
                factor = int(factor)
                monkey["factor"] = factor
            elif line.startswith("If true"):
                _, target_monkey = line.split("monkey")
                monkey["target_true"] = int(target_monkey)
            elif line.startswith("If false"):
                _, target_monkey = line.split("monkey")
                monkey["target_false"] = int(target_monkey)

    # print(monkeys)

    return monkeys


def part1(dataset):

    monkeys = copy.deepcopy(dataset)

    num_rounds = 20

    inspection_times = np.zeros(len(monkeys), dtype = np.int32)

    for _ in range(num_rounds):
        for ind, monkey in enumerate(monkeys):
            operation, number = monkey["operation"]
            factor = monkey["factor"]
            target_true = monkey["target_true"]
            target_false = monkey["target_false"]

            while monkey["items"]:
                inspection_times[ind]+=1

                item = monkey["items"].pop(0)

                if operation == "*":
                    item *= number
                elif operation == "+":
                    item += number
                else:
                    item = item**2

                item = int(item / 3)

                if item % factor == 0:
                    monkeys[target_true]["items"].append(item)
                else:
                    monkeys[target_false]["items"].append(item)

    busiest_monkeys = sorted(inspection_times, reverse=True)[:2]

    return np.prod(busiest_monkeys)


def part2(dataset):
    
    monkeys = copy.deepcopy(dataset)

    factors = []
    for monkey in monkeys:
        factors.append(monkey["factor"])

    modulus = np.prod(factors)

    num_rounds = 10000

    inspection_times = np.zeros(len(monkeys), dtype = np.int32)

    for round in range(1,num_rounds+1):

        for ind, monkey in enumerate(monkeys):

            operation, number = monkey["operation"]
            factor = monkey["factor"]
            target_true = monkey["target_true"]
            target_false = monkey["target_false"]

            while monkey["items"]:
                inspection_times[ind] += 1

                item = monkey["items"].pop(0)

                if operation == "*":
                    item *= number
                elif operation == "+":
                    item += number
                else:
                    item = item**2

                # item = int(item / 3)

                #my reduction
                # https://www.reddit.com/r/adventofcode/comments/zizi43/2022_day_11_part_2_learning_that_it_was_that/
                item = item % modulus

                if item % factor == 0:
                    monkeys[target_true]["items"].append(item)
                else:
                    monkeys[target_false]["items"].append(item)

        if round in [1,20] or round % 1000 == 0:
            print(f"round {round}: {inspection_times}")

    busiest_monkeys = sorted(inspection_times, reverse=True)[:2]

    return np.prod(busiest_monkeys)



####################################################

if __name__ == "__main__":
    test_types = [
        'example',
        'input',
        ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset(test_type)
        print("Part 1:", part1(dataset))
        print("Part 2:", part2(dataset))