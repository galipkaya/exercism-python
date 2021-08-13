class Garden:
    def __init__(self, diagram, students=None):
        rows = diagram.split("\n")
        self.row1 = rows[0]
        self.row2 = rows[1]

        if students is None:
            self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
                             "Ileana", "Joseph", "Kincaid", "Larry"]
        else:
            self.students = sorted(students)

        self.plant_letters = {
            'G': "Grass",
            'C': "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

    def plants(self, student):
        result = []
        index = self.students.index(student)
        result.append(self.plant_letters.get(self.row1[2 * index]))
        result.append(self.plant_letters.get(self.row1[2 * index + 1]))
        result.append(self.plant_letters.get(self.row2[2 * index]))
        result.append(self.plant_letters.get(self.row2[2 * index + 1]))
        return result
