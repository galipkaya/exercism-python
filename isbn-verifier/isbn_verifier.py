def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    res = 0
    for ind, ch in enumerate(isbn):
        coef = None
        if ch == 'X':
            if ind == 9:
                coef = 10
            else:
                return False
        elif ch.isnumeric():
            coef = int(ch)
        else:
            return False
        res += coef * (10 - ind)

    return res % 11 == 0
