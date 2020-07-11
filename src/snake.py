import pygame
from collections import deque
from surface import Surface

WHITE = (255, 255, 255)
class Snake:
    """
    Creates the snake Object for the User to use
    """

    def __init__(self, screen, surface_data, x=1, y=0, color=WHITE):
        """
        --------
        :param
        self.x is the x vector
        sef.y is the y vector
        self.snake is a list representation of snake
        self._make_snake initializes snake on screen
        """
        self.color = color
        self.x = x
        self.y = y
        self.snake = deque([])
        self.rows, self.columns, self.blocksize = surface_data
        self._make_snake(screen)

    def _make_snake(self, screen, length=2):
        """
        Initialize a snake with a length of length on the screen
        """
        y = self.columns * self.blocksize // 2
        y = (y - self.blocksize//2, y)[self.columns % 2 == 0]
        for x in range(1, length + 1):
            rect = pygame.Rect(x * self.blocksize, y, self.blocksize, self.blocksize,)
            pygame.draw.rect(screen, self.color, rect)
            self.snake.append((x * self.blocksize, y))

    def get_user_move(self):
        """
        The moves the user makes
        self.x, self.y will give the direction to move on screen.
        """
        # key constants
        keys = pygame.key.get_pressed()
        LEFT = keys[pygame.K_LEFT]
        RIGHT = keys[pygame.K_RIGHT]
        DOWN = keys[pygame.K_DOWN]
        UP = keys[pygame.K_UP]
        head_x, head_y = self.x, self.y
        if any([UP, RIGHT, DOWN, LEFT]):
            # Takes user move
            # if user move goes opposite direction or
            # user move is same as where the snake is already going
            # no change in self.x, self.y
            self.x, self.y = ((0, 1), (1, 0))[LEFT or RIGHT]
            self.x, self.y = ((-self.x, -self.y), (self.x, self.y))[DOWN or RIGHT]
            self.x, self.y = ((head_x, head_y), (self.x, self.y))[
                self.x != head_x and self.y != head_y
            ]
        self.snake.append(
            (
                self.snake[-1][0] + self.x * self.blocksize,
                self.snake[-1][1] + self.y * self.blocksize,
            )
        )

    def move_snake(self, screen, cords, color):
        x, y = cords
        rect = pygame.Rect(x, y, self.blocksize, self.blocksize)
        pygame.draw.rect(screen, color, rect)
        pygame.display.update(rect)
    
    def in_itself(self):
        """ 
        return:
            Boolean --> running
        """
        if len(self.snake) != len(set(self.snake)):
            return False
        return True


if __name__ == "__main__":
    surface = Surface()
    screen = surface.make_screen()
    snake = Snake(screen, surface.snake_data)
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(float('inf'))
        snake.get_user_move()
        pygame.time.wait(100)
        tail = snake.snake.popleft()
        snake.move_snake(screen, tail, (0, 0, 0))
        snake.move_snake(screen, snake.snake[-1], (255, 255, 255))
    
