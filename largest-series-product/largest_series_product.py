def largest_product(series, size):
    if size < 0:
        raise ValueError("negative size")

    length = len(series)
    if length == 0:
        if size == 0:
            return 1
        raise ValueError("empty series")

    if size > length:
        raise ValueError("too much size")

    max_product = 0
    for i in range(0, length):
        if i + size > length:
            break
        max_product = max(product(series, size, i), max_product)

    return max_product


def product(series, size, index):
    current_product = 1
    for i in range(index, index+size):
        current_product *= int(series[i])
    return current_product
