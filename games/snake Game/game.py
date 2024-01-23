import pygame
import random
from snake import Snake

pygame.init()

white = (255, 255, 255)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

game_over = False
snake = Snake()

clock = pygame.time.Clock()
snake_speed = 15  # You can adjust the speed

def game_loop():
    global game_over
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_dir('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_dir('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.change_dir('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_dir('RIGHT')

        food_position = [random.randrange(1, (dis_width // 10)) * 10,
                         random.randrange(1, (dis_height // 10)) * 10]

        if snake.move(food_position):
            food_position = [random.randrange(1, (dis_width // 10)) * 10,
                             random.randrange(1, (dis_height // 10)) * 10]

        dis.fill(blue)

        for position in snake.get_body():
            pygame.draw.rect(dis, white, pygame.Rect(
                position[0], position[1], 10, 10))

        pygame.draw.rect(dis, (255, 0, 0), pygame.Rect(
            food_position[0], food_position[1], 10, 10))

        if snake.check_collision():
            game_over = True

        pygame.display.flip()

        clock.tick(snake_speed)  # Set the speed of the snake

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
