plain = "abcdefghijklmnopqrstuvwxyz123456789"
cipher = "zyxwvutsrqponmlkjihgfedcba123456789"


def encode(plain_text):
    plain_text = plain_text.lower()
    result = ""
    chunk = 0
    for ch in plain_text:
        if not ch.isalnum():
            continue
        result += cipher[plain.index(ch)]
        chunk += 1
        if chunk % 5 == 0:
            result += " "
    return result.strip()


def decode(ciphered_text):
    result = ""
    for ch in ciphered_text:
        if ch == " ":
            continue
        result += plain[cipher.index(ch)]
    return result

