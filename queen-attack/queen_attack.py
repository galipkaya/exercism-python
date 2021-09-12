class Queen:
    def __init__(self, row, column):
        if row < 0 or column < 0 or row >= 8 or column >= 8:
            raise ValueError("invalid value")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("same")
        return self.row == another_queen.row or self.column == another_queen.column or \
            abs(self.row - another_queen.row)==abs(self.column-another_queen.column)
