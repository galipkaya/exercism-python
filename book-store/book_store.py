from collections import Counter, OrderedDict
from operator import itemgetter

def group_by(basket, group_by_5_count, group_by_4_count):
    result = 0
    counter = OrderedDict(Counter(basket).most_common())
    while not all(v == 0 for v in counter.values()):
        diff = 0
        for k, v in counter.items():
            if v != 0:
                counter[k] -= 1
                diff += 1
            if group_by_4_count > 0 and diff == 4:
                group_by_4_count -= 1
                break
            elif group_by_5_count > 0 and diff == 5:
                group_by_5_count -= 1
                break
        counter = OrderedDict(sorted(counter.items(), key=itemgetter(1), reverse=True))

        if diff == 1:
            result += 800
        elif diff == 2:
            result += 1520
        elif diff == 3:
            result += 2160
        elif diff == 4:
            result += 2560
        elif diff == 5:
            result += 3000

    return result


def total(basket):
    # maximize 4 group
    group_5_count = 0
    group_4_count = 0
    total_books = len(basket)
    while total_books >= 8:
        group_4_count += 2
        total_books -= 8
    if total_books == 5:
        group_5_count = 1
    result1 = group_by(basket, group_5_count, group_4_count)

    # maximize 5 group
    group_5_count = 0
    group_4_count = 0
    total_books = len(basket)
    while total_books >= 5:
        group_5_count += 1
        total_books -= 5
    if total_books == 4:
        group_4_count = 1
    result2 = group_by(basket, group_5_count, group_4_count)

    return min(result1, result2)
