
from collections import Counter
import numpy as np
from functools import cmp_to_key


file = open("input.txt", "r")

lines = file.readlines()


def get_strength(hand):

    occurr = Counter(hand)
    if len(occurr) == 1:   # poker
        return 7
    if len(occurr) == 2:
        if np.max(list(occurr.values()))==4: #4
            return 6
        elif np.max(list(occurr.values()))==3: #full
            return 5
    if len(occurr)==3:
        if np.max(list(occurr.values()))==3: #tris
            return 4
        elif np.max(list(occurr.values()))==2: #dopppia coppia
            return 3
    if len(occurr)==4:
        if np.max(list(occurr.values()))==2: #coppia
            return 2
    if len(occurr)==5: #niente
        return 1

    print('errore')
    return None


def get_order(first_value):
    if first_value=='T':
        return 10
    if first_value=='J':
        return 11
    if first_value=='Q':
        return 12
    if first_value=='K':
        return 13
    if first_value=='A':
        return 14
    return int(first_value)


def custom_compare(tuple1, tuple2):

    hand1 = tuple1[0]
    hand2 = tuple2[0]

    return compare_hands(hand1, hand2)


def compare_hands(hand1, hand2):
    if len(hand1)==0:
        return 0

    if len(hand1)==5:
        if get_strength(hand1) > get_strength(hand2):
            return 1
        if get_strength(hand1) < get_strength(hand2):
            return -1

    if get_order(hand1[0]) > get_order(hand2[0]):
        return 1
    if get_order(hand1[0]) < get_order(hand2[0]):
        return -1

    return compare_hands(hand1[1:], hand2[1:])


bid_list = []
hand_list = []

for line in lines:
    hand, bid = line.split()
    bid_list.append(int(bid))
    hand_list.append(hand)


hand_bid_list = [(hand, bid) for hand,bid in zip(hand_list, bid_list)]
# print(hand_bid_list)

sorted_list = sorted(hand_bid_list, key=cmp_to_key(custom_compare))

total_win = [(i+1)*bid for i,(hand,bid) in enumerate(sorted_list)]

print(np.sum(total_win))

#####################################

file = open("input.txt", "r")

lines = file.readlines()


def get_strength(original_hand):

    n_jokers = original_hand.count('J')
    hand = original_hand.replace('J', '')

    occurr = Counter(hand)
    if len(occurr) == 1 or len(occurr) == 0:   # poker
        return 7
    if len(occurr) == 2:
        if np.max(list(occurr.values())) + n_jokers ==4: #4
            return 6
        elif np.max(list(occurr.values())) + n_jokers ==3: #full
            return 5
    if len(occurr)==3:
        if np.max(list(occurr.values())) + n_jokers ==3: #tris
            return 4
        elif np.max(list(occurr.values())) + n_jokers ==2: #dopppia coppia
            return 3
    if len(occurr)==4:
        if np.max(list(occurr.values())) + n_jokers ==2: #coppia
            return 2
    if len(occurr)==5: #niente
        return 1

    print('errore:', original_hand)
    return None


def get_order(first_value):
    if first_value=='T':
        return 10
    if first_value=='J':
        return 1
    if first_value=='Q':
        return 12
    if first_value=='K':
        return 13
    if first_value=='A':
        return 14
    return int(first_value)


def custom_compare(tuple1, tuple2):

    hand1 = tuple1[0]
    hand2 = tuple2[0]

    return compare_hands(hand1, hand2)


def compare_hands(hand1, hand2):
    if len(hand1)==0:
        return 0

    if len(hand1)==5:
        if get_strength(hand1) > get_strength(hand2):
            return 1
        if get_strength(hand1) < get_strength(hand2):
            return -1

    if get_order(hand1[0]) > get_order(hand2[0]):
        return 1
    if get_order(hand1[0]) < get_order(hand2[0]):
        return -1

    return compare_hands(hand1[1:], hand2[1:])


bid_list = []
hand_list = []

for line in lines:
    hand, bid = line.split()
    bid_list.append(int(bid))
    hand_list.append(hand)


hand_bid_list = [(hand, bid) for hand,bid in zip(hand_list, bid_list)]
# print(hand_bid_list)

sorted_list = sorted(hand_bid_list, key=cmp_to_key(custom_compare))

total_win = [(i+1)*bid for i,(hand,bid) in enumerate(sorted_list)]

print(np.sum(total_win))
