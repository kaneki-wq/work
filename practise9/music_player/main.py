import pygame
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

player = MusicPlayer("music")

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((25, 25, 25))

    # ===== Отображение =====
    track_text = font.render(f"Track: {player.get_current_track()}", True, (255, 255, 255))
    screen.blit(track_text, (40, 80))

    status = "Stopped"
    if player.is_playing:
        status = "Playing"
    elif player.is_paused:
        status = "Paused"

    status_text = font.render(f"Status: {status}", True, (200, 200, 200))
    screen.blit(status_text, (40, 120))

    time_text = small_font.render(f"Time: {player.get_position()} sec", True, (180, 180, 180))
    screen.blit(time_text, (40, 160))

    controls = small_font.render("P=Play  S=Stop  N=Next  B=Back  SPACE=Pause  Q=Quit", True, (150, 150, 150))
    screen.blit(controls, (20, 220))

    pygame.display.flip()

    # ===== Автопереход =====
    if not pygame.mixer.music.get_busy() and player.is_playing and not player.is_paused:
        player.next_track()

    # ===== События =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.prev_track()

            elif event.key == pygame.K_SPACE:
                if player.is_playing:
                    player.pause()
                else:
                    player.play()

            elif event.key == pygame.K_q:
                running = False

    clock.tick(30)

pygame.quit()