from board import SudokuBoard
from sudoku.player import SudokuPlayer  # Update the import statement


class SudokuGame:
    def __init__(self, initial_board):
        self.board = SudokuBoard(initial_board)
        self.players = [SudokuPlayer()]  # Placeholder for potential player-specific functionality

    def play(self):
        print("Sudoku Puzzle:")
        self.board.print_board()
        print("\nSolving...\n")

        if self.board.solve():
            print("Sudoku Solved:")
            self.board.print_board()
        else:
            print("No solution exists.")
