
import numpy as np

file = open("day5_data.txt", "r")

content = file.read()

seeds_string = 'seeds:'

maps = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:','humidity-to-location map:']

old_index = 0
old_string_length = len(seeds_string)

map_string = 'seed-to-soil map:'
new_index = content.find(map_string)
seeds = np.array(content[old_index+old_string_length:new_index].split())
seeds = [int(x) for x in seeds]
old_string_length = len(map_string)

map_tables = []

for i, map_string in enumerate(maps):
    if i>0:
        old_index = new_index
        new_index = content.find(map_string)
        temp = content[old_index+old_string_length:new_index].split('\n')
        old_string_length = len(map_string)

        temp = [x for x in temp if x != ""]
        temp = [x.split() for x in temp]
        temp = [[int(x) for x in sub_list] for sub_list in temp]
        temp = np.array(temp)

        map_tables.append(temp)

old_index = new_index
temp = content[old_index+old_string_length:].split('\n')
old_string_length = len(map_string)

temp = [x for x in temp if x != ""]
temp = [x.split() for x in temp]
temp = [[int(x) for x in sub_list] for sub_list in temp]
temp = np.array(temp)
map_tables.append(temp)

def find_destination(source, map_index):
    mapping = map_tables[map_index]

    for row in range(mapping.shape[0]):
        if source >= mapping[row,1] and source < mapping[row,1] + mapping[row,2]:
            destination = mapping[row,0] + source - mapping[row,1]
            return destination
    return source

locations = []
for seed in seeds:

    dest = seed
    for map_index in range(len(maps)):
        dest = find_destination(dest, map_index)

    locations.append(dest)

minimum = np.min(locations)
# print(minimum)

###################################################

file = open("day5_data.txt", "r")

content = file.read()

seeds_string = 'seeds:'

maps = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:','humidity-to-location map:']

old_index = 0
old_string_length = len(seeds_string)

map_string = 'seed-to-soil map:'
new_index = content.find(map_string)
seeds = np.array(content[old_index+old_string_length:new_index].split())
seeds = [int(x) for x in seeds]
old_string_length = len(map_string)

seeds_new = []
cur = 0
while cur < len(seeds):
    print(cur)
    start = seeds[cur]
    number = seeds[cur+1]
    seeds_new += list(range(start, start+number))
    cur += 2

map_tables = []

for i, map_string in enumerate(maps):
    if i>0:
        old_index = new_index
        new_index = content.find(map_string)
        temp = content[old_index+old_string_length:new_index].split('\n')
        old_string_length = len(map_string)

        temp = [x for x in temp if x != ""]
        temp = [x.split() for x in temp]
        temp = [[int(x) for x in sub_list] for sub_list in temp]
        temp = np.array(temp)

        map_tables.append(temp)

old_index = new_index
temp = content[old_index+old_string_length:].split('\n')
old_string_length = len(map_string)

temp = [x for x in temp if x != ""]
temp = [x.split() for x in temp]
temp = [[int(x) for x in sub_list] for sub_list in temp]
temp = np.array(temp)
map_tables.append(temp)

def find_destination(source, map_index):
    mapping = map_tables[map_index]

    for row in range(mapping.shape[0]):
        if source >= mapping[row,1] and source < mapping[row,1] + mapping[row,2]:
            destination = mapping[row,0] + source - mapping[row,1]
            return destination
    return source

minimum = None
for seed in seeds:

    dest = seed
    for map_index in range(len(maps)):
        dest = find_destination(dest, map_index)

    if minimum is None:
        minimum = dest
    elif dest < minimum:
        minimum = dest
minimum = np.min(locations)
print(minimum)

print(seeds + list(range(3,8)))
