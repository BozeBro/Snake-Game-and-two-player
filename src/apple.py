import random
import sys
import pygame
from surface import Surface

RED = (255, 0, 0)
class Apple(Surface):
    def __init__(self, snake, surface_data, **kwargs):
        super().__init__(*surface_data)
        self.apple = None
        self.exists = 0
        self.spawns = []
        self.color = kwargs.get("color", RED)
        self._make_spawns(snake)

    def _make_spawns(self, snake):
        """
        Only used at initialization
        Finds valid spawn points for apple
        Does not include snake
        """
        for y in range(self.columns):
            for x in range(self.rows):
                cord_x, cord_y = x * self.blocksize, y * self.blocksize
                if (cord_x, cord_y) not in snake:
                    self.spawns.append((cord_x, cord_y))

    def make_apple(self, screen):
        """
        Creates the apple object onto the screen object
        """
        x, y = self.spawns[random.randint(0, len(self.spawns) - 1)]
        rect = pygame.Rect(x, y, self.blocksize, self.blocksize)
        pygame.draw.rect(screen, self.color, rect)
        pygame.display.update(rect)
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
            if head == self.apple:
                self.exists = 0
        except ValueError:
            return False
        return True


