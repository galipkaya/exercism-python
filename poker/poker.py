from functools import cmp_to_key
from collections import Counter

CARDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
HANDS = ["High card", "One pair", "Two pair", "Three of a kind", "Straight", "Flush", "Full house",
         "Four of a kind", "Straight flush"]


class Card:
    def __init__(self, card):
        self.number = card[:-1]
        self.type = card[-1]
        self.index = CARDS.index(self.number)

    def __lt__(self, other):
        return self.index < other.index

    def __str__(self):
        return self.number+self.type


class Hand:
    def __init__(self, original_hand):
        self.hand = original_hand
        self.sorted_hand = sorted([Card(c) for c in self.hand.split(" ")])
        self.numbers = [c.number for c in self.sorted_hand]
        self.number_counter = Counter(self.numbers)
        number_counts = sorted(self.number_counter.values())

        def get_kind():
            all_same = all([c.type == self.sorted_hand[0].type for c in self.sorted_hand])
            straight = all(CARDS.index(self.numbers[i]) == CARDS.index(self.numbers[i + 1]) - 1 for i in
                           range(len(self.numbers) - 1)) or self.numbers == ['2', '3', '4', '5', 'A']

            if straight and all_same:
                return "Straight flush"
            if 4 in number_counts:
                return "Four of a kind"
            if number_counts == [2, 3]:
                return "Full house"
            if all_same:
                return "Flush"
            if straight:
                return "Straight"
            if number_counts[-1] == 3:
                return "Three of a kind"
            if number_counts == [1, 2, 2]:
                return "Two pair"
            if number_counts == [1, 1, 1, 2]:
                return "One pair"
            return "High card"

        self.kind = get_kind()
        self.kind_index = HANDS.index(self.kind)

    def __lt__(self, other):
        if self.kind_index == other.kind_index:
            if self.kind == "Full house" or self.kind == "Four of a kind":
                self_number = next(iter(self.number_counter.keys()))
                other_number = next(iter(other.number_counter.keys()))
                return CARDS.index(self_number) < CARDS.index(other_number)
            elif self.kind == "Straight":
                new_self_hand = self.sorted_hand
                new_other_hand = other.sorted_hand
                if other.numbers == ['2', '3', '4', '5', 'A']:
                    new_other_hand = [other.sorted_hand[0], *other.sorted_hand[0:4]]
                if self.numbers == ['2', '3', '4', '5', 'A']:
                    new_self_hand = [self.sorted_hand[0], *self.sorted_hand[0:4]]

                for i in range(4, 0, -1):
                    if new_self_hand[i] < new_other_hand[i]:
                        return True
                    if new_self_hand[i] > new_other_hand[i]:
                        return False
            else:
                for i in range(4, 0, -1):
                    if self.sorted_hand[i] < other.sorted_hand[i]:
                        return True
                    if self.sorted_hand[i] > other.sorted_hand[i]:
                        return False

        return self.kind_index < other.kind_index

    def __str__(self):
        return " ".join(map(str, self.sorted_hand))

    def __eq__(self, other):
        return self.numbers == other.numbers


def best_hands(hands):
    compiled_hands = [Hand(h) for h in hands]
    sorted_best_hands = sorted(compiled_hands, reverse=True)

    if len(sorted_best_hands) > 1 and sorted_best_hands[0] == sorted_best_hands[1]:
        return [sorted_best_hands[0].hand, sorted_best_hands[1].hand]

    return [sorted_best_hands[0].hand]
