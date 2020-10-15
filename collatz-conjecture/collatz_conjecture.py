def steps(number):
    if number <= 0:
        raise ValueError("Invalid parameter")
    res = 0
    while number != 1:
        res += 1
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    return res
