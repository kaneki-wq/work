import pygame
import sys
import os
from clock import get_time_angles

def rotate_center(image, angle, x, y):
    """Функция для вращения картинки вокруг её центра"""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect

def main():
    pygame.init()
    
    # Размер окна
    WIDTH, HEIGHT = 800, 800 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    
    current_dir = os.path.dirname(__file__)
    images_dir = os.path.join(current_dir, "images")
    
    # Настройки размера рук (меняй эти числа, чтобы подогнать под циферблат)
    MIN_HAND_SCALE = 0.35  # Минутная рука
    SEC_HAND_SCALE = 0.25  # Секундная рука

    try:
        # 1. Загружаем и масштабируем циферблат
        bg = pygame.image.load(os.path.join(images_dir, "main-clock.png"))
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        
        # 2. Загружаем и масштабируем минутную руку
        orig_min = pygame.image.load(os.path.join(images_dir, "right-hand.png"))
        new_min_size = (int(orig_min.get_width() * MIN_HAND_SCALE), 
                        int(orig_min.get_height() * MIN_HAND_SCALE))
        hand_min_img = pygame.transform.scale(orig_min, new_min_size)
        
        # 3. Загружаем и масштабируем секундную руку
        orig_sec = pygame.image.load(os.path.join(images_dir, "left-hand.png"))
        new_sec_size = (int(orig_sec.get_width() * SEC_HAND_SCALE), 
                        int(orig_sec.get_height() * SEC_HAND_SCALE))
        hand_sec_img = pygame.transform.scale(orig_sec, new_sec_size)

    except pygame.error as e:
        print(f"Ошибка: не удалось найти картинки в папке images! {e}")
        return

    clock = pygame.time.Clock()

    while True:
        # Обработка выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 1. Логика: получаем углы
        min_angle, sec_angle = get_time_angles()

        # 2. Отрисовка
        screen.fill((255, 255, 255)) # Белый фон, чтобы видеть черный циферблат
        screen.blit(bg, (0, 0))      # Рисуем циферблат

        # Рисуем минутную руку
        rot_min, rect_min = rotate_center(hand_min_img, min_angle, WIDTH // 2, HEIGHT // 2)
        screen.blit(rot_min, rect_min)

        # Рисуем секундную руку
        rot_sec, rect_sec = rotate_center(hand_sec_img, sec_angle, WIDTH // 2, HEIGHT // 2)
        screen.blit(rot_sec, rect_sec)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()