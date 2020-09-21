class Matrix:
    def __init__(self, matrix_string):
        self.values = [list(map(int, x)) for x in (row.split() for row in matrix_string.split("\n"))]

    def row(self, index):
        return self.values[index-1]

    def column(self, index):
        return [column_value[index-1] for column_value in self.values]
