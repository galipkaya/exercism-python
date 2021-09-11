import math


def cipher_text(plain_text):
    if not plain_text:
        return ""
    text = [ch for ch in plain_text.lower() if ch.isalnum()]
    
    # find lengths
    min_length = int(math.ceil(math.sqrt(len(text))))
    max_length = min_length
    if min_length ** 2 < len(text):
        max_length = min_length + 1
    elif (min_length-1)*max_length>len(text):
        min_length -= 1

    text += " " * (min_length * max_length - len(text))

    # convert to matrix
    matrix = []
    step = min_length
    if min_length != max_length:
        step = min_length + 1
    for i in range(0, len(text), step):
        matrix.append(text[i:i + max_length])

    # transpose matrix
    t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return " ".join("".join(row) for row in t_matrix)
