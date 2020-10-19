def factors(value):
    prime_factors = []
    while value > 1:
        for divisor in range(2, value+1):
            if value % divisor == 0:
                prime_factors.append(divisor)
                value = value // divisor
                break

    return prime_factors
