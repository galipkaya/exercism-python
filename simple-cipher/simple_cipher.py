import string
import random

ORDINAL_A = 97
ORDINAL_Z = 122
TOTAL_CHARS = 26


class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = ""
            for i in range(100):
                ch = chr(random.randint(ord('a'), ord('z')))
                key += ch

        self.key = key
        self.letters = list(string.ascii_lowercase)

    def encode(self, text):
        result = []
        key_len = len(self.key)
        for i, text_char in enumerate(text):
            key_index = i % key_len
            cipher_char = self.key[key_index]
            shift = ord(cipher_char) - ORDINAL_A
            new_char_ordinal = ord(text_char) + shift
            if new_char_ordinal > ORDINAL_Z:
                new_char_ordinal -= TOTAL_CHARS

            result.append(chr(new_char_ordinal))

        return "".join(result)

    def decode(self, text):
        result = []
        key_len = len(self.key)
        for i, text_char in enumerate(text):
            key_index = i % key_len
            cipher_char = self.key[key_index]
            shift = ord(text_char) - ord(cipher_char)
            result.append(self.letters[shift])

        return "".join(result)
