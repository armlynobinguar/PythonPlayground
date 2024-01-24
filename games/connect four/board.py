from settings import *
import pygame as pg


class Board(pg.sprite.Sprite):
    def __init__(self, game, *groups) -> None:
        super().__init__(*groups)
        self.game = game
        self.image = pg.Surface(BOARD_SIZE)
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.rect.x = (WINDOW_SIZE[0] / 2) - (BOARD_SIZE[0] / 2)
        self.rect.y = WINDOW_SIZE[1] - BOARD_SIZE[1]
        self.create_cells()

    def create_cells(self):
        offset = 45
        for i in range(6):
            for j in range(7):
                pg.draw.circle(
                    self.image,
                    "black",
                    (
                        (offset + ((COIN_SIZE + 10) * j)),
                        (offset + ((COIN_SIZE + 10) * i)),
                    ),
                    COIN_SIZE / 2,
                )
