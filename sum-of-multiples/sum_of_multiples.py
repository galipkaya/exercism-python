def sum_of_multiples(limit, multiples):
    if len(multiples) == 0:
        return 0

    numbers = []
    multiples = sorted(multiples)

    for i in range(multiples[0], limit):
        for j in multiples:
            if j != 0 and i % j == 0:
                numbers.append(i)
                break

    return sum(numbers)
