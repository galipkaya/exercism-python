from collections import namedtuple
import functools

Student = namedtuple("Student", "name grade")


def compare_student(item1, item2):
    if item1.grade < item2.grade:
        return -1
    elif item1.grade > item2.grade:
        return 1
    else:
        if item1.name < item2.name:
            return -1
        elif item1.name > item2.name:
            return 1
        return 0


class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append(Student(name, grade))

    def roster(self):
        return [student.name for student in sorted(self.students, key=functools.cmp_to_key(compare_student))]

    def grade(self, grade_number):
        return sorted([name for name, grade in self.students if grade_number==grade])
