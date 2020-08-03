def who_ate(snakes):
    for user in snakes:
        if user.snake[-1] == apple.apple:
            user.snake.appendleft(user.snake[0])
            apple.spawns.remove(user.snake[0])
            apple.make_rect(screen)
            break


def move_snake(user, other_user, typing="arrows"):
    user.get_user_move(move_type=typing)
    head, tail = user.snake[-1], user.snake[0]
    user.make_rect(screen, *tail, surface.color)
    user.make_rect(screen, *head, user.color)
    running = (
        apple.update_spawns(head, tail)
        and not user.in_itself()
        and not user.in_other(users.snake)
    )
    return running

