import pygame
import sys
from ball import Ball

def main():
    pygame.init()
    
    # Настройки экрана
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball")
    
    clock = pygame.time.Clock()
    ball = Ball(WIDTH, HEIGHT)
    
    running = True
    while running:
        # 1. Очистка экрана (белый фон)
        screen.fill((255, 255, 255))
        
        # 2. Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move((0, -ball.step))
                elif event.key == pygame.K_DOWN:
                    ball.move((0, ball.step))
                elif event.key == pygame.K_LEFT:
                    ball.move((-ball.step, 0))
                elif event.key == pygame.K_RIGHT:
                    ball.move((ball.step, 0))

        # 3. Отрисовка
        ball.draw(screen)
        
        # 4. Обновление экрана
        pygame.display.flip()
        clock.tick(60)  # Ограничение до 60 кадров в секунду

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()