# main.py
from game import HangmanGame
from player import HangmanPlayer

def play_hangman():
    word_list = ["PYTHON", "JAVA", "HTML", "CSS", "JAVASCRIPT"]
    player = HangmanPlayer()
    hangman_game = HangmanGame(word_list)

    while True:
        hangman_game.choose_word()

        while not hangman_game.is_game_over():
            print("Current State:", hangman_game.get_current_state()["guess_word"])
            guess = player.get_guess()
            if hangman_game.make_guess(guess):
                print("Correct!")
            else:
                print("Incorrect! Attempts left:", hangman_game.get_current_state()["attempts_left"])

        print("Game Over!")
        if "_" not in hangman_game.guess_word:
            print("Congratulations! You guessed the word:", hangman_game.get_current_state()["secret_word"])
        else:
            print("Sorry! The word was:", hangman_game.get_current_state()["secret_word"])

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    play_hangman()
