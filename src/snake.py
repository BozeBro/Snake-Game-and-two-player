import pygame
from collections import deque
from surface import Surface

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Snake(Surface):
    """
    Creates the snake Object for the User to use
    """

    def __init__(self, screen, surface_data, x=1, y=0, color=WHITE, length=2, **kwargs):
        """
        --------
        :param
        x is the x vector
        y is the y vector
        screen is for _make_snake
        surface_data is the attributes from the Surface instance
        **kwargs
            color for color of snake. default color is white
        self.snake is a list representation of snake

        self._make_snake initializes snake on screen
        """
        super().__init__(*surface_data)
        self.x = x
        self.y = y
        self.snake = 0
        self.color = kwargs.get("color", color)
        self._make_snake(screen, kwargs.get("length", length))

    def __len__(self):
        return len(self.snake)

    def _make_snake(self, screen, length):
        """
        Initialize a snake with a length of length on the screen

        :param
        screen is the screen object that is drawn on
        length is snake length. default is 2
        """
        self.snake = deque([])
        y = self.columns * self.blocksize // 2
        y = (y - self.blocksize // 2, y)[self.columns % 2 == 0]
        for x in range(1, length + 1):
            super().make_rect(
                screen, x * self.blocksize, y * self.blocksize, self.color
            )
            self.snake.append((x * self.blocksize, y))

    def get_user_move(self):
        """
        The move the user makes
        Will append the new square the snake in self.snake
        Handles illegal moves and insignificant moves 
            (Moving left while snake already going left)
        """
        # key constants
        keys = pygame.key.get_pressed()
        LEFT = keys[pygame.K_LEFT]
        RIGHT = keys[pygame.K_RIGHT]
        DOWN = keys[pygame.K_DOWN]
        UP = keys[pygame.K_UP]
        head_x, head_y = self.x, self.y
        if any([UP, RIGHT, DOWN, LEFT]):
            # See if user played a move, else no change in direction
            self.x, self.y = ((0, 1), (1, 0))[LEFT or RIGHT]
            # Chooses whether user move is (left or right) or (down or up)
            self.x, self.y = ((-self.x, -self.y), (self.x, self.y))[DOWN or RIGHT]
            # From the choice of two, we figure out the user move
            self.x, self.y = ((head_x, head_y), (self.x, self.y))[
                self.x != head_x and self.y != head_y
            ]
            # If (user move = snake move) or (user tries to go backwards), then no change
        self.snake.append(
            (
                self.snake[-1][0] + self.x * self.blocksize,
                self.snake[-1][1] + self.y * self.blocksize,
            )
        )

    def in_itself(self):
        return len(set(self.snake)) == len(self.snake)


if __name__ == "__main__":
    surface = Surface()
    screen = surface.make_screen()
    snake = Snake(
        screen, {"rows": 10, "columns": 10, "blocksize": 30}.values(), length=1
    )
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(float("inf"))
        snake.get_user_move()
        pygame.time.wait(100)
        tail = snake.snake.popleft()
        snake.test_snake(screen, snake.snake[-1], WHITE)
        snake.test_snake(screen, tail, BLACK)
