lyric = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]

enumString = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]


def recite_sub(start_verse, end_verse):
    result = "On the {} day of Christmas my true love gave to me: ".format(enumString[end_verse - 1])

    for i in range(end_verse - 1, -1, -1):
        if end_verse > 1 and i == 0:
            result += "and "
        result += lyric[i]

    return result


def recite(start_verse, end_verse):
    if start_verse == end_verse:
        return [recite_sub(start_verse, end_verse)]
    else:
        result = []
        for i in range(start_verse, end_verse+1):
            result.append( recite_sub(i, i))
        return result
