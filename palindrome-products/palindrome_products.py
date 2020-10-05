import sys
import itertools

def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("wrong factors")

    largest_product = -sys.maxsize - 1
    largest_factors = []

    offset = 0
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor+offset, max_factor + 1):
            if isPalindrome(i*j):
                if largest_product < i*j:
                    largest_product = i * j
                    largest_factors = [[i, j]]
                elif largest_product == i*j:
                    largest_factors.append([i,j])
        offset += 1

    if len(largest_factors) == 0:
        largest_product = None
    return largest_product, largest_factors


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("wrong factors")

    smallest_product = sys.maxsize
    smallest_factors = []
    offset = 0
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor+offset, max_factor + 1):
            if isPalindrome(i*j):
                if smallest_product > i*j:
                    smallest_product = i * j
                    smallest_factors = [[i, j]]
                elif smallest_product == i*j:
                    smallest_factors.append([i, j])
        offset += 1

    if len(smallest_factors) == 0:
        smallest_product = None
    return smallest_product, smallest_factors


def isPalindrome(number):
    num_str = str(number)
    length = len(num_str)
    if length == 1:
        return True

    return num_str == num_str[::-1]

