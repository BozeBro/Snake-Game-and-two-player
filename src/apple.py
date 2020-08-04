import random
import sys
import pygame
from surface import Surface
from snake import Snake
from colors import *


class Apple(Surface):
    def __init__(self, screen, snakes, surface_data, color=RED):
        """
        :param
            surface_data(iterable) - obtains rows, columns, and blocksize from a surface instance
            snakes(iterable) - all the snake player objects
            self.spawns(list) - valid places where an apple can spawn
            color(tuple) - color of the apple
        """
        self.screen = screen
        super().__init__(*surface_data)
        self.color = color
        self.spawns = self.make_spawns(snakes)

    def make_spawns(self, snakes):
        """
        Only used at initialization
        Finds valid spawn points for apple
        Creates spawns attribute
        :param
            snakes(iterable) - tells where snake players occupy
        :return
            list of valid spawn coordinates -> self.spawns
        """
        snakes = [body for body in [user.snake for user in snakes if user]]
        return [
            (cord_x, cord_y)
            for y in range(self.columns)
            for x in range(self.rows)
            if ((cord_x := x * self.blocksize), (cord_y := y * self.blocksize))
            not in snakes
        ]

    def make_rect(self, **kwargs):
        """
        Creates the apple object onto the screen object
        :param
            **kwargs - sent to drawing the rectangle
        self.exists(0 or 1) - tells if apple is eaten or not
        self.apple((int, int)) - tells the coordinates of the apple
        """
        x, y = self.spawns[random.randint(0, len(self.spawns) - 1)]
        super().make_rect(x, y, self.color, **kwargs)
        self.exists = 1
        self.apple = (x, y)

    def update_spawns(self, head, tail):
        """
        update available moves where apple can spawn.
        Handles wall collision via non-existent index in remove()
        Finds if apple has been eaten or not
        Turnary is used to stop overidding
        :param
            head - tells the front of the snake
            tail - Tells the back of the snake
        :return
            Boolean -> running
        """
        try:
            self.spawns.append(tail)
            # error in remove method if snake out of grid.
            self.spawns.remove(head)
            # self.exists in conditional to keep
            # self.exists False if already false
            self.exists = (0, 1)[head != self.apple and self.exists]
        except ValueError:
            return False
        return True


if __name__ == "__main__":
    # Test for the creation of an apple
    pygame.init()
    game_values = {"rows": 30, "columns": 30, "blocksize": 10}.values()
    surface = Surface(*game_values, caption="Snake Game", color=BLUE)
    surface.make_screen()
    apple = Apple(surface.screen, [snake], game_values, color=RED)
    apple.make_rect()
    running = True
    end = False
    while running and not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

