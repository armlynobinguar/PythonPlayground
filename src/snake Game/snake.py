# snake.py

import pygame
import time

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.change_direction = self.direction

    def change_dir(self, new_dir):
        if new_dir == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if new_dir == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if new_dir == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if new_dir == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def move(self, food_position):
        if self.direction == 'RIGHT':
            self.position[0] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10

        self.body.insert(0, list(self.position))
        if self.position == food_position:
            return True
        else:
            self.body.pop()
            return False

    def check_collision(self):
        if self.position[0] >= 500 or self.position[0] <= 0 or \
           self.position[1] >= 500 or self.position[1] <= 0:
           return True
        for segment in self.body[1:]:
            if segment == self.position:
                return True
        return False

    def get_head_position(self):
        return self.position

    def get_body(self):
        return self.body

