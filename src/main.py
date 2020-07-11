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

wait_time = 20
fps = float("inf")
clock = pygame.time.Clock()

game_values = {"rows": 10, "columns": 10, "blocksize": 30}.values()

surface = Surface(*game_values, color=BLUE, caption="Snake Game")
screen = surface.make_screen()
snake = Snake(screen, game_values, color=MAGENTA)
apple = Apple(snake.snake, game_values, color=RED)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    pygame.time.wait(wait_time)
    snake.get_user_move()
    pygame.time.wait(wait_time)
    # allow user time to make a move
    tail = snake.snake.popleft()
    if not apple.exists:
        snake.snake.appendleft(tail)
        apple.make_apple(screen)
    pygame.time.wait(wait_time)
    snake.move_snake(screen, tail, surface.color)
    snake.move_snake(screen, snake.snake[-1], snake.color)
    pygame.time.wait(wait_time)
    running = (False, True)[apple.update_spawns(snake.snake[-1], tail) and snake.in_itself()]
    pygame.time.wait(wait_time)
    # update() updates available cords for apple spawns and checks for wall collision
    # in_itself() checks snake collision with its body
print("FINISHED")
