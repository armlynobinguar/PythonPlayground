class SudokuBoard:
    def __init__(self, initial_board):
        self.board = [row[:] for row in initial_board]  # Create a deep copy of the initial board

    def print_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))

    def is_safe(self, row, col, num):
        for x in range(9):
            if (
                self.board[row][x] == num
                or self.board[x][col] == num
                or self.board[row - row % 3 + x // 3][col - col % 3 + x % 3] == num
            ):
                return False
        return True

    def find_empty_location(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)  # (row, col)
        return None  # No empty location

    def solve(self):
        empty_location = self.find_empty_location()
        if not empty_location:
            return True

        row, col = empty_location

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False
