class Garden:
    plant_letters = {
        'G': "Grass",
        'C': "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    default_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"]

    def __init__(self, diagram, students=None):
        rows = diagram.split("\n")
        self.row1 = rows[0]
        self.row2 = rows[1]

        if not students:
            self.students = Garden.default_students
        else:
            self.students = sorted(students)

    def plants(self, student):
        result = []
        index = self.students.index(student)
        result.append(self.plant_letters.get(self.row1[2 * index]))
        result.append(self.plant_letters.get(self.row1[2 * index + 1]))
        result.append(self.plant_letters.get(self.row2[2 * index]))
        result.append(self.plant_letters.get(self.row2[2 * index + 1]))
        return result
