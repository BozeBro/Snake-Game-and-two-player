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
        :param
            (x, y) must be 1, -1, or 0
            x - the x vector
            y - the y vector
            surface_data - the attributes from the Surface instance
            color - color of snake
            self.snake - list representation of snake object

            self._make_snake initializes snake on screen
        """
        super().__init__(*surface_data)
        self.screen = screen
        self.x = x
        self.y = y
        self.typing = typing
        self.snake = None
        self.color = color
        self.snake = self._make_snake(pos)

    def __len__(self):
        return max(1, len(self.snake))

    def _make_snake(self, pos):
        """
        Initialize a snake with a length of length on the screen
        :param
            pos - x position of the snake and range arguments.
                pos[0] is the head cords. pos[-1] is the tail cords
        :return
            snake -> self.snake
        """
        y = self.columns * self.blocksize // 2
        # y - self.blocksize // 2 prevents snake being in partly 2 squares
        y = (y - self.blocksize // 2, y)[self.columns % 2 == 0]
        snake = deque([])
        for x in range(*pos):
            self.make_rect(x * self.blocksize, y * self.blocksize, self.color)
            snake.append((x * self.blocksize, y))
        return snake

    def get_user_move(self):
        """
        The move the user makes
        Will append the new square the snake in self.snake
        Handles illegal moves 
            like moving backwards
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
        # See if user played a move, else no change in direction
        if any([UP, RIGHT, DOWN, LEFT]):
            # Chooses whether user move is (left or right) or (down or up)
            self.x, self.y = ((0, 1), (1, 0))[LEFT or RIGHT]
            # From the choice of two, we figure out the user move
            self.x, self.y = ((-self.x, -self.y), (self.x, self.y))[DOWN or RIGHT]
            # See if the move is legal and changes snake direction
            self.x, self.y = ((head_x, head_y), (self.x, self.y))[
                self.x != head_x and self.y != head_y
            ]
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
    pygame.init()
    # Test to handle snake spawning and movement
    surface = Surface()
    surface.make_screen()
    snake = Snake(surface.screen, {"rows": 10, "columns": 10, "blocksize": 30}.values())
    snakely = Snake(
        surface.screen,
        {"rows": 10, "columns": 10, "blocksize": 30}.values(),
        color=RED,
        pos=(4, 7, 1),
    )
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    snake.make_rect(*snake.snake[-1], snake.color)
    snakely.make_rect(*snakely.snake[-1], snakely.color)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(float("inf"))
        snake.get_user_move()
        pygame.time.wait(100)
        tail = snake.snake.popleft()
        snake.make_rect(*snake.snake[-1], WHITE)
        snake.make_rect(*tail, BLACK)
