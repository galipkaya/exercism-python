def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())
    res = []
    for tmp in candidates:
        if word.lower() != tmp.lower() and sorted_word == sorted(tmp.lower()):
            res.append(tmp)

    return res
