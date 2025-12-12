import os

# Set the current dir to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_cleaned_dataset_1(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
        
    strategies = []
    for line in lines:
        line = line.strip()
        
        map = {"A":"rock", "B": "paper", "C": "scissors",
               "X":"rock", "Y": "paper", "Z": "scissors"} 
        for prima, dopo in map.items():
            line = line.replace(prima, dopo)
        strategies.append(line)

    # print(strategies)

    return strategies

def get_cleaned_dataset_2(test_type):
    with open(test_type + ".txt", "r") as file:
        lines = file.readlines()
        
    strategies = []
    for line in lines:
        line = line.strip()
        
        map = {"A":"rock", "B": "paper", "C": "scissors",
               "X": "0", "Y": "3", "Z": "6" } 
        for prima, dopo in map.items():
            line = line.replace(prima, dopo)
        line = line.split()
        strategies.append(line)

    print(strategies)

    return strategies

def part1(dataset):

    first_score = {"rock": 1, "paper": 2, "scissors":3}
    second_score = {  
        "rock": { "paper": 6, "scissors": 0, "rock": 3},
        "paper": {"rock": 0, "scissors": 6, "paper": 3},
        "scissors": {"rock": 6, "paper": 0, "scissors": 3}}

    score = 0
    for strategy in dataset:
        his_choice, my_choice = strategy.split()
        score += first_score[my_choice]
        if his_choice == my_choice:
            score += 3
        else:
            score += second_score[his_choice][my_choice]

    return score

def part2(dataset):

    first_score = {"rock": 1, "paper": 2, "scissors" :3}
    second_score = {  
        "rock": { "paper": 6, "scissors": 0, "rock": 3},
        "paper": {"rock": 0, "scissors": 6, "paper": 3},
        "scissors": {"rock": 6, "paper": 0, "scissors": 3}}

    score = 0
    for strategy in dataset:
        his_choice, wanted_result = strategy

        for choice,result in second_score[his_choice].items():
            if result == int(wanted_result):
                my_choice = choice

        assert my_choice is not None
        
        score += first_score[my_choice]
        score += second_score[his_choice][my_choice]

    return score

####################################################

if __name__ == "__main__":
    test_types = [
        'example', 
        'input'
        ]

    for test_type in test_types:
        print(f"\nTest type: {test_type}")

        dataset = get_cleaned_dataset_1(test_type)
        print("Part 1:", part1(dataset))

        dataset = get_cleaned_dataset_2(test_type)
        print("Part 2:", part2(dataset))