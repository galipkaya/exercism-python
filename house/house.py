FIRST_LINES = [
    "This is the house that Jack built.",
    "This is the malt",
    "This is the rat",
    "This is the cat",
    "This is the dog",
    "This is the cow with the crumpled horn",
    "This is the maiden all forlorn",
    "This is the man all tattered and torn",
    "This is the priest all shaven and shorn",
    "This is the rooster that crowed in the morn",
    "This is the farmer sowing his corn",
    "This is the horse and the hound and the horn"
]

OTHER_LINES = [
    " that lay in the house that Jack built.",
    " that ate the malt",
    " that killed the rat",
    " that worried the cat",
    " that tossed the dog",
    " that milked the cow with the crumpled horn",
    " that kissed the maiden all forlorn",
    " that married the man all tattered and torn",
    " that woke the priest all shaven and shorn",
    " that kept the rooster that crowed in the morn",
    " that belonged to the farmer sowing his corn"

]


def get_line(start, end):
    rhyme = FIRST_LINES[start]
    if end != 0:
        for i in range(end-1, -1, -1):
            rhyme += OTHER_LINES[i]
    return rhyme


def recite(start_verse, end_verse):
    result = []
    if start_verse == end_verse:
        result.append(get_line(start_verse - 1, end_verse - 1))
    else:
        for i in range(start_verse-1, end_verse):
            result.append(get_line(i, i))
    return result
