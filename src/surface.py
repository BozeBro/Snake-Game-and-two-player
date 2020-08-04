import pygame
from colors import *


class Surface:
    """
    Handles functions that interact with the screen including:
    drawing to the screen
    creating the screen
    """

    def __init__(
        self, rows=17, columns=17, blocksize=20, caption="Snake Game", color=WHITE
    ):
        """
        :param:
        (rows=17, columns=17, blocksize=20, caption="Snake Game")
        rows - tells how many rows there will be
        columns - tells how many columns there will be
        blocksize - tells how big a square
        caption - tells what the title in the game window
        color - tells what the color of screen is
        """
        # constants
        self.rows = rows
        self.columns = columns
        self.blocksize = blocksize
        self.caption = caption
        self.color = color

    def make_screen(self):
        """
        Initializes the screen object where the game is played.
        Only used at runtime, or when game plays
        """
        self.screen = pygame.display.set_mode(
            (self.rows * self.blocksize, self.columns * self.blocksize)
        )
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.color)

    def make_rect(self, x, y, color, **kwargs):
        """ 
        Used by apple and snake object.
        Draws a rectangle onto the screen.
        """
        rect = pygame.Rect(x, y, self.blocksize, self.blocksize)
        pygame.draw.rect(self.screen, color, rect, **kwargs)
        pygame.display.update(rect)


if __name__ == "__main__":
    # Test for creation of the screen
    pygame.init()
    surface = Surface(color=WHITE)
    surface.make_screen()
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
