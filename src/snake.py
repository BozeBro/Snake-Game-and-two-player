from collections import deque
import pygame
from surface import Surface
from colors import *


class Snake(Surface):
    def __init__(
        self,
        screen,
        surface_data,
        x=1,
        y=0,
        typing="arrows",
        color=WHITE,
        pos=(1, 2, 1),
    ):
        """
        --------
        :param
        x is the x vector
        y is the y vector
        surface_data is the attributes from the Surface instance
        color for color of snake. default color is white
        self.snake is a list representation of snake

        self._make_snake initializes snake on screen
        """
        super().__init__(*surface_data)
        self.screen = screen
        self.x = x
        self.y = y
        self.typing = typing
        self.snake = None
        self.color = color
        self._make_snake(pos)

    def __len__(self):
        return max(1, len(self.snake))

    def _make_snake(self, pos):
        """
        Initialize a snake with a length of length on the screen

        :param
        pos is x position of the snake and range arguments.
        """
        self.snake = deque([])
        y = self.columns * self.blocksize // 2
        y = (y - self.blocksize // 2, y)[self.columns % 2 == 0]
        for x in range(*pos):
            self.make_rect(x * self.blocksize, y * self.blocksize, self.color)
            self.snake.append((x * self.blocksize, y))

    def get_user_move(self):
        """
        The move the user makes
        Will append the new square the snake in self.snake
        Handles illegal moves and insignificant moves 
            (Moving left while snake already going left)
        """
        # left, right, down, up. key formation
        keys = pygame.key.get_pressed()
        move_types = {
            "arrows": (
                keys[pygame.K_LEFT],
                keys[pygame.K_RIGHT],
                keys[pygame.K_DOWN],
                keys[pygame.K_UP],
            ),
            "letters": (
                keys[pygame.K_a],
                keys[pygame.K_d],
                keys[pygame.K_s],
                keys[pygame.K_w],
            ),
        }
        # key constants
        LEFT, RIGHT, DOWN, UP = move_types[self.typing]
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
        return len(set(self.snake)) != len(self.snake)

    def in_other(self, snake):
        return self.snake[-1] in set(snake)


if __name__ == "__main__":
    surface = Surface()
    screen = surface.make_screen()
    snake = Snake(screen, {"rows": 10, "columns": 10, "blocksize": 30}.values())
    snakely = Snake(
        screen,
        {"rows": 10, "columns": 10, "blocksize": 30}.values(),
        color=RED,
        pos=(4, 7, 1),
    )
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    snake.make_rect(screen, *snake.snake[-1], snake.color)
    snakely.make_rect(screen, *snakely.snake[-1], snakely.color)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(float("inf"))
        snake.get_user_move()
        pygame.time.wait(100)
        tail = snake.snake.popleft()
        # snake.make_rect(screen, *snake.snake[-1], WHITE)
        # snake.make_rect(screen, *tail, BLACK)
