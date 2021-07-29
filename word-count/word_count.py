import re


def count_words(sentence):
    result = {}
    words = re.split(" |\n|\t|,|_", sentence.lower())

    for word in words:
        if word == "":
            continue

        word = word.strip("'").replace("!", "").replace("&", "").replace("@", "").\
            replace("$", "").replace("%", "").replace("^", "").replace(":", "").replace(".", "")

        if result.get(word) is None:
            result[word] = 1
        else:
            result[word] = result[word] + 1

    return result
