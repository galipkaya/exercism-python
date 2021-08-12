import re


def abbreviate(words):
    words_list = re.split(" |-|_", words)

    return ''.join(word[0].upper() if word != "" else "" for word in words_list)
