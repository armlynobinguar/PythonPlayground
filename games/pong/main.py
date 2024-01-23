import pygame
from game import Game
from paddle import Paddle

def main():
    pygame.init()

    game = Game()
    paddle = Paddle(300, 160)  # Adjust the initial position as needed

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        # Update logic for the paddle, e.g., paddle.move(), etc.
        # Draw the paddle
        paddle.draw(game.screen)

        game.screen.fill((0, 0, 0))
        pygame.display.flip()
        game.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
