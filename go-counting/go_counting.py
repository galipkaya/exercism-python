NONE = '0'
WHITE = 'w'
BLACK = 'b'
WHITE_LIST = ['W', 'w', ' ']
BLACK_LIST = ['B', 'b', ' ']
UNCHECKED = ' '
FILLED_TERRITORIES = ['b', 'w']
ALL_TERRITORIES = ['b', 'w', '0']


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.MAX_X = len(board)
        self.MAX_Y = len(board[0])

        self.board = [list(row) for row in board]
        """self.board = []  # [list(row) for row in board]
        for i in range(0, self.MAX_Y):
            self.board.append([self.MAX_X * ''])
        for row in range(0, self.MAX_X):
            for column in range(0, self.MAX_Y):
                self.board[column][row] = board[row][column]
        """
        self.fill_board(0, 0)

    def is_north_match(self, x, y, owner):
        if y - 1 >= 0:
            return self.board[x][y - 1] in owner and self.board[x][y - 1] != NONE
        return True

    def is_south_match(self, x, y, owner):
        if y + 1 < self.MAX_Y:
            return self.board[x][y + 1] in owner and self.board[x][y + 1] != NONE
        return True

    def is_east_match(self, x, y, owner):
        if x + 1 < self.MAX_X:
            return self.board[x + 1][y] in owner and self.board[x + 1][y] != NONE
        return True

    def is_west_match(self, x, y, owner):
        if x - 1 >= 0:
            return self.board[x - 1][y] in owner and self.board[x - 1][y] != NONE
        return True

    def fill_board(self, x, y):
        # check north: x, y-1
        # if y - 1 >= 0:  # and self.board[x][y - 1] == UNCHECKED:
        #    self.fill_board(x, y - 1)
        # check south: x, y+1
        if y + 1 < self.MAX_Y:  # and self.board[x][y + 1] == UNCHECKED:
            self.fill_board(x, y + 1)
        # check east: x+1, y
        if x + 1 < self.MAX_X:  # and self.board[x + 1][y] == UNCHECKED:
            self.fill_board(x + 1, y)
        # check west: x-1, y
        # if x - 1 >= 0:  # and self.board[x - 1][y] == UNCHECKED:
        #    self.fill_board(x - 1, y)

        all_empty = self.is_north_match(x, y, UNCHECKED) and self.is_south_match(x, y, UNCHECKED) and \
            self.is_east_match(x, y, UNCHECKED) and self.is_west_match(x, y, UNCHECKED)
        if all_empty:
            self.board[x][y] = NONE
        elif self.board[x][y] != 'W' and self.board[x][y] != 'B':
            # check black
            if self.is_north_match(x, y, BLACK_LIST) and self.is_south_match(x, y, BLACK_LIST) and \
                    self.is_east_match(x, y, BLACK_LIST) and self.is_west_match(x, y, BLACK_LIST):
                self.board[x][y] = BLACK
            # check white
            elif self.is_north_match(x, y, WHITE_LIST) and self.is_south_match(x, y, WHITE_LIST) and \
                    self.is_east_match(x, y, WHITE_LIST) and self.is_west_match(x, y, WHITE_LIST):
                self.board[x][y] = WHITE

            if self.board[x][y] == UNCHECKED:
                self.board[x][y] = NONE
                self.fill_none(x, y)

    def fill_none(self, x, y):
        if y - 1 >= 0 and self.is_north_match(x, y, FILLED_TERRITORIES):
            self.board[x][y - 1] = NONE
        if y + 1 < self.MAX_Y and self.is_south_match(x, y, FILLED_TERRITORIES):
            self.board[x][y + 1] = NONE
            self.fill_none(x, y + 1)
        if x + 1 < self.MAX_X and self.is_east_match(x, y, FILLED_TERRITORIES):
            self.board[x + 1][y] = NONE
            self.fill_none(x + 1, y)
        if x - 1 >= 0 and self.is_west_match(x, y, FILLED_TERRITORIES):
            self.board[x - 1][y] = NONE

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if x < 0 or x >= self.MAX_X or y < 0 or y >= self.MAX_Y:
            raise ValueError("Coordinate error")

        result = []
        territory_color = self.board[y][x]
        if territory_color != WHITE and territory_color != BLACK:
            territory_color = NONE

        self.fill_territory(y, x, result, territory_color, [])
        return territory_color, set(result)

    def fill_territory(self, x, y, result, territory_color, travelled_points):
        if (x, y) in travelled_points:
            return
        travelled_points.append((x, y))
        if self.board[x][y] == territory_color:
            result.append((y, x))
        else:
            return

        if x - 1 >= 0:
            self.fill_territory(x - 1, y, result, territory_color, travelled_points)
        if x + 1 < self.MAX_X:
            self.fill_territory(x + 1, y, result, territory_color, travelled_points)
        if y - 1 >= 0:
            self.fill_territory(x, y - 1, result, territory_color, travelled_points)
        if y + 1 < self.MAX_Y:
            self.fill_territory(x, y + 1, result, territory_color, travelled_points)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        result = {BLACK: set(), WHITE: set(), NONE: set()}
        for x in range(0, self.MAX_X):
            for y in range(0, self.MAX_Y):
                if self.board[x][y] in ALL_TERRITORIES:
                    result[self.board[x][y]].add((y, x))

        return result
