import pygame

from settings import *
from snake import Snake
from food import Food

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

# Создание объектов
snake = Snake()
food = Food(snake.body)

score = 0
level = 1
speed = START_SPEED

game_over = False


# Функция перезапуска
def reset_game():

    global snake, food
    global score, level
    global speed, game_over

    snake = Snake()
    food = Food(snake.body)

    score = 0
    level = 1
    speed = START_SPEED

    game_over = False


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_over:

                # Retry
                if event.key == pygame.K_r:
                    reset_game()

            else:
                snake.change_direction(event.key)

    if not game_over:

        # Движение
        new_head = snake.move()

        head_x, head_y = new_head

        # Столкновение со стеной
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            game_over = True

        # Столкновение с собой
        if snake.check_self_collision():
            game_over = True

        # Проверка еды
        if new_head == food.position:

            score += 1

            snake.grow()

            # Новый уровень
            if score % FOOD_PER_LEVEL == 0:
                level += 1
                speed += 2

            food = Food(snake.body)

    # Отрисовка
    screen.fill(BLACK)

    if game_over:

        game_over_text = font.render(
            "GAME OVER",
            True,
            RED
        )

        retry_text = font.render(
            "Press R to Retry",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            (WIDTH // 2 - 80, HEIGHT // 2 - 20)
        )

        screen.blit(
            retry_text,
            (WIDTH // 2 - 100, HEIGHT // 2 + 20)
        )

    else:

        # Рисуем рамку
        pygame.draw.rect(
            screen,
            WHITE,
            (0, 0, WIDTH, HEIGHT),
            2
        )

        snake.draw(screen)
        food.draw(screen)

        score_text = font.render(
            f"Score: {score}",
            True,
            WHITE
        )

        level_text = font.render(
            f"Level: {level}",
            True,
            WHITE
        )

        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
