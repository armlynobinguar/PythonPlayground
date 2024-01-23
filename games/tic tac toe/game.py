from board import Board

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_move(self):
        while True:
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): "))
                if 1 <= move <= 9 and self.board.is_empty(move):
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")

    def play_game(self):
        self.board.display_board()
        for _ in range(9):
            move = self.get_player_move()
            self.board.make_move(move, self.current_player)
            self.board.display_board()

            if self.board.check_winner():
                print(f"Player {self.current_player} wins!")
                break

            if self.board.is_board_full():
                print("It's a draw!")
                break

            self.switch_player()
