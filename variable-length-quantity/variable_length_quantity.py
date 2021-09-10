import re


def encode(numbers):
    result = []
    for n in numbers:
        chunks = re.findall(r"\d{1,7}(?=(?:\d{7})*$)", bin(n)[2:])

        chunks[-1] = "0" + chunks[-1]
        for i in range(len(chunks) - 1):
            chunks[i] = "1" + chunks[i].zfill(7)
        result.extend([int(num, 2) for num in chunks])
    return result


def decode(octets):
    nums = []
    n = 0
    complete = True

    for octet in octets:
        n = (n * 128) + (octet & 0x7f)
        complete = (octet & 0x80) == 0

        if complete:
            nums.append(n)
            n = 0
    if not complete:
        raise ValueError('Incomplete sequence')
    return nums;


