from random import randint
import pygame
from apple import Apple
from surface import Surface
from snake import Snake
from colors import *


def game():
    """
    Overview
    -------------
    Surface controls game screen and the parent class of the Snake and Apple class
        It controls creation of the game screen and 
        making drawings on the game screen that the user sees
    The Snake class controls initialization of the snake onto the game screen
        It handles a user's moves and passes it to the Surface class to make into a drawing
        It handles whenever the snake collides with itself on the game screen
    The Apple class controls the location of apple spawns
        It will pass a decided spawn location to the Surface clas to make into a drawing
        It holds a list to store valid spawns and updates valid spawns after every move
        It handles whenever the snake collides into the border of the screen.
    """
    # time variables
    wait_time = 100
    fps = 30
    clock = pygame.time.Clock()

    game_values = {"rows": 10, "columns": 10, "blocksize": 30}.values()
    # Initializing objects
    surface = Surface(*game_values, caption="Snake Game", color=BLUE)
    screen = surface.make_screen()
    snake = Snake(screen, game_values, length=1, color=GREEN)
    apple = Apple(snake.snake, game_values, color=RED)
    apple.make_rect(screen)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(fps)
        pygame.time.wait(wait_time)
        # allow user time to make a move
        snake.get_user_move()
        tail = snake.snake.popleft()
        snake.make_rect(screen, *tail, surface.color)
        snake.make_rect(screen, *(head := snake.snake[-1]), snake.color)
        running = apple.update_spawns(head, tail) and snake.in_itself()
        # update() updates available cords for apple spawns and checks for wall collision
        # in_itself() checks snake collision with its body
        if not apple.exists:
            # handles when snake eats an apple
            snake.snake.appendleft(tail)
            apple.spawns.remove(tail)
            apple.make_rect(screen)
    print(f"snake length was {len(snake)}!")
    if len(snake) == surface.rows * surface.columns:
        print("You won")


if __name__ == "__main__":
    game()
