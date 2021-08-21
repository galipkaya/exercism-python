"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from itertools import groupby

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        return 50 if all(d == dice[0] for d in dice) else 0
    elif category == ONES:
        return sum(d for d in dice if d == 1)
    elif category == TWOS:
        return sum(d for d in dice if d == 2)
    elif category == THREES:
        return sum(d for d in dice if d == 3)
    elif category == FOURS:
        return sum(d for d in dice if d == 4)
    elif category == FIVES:
        return sum(d for d in dice if d == 5)
    elif category == SIXES:
        return sum(d for d in dice if d == 6)
    elif category == FULL_HOUSE:
        dice = sorted(dice)
        dice_numbers = [len(list(group)) for key, group in groupby(dice)]
        if len(dice_numbers) != 2:
            return 0
        if (dice_numbers[0] == 2 and dice_numbers[1] == 3) or \
                (dice_numbers[0] == 3 and dice_numbers[1] == 2):
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        dice = sorted(dice)
        dice_numbers = [len(list(group)) for key, group in groupby(dice)]
        if len(dice_numbers) != 2 and len(dice_numbers) != 1:
            return 0
        if dice_numbers[0] == 4 or dice_numbers[0] == 5:
            return sum(dice[:4])
        if dice_numbers[1] == 4:
            return sum(dice[1:])
        return 0
    elif category == LITTLE_STRAIGHT:
        dice = sorted(dice)
        if dice[0] == 1 and dice[1] == 2 and dice[2] == 3 and dice[3] == 4 and dice[4] == 5:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        dice = sorted(dice)
        if dice[0] == 2 and dice[1] == 3 and dice[2] == 4 and dice[3] == 5 and dice[4] == 6:
            return 30
        else:
            return 0
    elif category == CHOICE:
        return sum(dice)
