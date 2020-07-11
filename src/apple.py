import random
import sys
import pygame
RED = (255, 0, 0)
class Apple:
    def __init__(self, snake, surface_data):
        self.color = RED
        self.spawns = []
        self.exists = 0
        self.apple = None
        self.valid_spawns(snake, *surface_data)

    def valid_spawns(self, snake, rows, columns, blocksize):
        """
        Finds valid spawn points for apple
        Does not include snake
        """
        for y in range(columns):
            for x in range(rows):
                cord_x, cord_y = x * blocksize, y * blocksize
                if (cord_x, cord_y) not in snake:
                    self.spawns.append((cord_x, cord_y))

    def spawn_apple(self, screen, rows, columns, blocksize, color):
        """
        Creates the apple object onto the screen object
        """
        x, y = self.spawns[random.randint(0, len(self.spawns) - 1)]
        rect = pygame.Rect(x, y, blocksize, blocksize)
        pygame.draw.rect(screen, color, rect)
        pygame.display.update(rect)
        self.exists = 1
        self.apple = (x, y)

    def update(self, head, tail):
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


