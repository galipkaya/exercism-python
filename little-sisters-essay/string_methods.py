def capitalize_title(title):
    '''

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    '''

    words = title.split()
    new_words = []
    for word in words:
        new_words.append(list(word)[0].upper()+word[1:]+" ")

    return "".join(new_words).rstrip()

def check_sentence_ending(sentence):
    '''

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    '''

    return sentence[-1] == "."

def clean_up_spacing(sentence):
    '''

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    '''

    return sentence.lstrip().rstrip()

def replace_word_choice(sentence, old_word, new_word):
    '''

   :param sentence: str a sentence to replace words in.
   :param new_word: str replacement word
   :param old_word: str word to replace
   :return:  str input sentence with new words in place of old words
   '''

    return sentence.replace(old_word, new_word)
