import random

class GameLogic:
    def __init__(self):
        self.reset()

    def reset(self):
        self.matrix = [[0] * 4 for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.matrix[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.matrix[i][j] = 2 if random.random() < 0.9 else 4

    # Add methods for moving and merging tiles
    # Example: move_left(), move_right(), move_up(), move_down()
