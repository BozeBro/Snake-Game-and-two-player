import itertools
import random
import sys
import pygame
from surface import Surface
from snake import Snake
from colors import *


class Apple(Surface):
    def __init__(self, snakes, surface_data, color=RED):
        super().__init__(*surface_data)
        self.apple = None
        self.exists = [0 for i in snakes]
        self.spawns = []
        self.color = color
        self.make_spawns(snakes)

    def make_spawns(self, snakes):
        """
        Only used at initialization
        Finds valid spawn points for apple
        Does not include snake
        """
        snakes = [body for body in [user.snake for user in snakes if user]]

        self.spawns = []
        for y in range(self.columns):
            for x in range(self.rows):
                cord_x, cord_y = x * self.blocksize, y * self.blocksize
                if (cord_x, cord_y) not in snakes:
                    self.spawns.append((cord_x, cord_y))

    def make_rect(self, screen, **kwargs):
        """
        Creates the apple object onto the screen object
        all kwargs are sent to drawing the rectangle
        """
        x, y = self.spawns[random.randint(0, len(self.spawns) - 1)]
        # x, y = 15 * self.blocksize, 15 * self.blocksize
        super().make_rect(screen, x, y, self.color, **kwargs)
        self.exists = 1
        self.apple = (x, y)

    def update_spawns(self, head, tail):
        """
        update available moves where apple can spawn.
        Handles wall collision via non-existent index in remove()
        :return
            Boolean -> running
        """
        try:
            self.spawns.append(tail)
            self.spawns.remove(head)
            # error in remove method if snake out of grid.
            self.exists = (0, 1)[head != self.apple and self.exists]
        except ValueError:
            return False
        return True


if __name__ == "__main__":
    game_values = {"rows": 30, "columns": 30, "blocksize": 10}.values()
    surface = Surface(*game_values, caption="Snake Game", color=BLUE)
    screen = surface.make_screen()
    snake = Snake(screen, game_values, color=GREEN)
    apple = Apple(snake.snake, game_values, color=RED)
    apple.make_rect(screen)
    running = True
    end = False
    while running and not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

