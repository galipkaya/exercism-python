class Allergies:

    allergy_dict = {
        "cats": 128,
        "pollen": 64,
        "chocolate": 32,
        "tomatoes": 16,
        "strawberries": 8,
        "shellfish": 4,
        "peanuts": 2,
        "eggs": 1,
    }

    def __init__(self, score):
        score = score % 256
        self.score = score
        self.allergy_values = []
        for key, value in Allergies.allergy_dict.items():
            if score >= value:
                self.allergy_values.append(key)
                score -= value
            if score == 0:
                break

    def allergic_to(self, item):
        if self.score == 0:
            return False

        return item in self.allergy_values

    @property
    def lst(self):
        return self.allergy_values
