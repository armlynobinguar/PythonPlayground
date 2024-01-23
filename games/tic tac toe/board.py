class Board:
    def __init__(self):
        self.board = [' '] * 10  # Ignore index 0
        self.winning_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
            (1, 5, 9), (3, 5, 7)  # Diagonals
        ]

    def display_board(self):
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
        print("---|---|---")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print("---|---|---")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")

    def is_empty(self, position):
        return self.board[position] == ' '

    def make_move(self, position, player):
        self.board[position] = player

    def check_winner(self):
        for combo in self.winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board
