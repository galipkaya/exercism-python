import random
import string


class Robot:
    usedNames = set()

    def set_random_name(self) -> string:
        self.name = "{0}{1}{2}".format(
            random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase),
            random.randint(100, 999))

    def init_name(self):
        self.set_random_name()
        while self.name in self.usedNames:
            self.set_random_name()
        self.usedNames.add(self.name)

    def __init__(self):
        self.name = ""
        self.init_name()

    def reset(self):
        self.init_name()
