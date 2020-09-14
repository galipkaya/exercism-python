def is_pangram(sentence):
    if sentence == "":
        return False
    letters = [0] * 26
    for letter in sentence:
        if not letter.isalpha():
            continue
        i = ord(letter.lower()) - ord('a')
        letters[i] += 1

    return 0 not in letters
