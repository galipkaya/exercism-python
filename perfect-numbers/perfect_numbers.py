def classify(number):
    if number <= 0:
        raise ValueError("Not a natural number")

    total = 0
    for i in range(1, number//2+1):
        if number % i == 0:
            total += i

    if total < number:
        return "deficient"
    elif total > number:
        return "abundant"
    return "perfect"
