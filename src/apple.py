import random
import sys
import pygame
from surface import Surface
from colors import *


class Apple(Surface):
    def __init__(self, snake, surface_data, color=RED):
        super().__init__(*surface_data)
        self.apple = None
        self.exists = 0
        self.spawns = []
        self.color = color
        self._make_spawns(snake)

    def _make_spawns(self, snake):
        """
        Only used at initialization
        Finds valid spawn points for apple
        Does not include snake
        """
        self.spawns = []
        for y in range(self.columns):
            for x in range(self.rows):
                cord_x, cord_y = x * self.blocksize, y * self.blocksize
                if (cord_x, cord_y) not in snake:
                    self.spawns.append((cord_x, cord_y))

    def make_rect(self, screen, **kwargs):
        """
        Creates the apple object onto the screen object
        all kwargs are sent to drawing the rectangle
        """
        x, y = self.spawns[random.randint(0, len(self.spawns) - 1)]
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
            self.exists = (0, 1)[head != self.apple]
        except ValueError:
            return False
        return True

