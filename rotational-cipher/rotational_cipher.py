from string import ascii_lowercase
from string import ascii_uppercase


def rotate(text, key):
    result = ""
    for ch in text:
        if not ch.isalpha():
            result += ch
            continue

        source = ascii_lowercase
        if ch.isupper():
            source = ascii_uppercase

        result += source[(source.index(ch)+key) % 26]
    return result
