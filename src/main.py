from random import randint
import pygame
from apple import Apple
from surface import Surface
from snake import Snake


def game():
    # Color constants
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    MAGENTA = (255, 0, 255)

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
        running = (False, True)[apple.update_spawns(head, tail) and snake.in_itself()]
        # update() updates available cords for apple spawns and checks for wall collision
        # in_itself() checks snake collision with its body
        if not apple.exists:
            # handles when snake eats an apple
            snake.snake.appendleft(tail)
            apple.spawns.remove(tail)
            apple.make_rect(screen)
    if len(snake) == surface.rows * surface.columns: print("You won") 
    print(f"snake length was {len(snake)}!")


if __name__ == "__main__":
    game()
