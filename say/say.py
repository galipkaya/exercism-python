ONE_HUNDRED = 100
ONE_THOUSAND = 1000
TEN_THOUSAND = 10000
HUNDRED_THOUSAND = 100000
ONE_MILLION = 1000000
TEN_MILLION = 10000000
HUNDRED_MILLION = 100000000
ONE_BILLION = 1000000000
TEN_BILLION = 10000000000
HUNDRED_BILLION = 100000000000

names_to_nineteen = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens_decimal_names = {
    2: "twenty-",
    3: "thirty-",
    4: "forty-",
    5: "fifty-",
    6: "sixty-",
    7: "seventy-",
    8: "eighty-",
    9: "ninety-"
}


def get_tens_and_ones(text):
    if int(text) > 19:
        result = tens_decimal_names.get(int(text[0])) + names_to_nineteen.get(int(text[1]), "")
        if result[-1] == '-':
            return result[:-1]
        return result
    else:
        return names_to_nineteen.get(int(text), "")


def say_number(number):
    number_string = str(number)
    result = ""

    if number >= HUNDRED_BILLION:
        result += say_number(int(number_string[:3]))+" billion "+say_number(int(number % ONE_BILLION))
    elif number >= TEN_BILLION:
        result += say_number(int(number_string[:2]))+" billion "+say_number(int(number % ONE_BILLION))
    elif number >= ONE_BILLION:
        result += say_number(int(number_string[:1]))+" billion "+say_number(int(number % ONE_BILLION))
    elif number >= HUNDRED_MILLION:
        result += say_number(int(number_string[:3]))+" million "+say_number(int(number % ONE_MILLION))
    elif number >= TEN_MILLION:
        result += say_number(int(number_string[:2]))+" million "+say_number(int(number % ONE_MILLION))
    elif number >= ONE_MILLION:
        result += say_number(int(number_string[:1]))+" million "+say_number(int(number % ONE_MILLION))
    elif number >= HUNDRED_THOUSAND:
        result += say_number(int(number_string[:3]))+" thousand "+say_number(int(number % ONE_THOUSAND))
    elif number >= TEN_THOUSAND:
        result += get_tens_and_ones(number_string[:2]) + " thousand " + say_number(number % ONE_THOUSAND)
    elif number >= ONE_THOUSAND:
        result += get_tens_and_ones(number_string[0]) + " thousand " + say_number(number % ONE_THOUSAND)
    elif number >= ONE_HUNDRED:
        result += get_tens_and_ones(number_string[0]) + " hundred " + say_number(number % ONE_HUNDRED)
    else:
        result += get_tens_and_ones(number_string)

    return result.rstrip()


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("invalid number")

    if number == 0:
        return "zero"

    return say_number(number)
