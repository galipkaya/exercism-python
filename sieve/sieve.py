def primes(limit):
    if limit < 2:
        return []
    result_primes = list(range(2, limit + 1))

    for i in result_primes:
        for j in range(2, int(limit/i)+1):
            try:
                result_primes.remove(j * i)
            except ValueError:
                pass
    return result_primes
