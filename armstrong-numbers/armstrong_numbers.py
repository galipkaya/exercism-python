def is_armstrong_number(number):

    num_str: str = str(number)
    result: int = 0
    expo_str: int = len(num_str)
    for digit in num_str:
        result += int(digit) ** expo_str
    return number == result
