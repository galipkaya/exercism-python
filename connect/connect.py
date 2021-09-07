class ConnectGame:
    def __init__(self, board):
        lines = board.split("\n")
        self.board = []
        for line in lines:
            new_line = [ch for ch in line if ch != " "]
            self.board.append(new_line)

    def move(self, player, i, j, from_i, from_j):
        length_i = len(self.board)
        length_j = len(self.board[0])
        if i < 0 or i >= length_i or j < 0 or j >= length_j:
            return False

        if player == "X":
            if self.board[i][j] != "X":
                return False
            elif self.board[i][j] == "X" and j == length_j - 1:
                return True
            else:
                self.board[i][j] = "#"
                if not (from_i == i - 1 and from_j == j) and self.move(player, i - 1, j, i, j):
                    return True
                if not (from_i == i + 1 and from_j == j) and self.move(player, i + 1, j, i, j):
                    return True
                if not (from_i == i and from_j == j + 1) and self.move(player, i, j + 1, i, j):
                    return True
                if not (from_i == i-1 and from_j == j + 1) and self.move(player, i-1, j + 1, i, j):
                    return True
                if not (from_i == i+1 and from_j == j - 1) and self.move(player, i+1, j - 1, i, j):
                    return True
                if not (from_i == i and from_j == j - 1) and self.move(player, i, j - 1, i, j):
                    return True

        if player == "O":
            if self.board[i][j] == "O" and i == length_i - 1:
                return True
            elif self.board[i][j] != "O":
                return False
            else:
                if not (from_i == i + 1 and from_j == j - 1) and self.move(player, i + 1, j - 1, i, j):
                    return True
                if not (from_i == i - 1 and from_j == j + 1) and self.move(player, i - 1, j + 1, i, j):
                    return True
                if not (from_i == i and from_j == j + 1) and self.move(player, i, j + 1, i, j):
                    return True
                if not (from_i == i + 1 and from_j == j) and self.move(player, i + 1, j, i, j):
                    return True

        return False

    def get_winner(self):
        # X plays left to right
        for i in range(len(self.board)):
            if self.board[i][0] == "X":
                if self.move("X", i, 0, -1, -1):
                    return "X"

        # O plays top to bottom
        for i in range(len(self.board[0])):
            if self.board[0][i] == "O":
                if self.move("O", 0, i, -1, -1):
                    return "O"

        return ""
