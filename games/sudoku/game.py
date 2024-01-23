from board import SudokuBoard  # Update the import statement

class SudokuGame:
    def __init__(self, initial_board):
        self.board = SudokuBoard(initial_board)

    def play(self):
        print("Sudoku Puzzle:")
        self.board.print_board()
        print("\nSolving...\n")

        if self.board.solve():
            print("Sudoku Solved:")
            self.board.print_board()
        else:
            print("No solution exists.")
