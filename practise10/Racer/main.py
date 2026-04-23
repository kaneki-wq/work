import pygame
import random

from settings import *
from player import Player
from enemy import Enemy
from coin import Coin
from utils import load_image, load_sound

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Ultimate")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

background = load_image("assets/images/background.png", (WIDTH, HEIGHT))

coin_sound = load_sound("assets/sounds/coin.wav")
crash_sound = load_sound("assets/sounds/crash.wav")


def show_menu():
    while True:
        screen.fill(BLACK)

        t1 = font.render("Racer Game", True, WHITE)
        t2 = font.render("Press SPACE", True, WHITE)

        screen.blit(t1, (WIDTH//2 - 120, HEIGHT//2 - 50))
        screen.blit(t2, (WIDTH//2 - 120, HEIGHT//2))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                return True


def game():
    player = Player()

    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)

    for _ in range(3):
        e = Enemy()
        enemies.add(e)
        all_sprites.add(e)

    score = 0
    speed = BASE_SPEED
    bg_y = 0

    running = True
    while running:
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False

        player.move()
        speed += SPEED_INCREASE

        for enemy in enemies:
            enemy.move(speed)

        # монеты
        if random.randint(1, COIN_SPAWN_RATE) == 1:
            c = Coin()
            coins.add(c)
            all_sprites.add(c)

        for coin in coins:
            coin.move(speed)

        # сбор
        collected = pygame.sprite.spritecollide(player, coins, True)
        if collected:
            coin_sound.play()
        score += len(collected)

        # столкновение
        if pygame.sprite.spritecollideany(player, enemies):
            crash_sound.play()
            return score

        # фон
        bg_y += speed
        if bg_y >= HEIGHT:
            bg_y = 0

        screen.blit(background, (0, bg_y))
        screen.blit(background, (0, bg_y - HEIGHT))

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        text = font.render(f"Coins: {score}", True, WHITE)
        screen.blit(text, (WIDTH - 180, 20))

        pygame.display.flip()


def game_over(score):
    while True:
        screen.fill(BLACK)

        t1 = font.render(f"Game Over: {score}", True, WHITE)
        t2 = font.render("Press R", True, WHITE)

        screen.blit(t1, (WIDTH//2 - 120, HEIGHT//2 - 40))
        screen.blit(t2, (WIDTH//2 - 80, HEIGHT//2 + 10))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                return True


running = True

while running:
    if not show_menu():
        break

    score = game()

    if score is False:
        break

    if not game_over(score):
        break

pygame.quit()