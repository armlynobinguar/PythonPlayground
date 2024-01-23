import pygame

class Paddle:
    def __init__(self, x, y):
        self.width = 15
        self.height = 80
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
