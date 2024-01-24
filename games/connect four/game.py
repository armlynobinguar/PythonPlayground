import pygame as pg
from board import Board
from settings import *


class Game:
    def __init__(self) -> None:
        # Initialize the game settings
        pg.init()
        self.screen = pg.display.set_mode((720, 540))
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True
        self.sprites = pg.sprite.Group()
        self.board = Board(self, self.sprites)
        self.turn = 0
        self.players = ["red", "yellow"]
        self.stacks = [[], [], [], [], [], [], []]
        self.last_stack = -1

    def events(self):
        self.check_game()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    return
            if event.type == pg.MOUSEBUTTONDOWN:
                if not self.playing:
                    print("Game is finished. Someone won!")
                    return
                pos = pg.mouse.get_pos()
                relative_pos = (pos[0] - self.board.rect.left, pos[1] - self.board.rect.top)
                # Check if inside bound of grid
                if (relative_pos[0] > 0 and relative_pos[1] > 0) and (
                    relative_pos[0] < BOARD_SIZE[0] and relative_pos[1] < BOARD_SIZE[1]
                ):
                    self.add_coin(relative_pos)

    def update(self):
        self.sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.sprites.draw(self.screen)
        if not self.playing:
            self.display_game_over()
        pg.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pg.quit()

    def add_coin(self, relative_pos):
        # Stacks check for x
        # 5-85, 85-165, 165-245, 245-325, 325-405, 405-485, 485-565
        x, _ = relative_pos
        # Check which stack it hit
        if x >= 5 and x <= 85:
            stack_number = 0
        elif x > 85 and x <= 165:
            stack_number = 1
        elif x > 165 and x <= 245:
            stack_number = 2
        elif x > 245 and x <= 325:
            stack_number = 3
        elif x > 325 and x <= 405:
            stack_number = 4
        elif x > 405 and x <= 485:
            stack_number = 5
        else:
            stack_number = 6
        # Check if there is still space in the stack
        if len(self.stacks[stack_number]) < 6:
            # Draw circle and add
            offset = 45
            pos_x = offset + ((COIN_SIZE + 10) * stack_number)
            pos_y = (COIN_SIZE * 6 + 70) - (offset + ((COIN_SIZE + 10) * len(self.stacks[stack_number])))
            pg.draw.circle(self.board.image, self.players[self.turn % 2], (pos_x, pos_y), COIN_SIZE / 2)
            self.stacks[stack_number].append(self.players[self.turn % 2])
            self.turn += 1
        self.last_stack = stack_number

    def check_game(self):
        row = len(self.stacks[self.last_stack]) - 1
        # Check horizontal
        streak = 0
        largest_streak = 0
        for i in range(7):
            try:
                if self.stacks[i][row] == self.players[(self.turn - 1) % 2]:
                    streak += 1
                else:
                    if streak > largest_streak:
                        largest_streak = streak
                    streak = 0
            except Exception as _:
                if streak > largest_streak:
                    largest_streak = streak
                streak = 0
        if largest_streak == 4:
            self.playing = False
            return
        # Check if height is at least 4
        if row >= 3:
            # Check vertical
            stack = self.stacks[self.last_stack]
            if stack[-1] == stack[-2] and stack[-2] == stack[-3] and stack[-3] == stack[-4]:
                self.playing = False
                return
            # Check diagonal
            if self.last_stack >= 3:
                try:
                    if (
                        self.stacks[self.last_stack][row] == self.stacks[self.last_stack - 1][row - 1]
                        and self.stacks[self.last_stack - 1][row - 1] == self.stacks[self.last_stack - 2][row - 2]
                        and self.stacks[self.last_stack - 2][row - 2] == self.stacks[self.last_stack - 3][row - 3]
                    ):
                        self.playing = False
                        return
                except Exception as e:
                    pass
            if self.last_stack <= 1:
                try:
                    if (
                        self.stacks[self.last_stack][row] == self.stacks[self.last_stack + 1][row - 1]
                        and self.stacks[self.last_stack + 1][row - 1] == self.stacks[self.last_stack + 2][row - 2]
                        and self.stacks[self.last_stack + 2][row - 2] == self.stacks[self.last_stack + 3][row - 3]
                    ):
                        self.playing = False
                        return
                except Exception as e:
                    pass

    def display_game_over(self):
        overlay = pg.Surface(WINDOW_SIZE)
        overlay.fill((0, 0, 0))
        overlay.set_alpha(60)
        self.screen.blit(overlay, overlay.get_rect())
        # Text
        font = pg.font.Font(None, 32)
        text = font.render("Game over", True, "green")
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2)
        self.screen.blit(text, text_rect)
