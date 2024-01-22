import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        
        # Updated color of the bird to YELLOW
        self.image.fill((255, 255, 0))
        
        self.rect = self.image.get_rect(center=(width // 4, height // 2))
        self.velocity = 0

    def jump(self):
        self.velocity = -10

    def update(self):
        self.velocity += 0.5
        self.rect.y += self.velocity

        if self.rect.bottom > 400:
            self.rect.bottom = 400
            self.velocity = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
