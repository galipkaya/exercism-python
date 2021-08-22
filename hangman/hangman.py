# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = "_"*len(word)

    def guess(self, char):
        if self.status == STATUS_LOSE:
            raise ValueError("already lost")
        if self.status == STATUS_WIN:
            raise ValueError("already won")

        if char in self.word:
            if char in self.masked_word:
                self.remaining_guesses -= 1
            else:
                new_word = list(self.masked_word)
                char_indexes = [i for i, ltr in enumerate(self.word) if ltr == char]
                for i in char_indexes:
                    new_word[i] = char
                self.masked_word = "".join(new_word)
                if self.masked_word.find("_") == -1:
                    self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
