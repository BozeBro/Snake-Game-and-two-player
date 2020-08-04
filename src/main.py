import sys
import os.path
import pygame
import utils
from apple import Apple
from surface import Surface
from snake import Snake
from colors import *


def home(game_values):
    """
    Home page of the game / GUI
    """
    width = rows * blocksize
    height = columns * blocksize
    # icon size constants
    i_width, i_height = width // 4 + (rows // 3), height // 4
    # icon position constants,
    # sg for single, and double,
    # sn for snake and help
    sg_width, sg_height = width // 10, height // 4 + height // 10
    sn_width, sn_height = width // 2 - (width + rows) // 6, i_height // 10
    # Initializing objects
    images = utils.load_images(os.path.dirname(__file__), i_width, i_height)
    surface = Surface(*game_values, caption="Snake Game", color=BLACK)
    surface.make_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        surface.screen.blit(
            images["single"], (sg_width, sg_height),
        )
        surface.screen.blit(
            images["double"], (width - (sg_width + i_width), sg_height),
        )
        surface.screen.blit(images["snake"], (sn_width, sn_height))
        # Highlighting an icon
        x, y = pygame.mouse.get_pos()
        if sg_height <= y <= sg_height + i_height:
            # single player
            if sg_width <= x <= sg_width + i_width:
                rect = pygame.Rect((sg_width, sg_height), (i_width, i_height))
                pygame.draw.rect(surface.screen, RED, rect, 3)
                if pygame.mouse.get_pressed()[0]:
                    return 1

            elif (
                width - (sg_width + i_width)
                <= x
                <= width - (sg_width + i_width) + i_width
            ):
                # double player
                rect = pygame.Rect(
                    (width - (sg_width + i_width), sg_height), (i_width, i_height)
                )
                pygame.draw.rect(surface.screen, RED, rect, 3)
                if pygame.mouse.get_pressed()[0]:
                    return 2
        pygame.display.flip()


def game(game_values, players=1):
    """
    Overview
    -------------
    Surface - controls game screen and the parent class of the Snake and Apple class
        It controls creation of the game screen and 
        making drawings on the game screen that the user sees
    Snake - controls initialization of the snake onto the game screen
        It handles a user's moves and passes it to the Surface class to make into a drawing
        It handles whenever the snake collides with itself on the game screen
    Apple - controls the location of apple spawns
        It will pass a decided spawn location to the Surface clas to make into a drawing
        It holds a list to store valid spawns and updates valid spawns after every move
        It handles whenever the snake collides into the border of the screen.
    
    :param
        players - controls amount of players in the game
    """

    def who_ate(snakes):
        """
        Finds the eating snake to add tail back, 
        update apple spawns and 
        make a new apple
        :param
            snakes(iterable) - gives the players
        """
        for user in snakes:
            if user.snake[-1] == apple.apple:
                user.snake.appendleft(user.snake[0])
                apple.spawns.remove(user.snake[0])
                apple.make_rect()
                break

    def move_snake(user, other_user, winner):
        """
        Moves the snake head, and updates apple spawns
        :param
            user - current snake to move
            other_user - other snake. Will be [] if single player
            winner - sets the winner to other_user if user dies/collides
        :return
            running, winner
        """
        if not user:
            return True
        other_user = other_user.snake if other_user else []
        user.get_user_move()
        head, tail = user.snake[-1], user.snake[0]
        user.make_rect(*tail, surface.color)
        user.make_rect(*head, user.color)
        running = (
            apple.update_spawns(head, tail)
            and not user.in_itself()
            and not user.in_other(other_user)
        )
        return running, winner

    # time variables
    wait_time = 100
    fps = 30
    clock = pygame.time.Clock()
    # Initializing objects
    surface = Surface(*game_values, caption="Snake Game", color=WHITE)
    surface.make_screen()
    snake = Snake(
        surface.screen,
        game_values,
        x=-1,
        pos=(surface.rows - 1, surface.rows - 2, -1),
        color=GREEN,
    )
    if players == 2:
        snake2 = Snake(surface.screen, game_values, typing="letters", color=MAGENTA)
    else:
        snake2 = []
    snakes = (snake, snake2)
    apple = Apple(surface.screen, snakes, game_values, color=RED)
    apple.make_rect()
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(fps)
        # allow user time to make a move
        pygame.time.wait(wait_time)
        # move() Handles self collision, collision with others, and ollision with walls
        running, winner = move_snake(snake, snake2, "snake2")
        if running and snake2:
            running, winner = move_snake(snake2, snake, "snake")
        # handles when a snake eats an apple
        if not apple.exists:
            who_ate(snakes)
        for player in snakes:
            # Remove tail of each snake
            if player:
                player.snake.popleft()
    if players == 1:
        if len(snake) == surface.rows * surface.columns:
            print("You won!")
        print(f"snake length was {len(snake)}!")
    elif players == 2:
        print(
            f"snake1 length was {len(snake)}!",
            f"snake2 length was {len(snake2)}!",
            f"The winner is {winner}!",
            sep="\n",
        )


if __name__ == "__main__":
    # screen constants
    rows, columns, blocksize = 30, 30, 20
    game_values = (rows, columns, blocksize)
    pygame.init()
    while True:
        players = home(game_values)
        game(game_values, players)
