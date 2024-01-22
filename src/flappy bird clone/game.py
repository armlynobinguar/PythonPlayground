import pygame
import sys
import random
from bird import Bird
from pipe import Pipe

class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 600, 400
        self.FPS = 30
        self.GRAVITY = 0.5
        self.BIRD_JUMP = -10
        self.PIPE_SPEED = 5

        # Updated colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)

        # Pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        # Game entities
        self.bird = Bird(self.WIDTH, self.HEIGHT)
        self.pipes = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bird)
