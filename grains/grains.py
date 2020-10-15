def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Invalid parameter")

    return 2 ** (number - 1)


def total():
    res = 0
    for i in range(1, 65):
        res += square(i)

    return res

