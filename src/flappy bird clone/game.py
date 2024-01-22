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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.bird.jump()

    def spawn_pipes(self):
        if random.randint(1, 100) == 1:
            pipe_height = random.randint(100, self.HEIGHT - 100)
            self.pipes.add(Pipe(self.WIDTH, pipe_height))
            self.pipes.add(Pipe(self.WIDTH, self.HEIGHT - pipe_height, is_top=False))

    def main(self):  # Change the method name to 'main'
        while True:
            self.handle_events()
            self.spawn_pipes()

            self.all_sprites.update()

            # Check for collisions
            if pygame.sprite.spritecollide(self.bird, self.pipes, False):
                pygame.quit()
                sys.exit()

            # Draw everything
            self.screen.fill(self.RED)  # Set the background color to RED
            self.all_sprites.draw(self.screen)
            self.pipes.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.FPS)
