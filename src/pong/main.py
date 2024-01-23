import pygame
from paddle import Paddle


def main():
    game = Game()
    paddle = Paddle(50, game.height // 2 - 40)

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle.rect.y -= 5
        if keys[pygame.K_DOWN]:
            paddle.rect.y += 5

        game.screen.fill((0, 0, 0))
        paddle.draw(game.screen)
        pygame.display.flip()
        game.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
