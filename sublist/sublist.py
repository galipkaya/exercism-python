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

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def contains(l1, l2):
    if not l2:
        return True
    for j in range(len(l1)):
        if l1[j] == l2[0]:
            new_l1 = l1[j:j+len(l2)]
            if is_equal(new_l1, l2):
                return True
    return False


def is_equal(list_one, list_two):
    return len(list_one) == len(list_two) and all(list_one[i]==list_two[i] for i in range(len(list_one)))


def sublist(list_one, list_two):
    if (not list_one and not list_two) or is_equal(list_one, list_two):
        return EQUAL

    if len(list_one) > len(list_two) and contains(list_one, list_two):
        return SUPERLIST

    if len(list_one) < len(list_two) and contains(list_two, list_one):
        return SUBLIST

    return UNEQUAL
