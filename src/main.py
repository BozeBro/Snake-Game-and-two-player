from random import randint
import pygame
from apple import Apple
from surface import Surface
from snake import Snake

# Color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)

wait_time = 100
clock = pygame.time.Clock()

surface = Surface(color=BLUE)
screen = surface.make_screen()
snake = Snake(screen, surface.surface_data, color=MAGENTA)
apple = Apple(snake.snake, surface.surface_data)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(float("inf"))
    snake.get_user_move()
    pygame.time.wait(wait_time)
    # allow user the time to make a move
    tail = snake.snake.popleft()
    if not apple.exists:
        snake.snake.appendleft(tail)
        apple.spawn_apple(
            screen, surface.rows, surface.columns, surface.blocksize, apple.color
        )
    snake.move_snake(screen, tail, surface.color)
    snake.move_snake(screen, snake.snake[-1], snake.color)
    running = (False, True)[
        apple.update(snake.snake[-1], tail) and snake.in_itself()
        ]
    # update() updates available cords for apple spawns and checks for wall collision
    # in_itself() checks snake collision with its body
print("FINISHED")

