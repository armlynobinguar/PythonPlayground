import pygame
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self, width, height, is_top=True):
        super().__init__()
        self.image = pygame.Surface((50, height))
        
        # Updated color of the pipes to WHITE
        self.image.fill((255, 255, 255))
        
        self.rect = self.image.get_rect()
        if is_top:
            self.rect.topleft = (width, 0)
        else:
            self.rect.bottomleft = (width, height)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()
