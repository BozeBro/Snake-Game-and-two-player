import pygame

# color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Surface:
    """
    Class to produce the surface to play the game.
    Class methods are only used during runtime to produce the surface object
    """

    def __init__(self, rows=17, columns=17, blocksize=20, caption="Snake Game", color=BLACK):
        """
        :param:
            (rows=17, columns=17, blocksize=20, caption="Snake Game")
            rows tells how many rows there will be
            columns tells how many columns there will be
                Each row/column is a row/column of squares
            blocksize tells how big a square is in pixels(px)
            caption tells what the title in the game window
        self.surface_data
            attributes for snake object to inheret
        """
        # constants
        self.rows = rows
        self.columns = columns
        self.caption = caption
        self.blocksize = blocksize
        self.color = color
        self.surface_data = (self.rows, self.columns, self.blocksize)

    def make_screen(self, grid_color=WHITE):
        """
        Initializes the screen object where the game is played.
        param:
        grid_color
            color of the border of each square. Past into grid maker function
        squares
            Color of the squares
        return:
        grid maker object
        """
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.rows * self.blocksize, self.columns * self.blocksize)
        )
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.color)
        return self.screen
        # return self._make_grid(grid_color)

    def _make_grid(self, color=WHITE):
        """
        Turns the screen object into a grid.
        :param
        color
            color of the borders of each square
        :return
        screen object
        """

        for y in range(self.columns):
            for x in range(self.rows):
                rect = pygame.Rect(
                    x * self.blocksize,
                    y * self.blocksize,
                    self.blocksize,
                    self.blocksize,
                )
                pygame.draw.rect(self.screen, color, rect, 1)
                pygame.display.flip()
        return self.screen


if __name__ == "__main__":
    surface = Surface()
    surface.make_screen()
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
