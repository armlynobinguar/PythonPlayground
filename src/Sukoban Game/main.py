# main.py
from game import SokobanGame
from level import get_sample_level


# Additional helper functions for displaying the game
def display_game(game):
    for y, row in enumerate(game.level):
        for x, char in enumerate(row):
            if (x, y) == game.player_position:
                print("P", end=" ")
            elif (x, y) in game.boxes:
                print("B", end=" ")
            elif (x, y) in game.targets:
                print("T", end=" ")
            elif char == "#":
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()


def main():
    level = get_sample_level()
    game = SokobanGame(level)

    while not game.is_game_over():
        display_game(game)
        move = input("Enter move (W/A/S/D): ").upper()

        if move == "W":
            game.move(0, -1)
        elif move == "A":
            game.move(-1, 0)
        elif move == "S":
            game.move(0, 1)
        elif move == "D":
            game.move(1, 0)

    print("Congratulations! You solved the puzzle.")


if __name__ == "__main__":
    main()
