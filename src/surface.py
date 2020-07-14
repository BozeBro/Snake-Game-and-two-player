import pygame
from colors import *


class Surface:
    """
    Class to produce the surface to play the game.
    Class methods are only used during runtime to produce the surface object
    """

    def __init__(
        self, rows=17, columns=17, blocksize=20, caption="Snake Game", color=BLACK
    ):
        """
        :param:
            (rows=17, columns=17, blocksize=20, caption="Snake Game")
            rows tells how many rows there will be
            columns tells how many columns there will be
                Each row/column is a row/column of squares
            blocksize tells how big a square is in pixels(px)
            caption tells what the title in the game window
        """
        # constants
        self.rows = rows
        self.columns = columns
        self.blocksize = blocksize
        self.caption = caption
        self.color = color

    def make_screen(self, grid_color=WHITE):
        """
        Initializes the screen object where the game is played.
        param:
        grid_color
            color of the border of each square. Past into grid maker function
        """
        pygame.init()
        screen = pygame.display.set_mode(
            (self.rows * self.blocksize, self.columns * self.blocksize)
        )
        pygame.display.set_caption(self.caption)
        screen.fill(self.color)
        return screen

    def make_rect(self, screen, x, y, color, **kwargs):
        """ 
        Used by apple and snake object.
        Draws a rectangle onto the screen.
        """
        rect = pygame.Rect(x, y, self.blocksize, self.blocksize)
        pygame.draw.rect(screen, color, rect, **kwargs)
        pygame.display.update(rect)


if __name__ == "__main__":
    surface = Surface()
    surface.make_screen()
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
