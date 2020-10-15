def is_isogram(string):
    sorted_string = sorted(string.lower())
    for i, ch in enumerate(sorted_string):
        if i > 0 and ch != '-' and ch != ' ' and ch == sorted_string[i - 1]:
            return False
    return True
