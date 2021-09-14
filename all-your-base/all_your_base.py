def get_base_10(digits, input_base):
    exp = len(digits)-1
    total = 0
    for n in digits:
        if n >= input_base:
            raise ValueError("invalid number")
        elif n < 0:
            raise ValueError("negative number")
        total += n * input_base**exp
        exp -= 1
    return total


def rebase(input_base, digits, output_base):
    if input_base <= 1 or output_base <= 1:
        raise ValueError("Negative base")

    base_10_number = get_base_10(digits, input_base)
    if base_10_number == 0:
        return [0]

    if output_base == 10:
        return list(map(int, list(str(base_10_number))))
    else:
        result = []
        number = base_10_number
        q = number
        while True:
            q, r = divmod(q, output_base)
            result.insert(0, r)
            if q < output_base:
                result.insert(0, q)
                break
        return result
