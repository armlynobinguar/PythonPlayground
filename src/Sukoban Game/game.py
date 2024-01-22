# game.py
class SokobanGame:
    def __init__(self, level):
        self.level = level
        self.player_position = None
        self.boxes = []
        self.targets = []

        self.load_level()

    def load_level(self):
        for y, row in enumerate(self.level):
            for x, char in enumerate(row):
                if char == "P":
                    self.player_position = (x, y)
                elif char == "B":
                    self.boxes.append((x, y))
                elif char == "T":
                    self.targets.append((x, y))

    def move(self, dx, dy):
        new_position = (self.player_position[0] + dx, self.player_position[1] + dy)

        if new_position not in self.boxes and self.is_valid_move(new_position):
            self.player_position = new_position

        if new_position in self.boxes:
            new_box_position = (new_position[0] + dx, new_position[1] + dy)
            if new_box_position not in self.boxes and self.is_valid_move(new_box_position):
                self.player_position = new_position
                self.boxes.remove(new_position)
                self.boxes.append(new_box_position)

    def is_valid_move(self, position):
        x, y = position
        return 0 <= x < len(self.level[0]) and 0 <= y < len(self.level) and self.level[y][x] != "#"

    def is_game_over(self):
        return all(box in self.targets for box in self.boxes)
