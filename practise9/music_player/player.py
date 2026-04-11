import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = [f for f in os.listdir(music_folder) if f.endswith((".wav", ".mp3"))]

        if not self.playlist:
            raise Exception("Папка music пуста!")

        self.current_index = 0
        self.is_playing = False
        self.is_paused = False

        self.load_track()

    def load_track(self):
        track_path = os.path.join(self.music_folder, self.playlist[self.current_index])
        pygame.mixer.music.load(track_path)

    def play(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            self.load_track()
            pygame.mixer.music.play()

        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def pause(self):
        pygame.mixer.music.pause()
        self.is_paused = True
        self.is_playing = False

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True
        self.is_paused = False

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True
        self.is_paused = False

    def get_current_track(self):
        return self.playlist[self.current_index]

    def get_position(self):
        # время в секундах
        return pygame.mixer.music.get_pos() // 1000