import math


def triplets_with_sum(number):
    result = []
    for a in range(1, number):
        for b in range(a + 1, number):
            c = math.sqrt(a ** 2 + b ** 2)
            number_dec = str(c-int(c))[2:]
            total = a + b + int(c)
            if number_dec == '0' and total == number:
                result.append([a, b, int(c)])
            if total > number:
                break
    return result
