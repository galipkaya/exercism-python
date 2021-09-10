from string import ascii_lowercase
from textwrap import wrap


def get_coprime(a: int):
    for i in range(27):
        if a * i % 26 == 1:
            return i
    raise ValueError("not coprime")


def encode(plain_text, a, b):
    get_coprime(a)

    def enc(ch):
        if ch.isdigit():
            return ch
        if not ch.isalnum():
            return ""
        return ascii_lowercase[(a * ascii_lowercase.index(ch) + b) % 26]

    enc_str = "".join([enc(ch) for ch in plain_text.lower()])
    return " ".join(wrap(enc_str, 5))


def decode(ciphered_text, a, b):
    a = get_coprime(a)

    def dec(ch):
        if ch.isdigit():
            return ch
        return ascii_lowercase[a * (ascii_lowercase.index(ch) - b) % 26]

    return "".join([dec(ch) for ch in ciphered_text if ch != " "])
