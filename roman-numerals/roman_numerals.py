NUMBERS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def roman(number):
    def _roman(num, result):
        keys = NUMBERS.keys()
        if num in keys:
            result = result + NUMBERS[num]
            return result

        rem = 0
        for n in keys:
            if n < num:
                quo, rem = divmod(num, n)
                result = result + NUMBERS[n] * quo
                num -= quo * n
                break
        if rem == 0:
            return result
        return _roman(rem, result)

    return _roman(number, "")
