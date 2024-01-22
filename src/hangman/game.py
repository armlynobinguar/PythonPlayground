# game.py
import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = ""
        self.guess_word = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def choose_word(self):
        self.secret_word = random.choice(self.word_list)
        self.guess_word = ["_"] * len(self.secret_word)
        self.attempts_left = self.max_attempts

    def make_guess(self, letter):
        if letter in self.secret_word:
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == letter:
                    self.guess_word[i] = letter
            return True
        else:
            self.attempts_left -= 1
            return False

    def is_game_over(self):
        return self.attempts_left == 0 or "_" not in self.guess_word

    def get_current_state(self):
        return {
            "secret_word": self.secret_word,
            "guess_word": " ".join(self.guess_word),
            "attempts_left": self.attempts_left
        }
