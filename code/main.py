import pygame
import sys
import time
from settings import *
from level import Level
from button import *

# Initialize pygame
pygame.init()

# Screen setup
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Realm Redeemers: The Last Stand")

background_img_path = "../graphics/img/background.png"
background = pygame.image.load(background_img_path)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
options_bg = pygame.image.load(options_bg_img_path)
options_bg = pygame.transform.scale(options_bg, (WIDTH, HEIGHT))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load audio
pygame.mixer.music.load(background_music_path)
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
sound_effect = pygame.mixer.Sound(sound_effect_path)
sound_effect.set_volume(0.3)

# Main Game class
class Game:
    def __init__(self):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.current_page = "menu"
        self.sound_volume = 100
        self.graphics_quality = "High"
        self.controls = "WASD"

        # Create buttons
        self.start_button = Button(700, 430, start, start_animation, 1)
        self.options_button = Button(700, 550, options, options_animation, 1)
        self.exit_button = Button(700, 670, exit, exit_animation, 1)
        self.increase_sound_button = Button(WIDTH // 2 + 200, 290, pygame.image.load(volume_up_img_path), pygame.image.load(volume_up_img_path), 0.5)
        self.decrease_sound_button = Button(WIDTH // 2 - 270, 290, pygame.image.load(volume_down_img_path), pygame.image.load(volume_down_img_path), 0.5)

        # Typing text
        self.typing_text = "Welcome to Realm Redeemers: The Last Stand"
        self.font = pygame.font.SysFont(None, 60)
        self.text_surface = self.font.render('', True, white)
        self.text_rect = self.text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center by default
        self.typing_index = 0
        self.typing_start_time = 0

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos)

    def handle_mouse_click(self, pos):
        if self.current_page == "menu":
            if self.start_button.clicked(pos):
                self.current_page = "typing"
                self.typing_index = 0
                self.typing_start_time = pygame.time.get_ticks()
                sound_effect.play()
            elif self.options_button.clicked(pos):
                self.current_page = "options"
                sound_effect.play()
            elif self.exit_button.clicked(pos):
                pygame.quit()
                sys.exit()
        elif self.current_page == "options":
            if self.increase_sound_button.clicked(pos):
                self.sound_volume = min(100, self.sound_volume + 10)
                pygame.mixer.music.set_volume(self.sound_volume / 100)
                sound_effect.play()
            elif self.decrease_sound_button.clicked(pos):
                self.sound_volume = max(0, self.sound_volume - 10)
                pygame.mixer.music.set_volume(self.sound_volume / 100)
                sound_effect.play()
            elif self.exit_button.clicked(pos):
                self.current_page = "menu"
                sound_effect.play()

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.current_page == "menu":
            self.start_button.update(pos)
            self.options_button.update(pos)
            self.exit_button.update(pos)
        elif self.current_page == "options":
            self.increase_sound_button.update(pos)
            self.decrease_sound_button.update(pos)
            self.exit_button.update(pos)
        elif self.current_page == "typing":
            self.update_typing()

    def update_typing(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.typing_start_time >= 40:  # Adjust typing speed here
            if self.typing_index < len(self.typing_text):
                self.typing_index += 1
                self.typing_start_time = current_time
            else:
                time.sleep(1)
                self.current_page = "game"

    def draw(self):
        if self.current_page == "menu":
            self.screen.blit(background, (0, 0))
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
            self.start_button.draw(self.screen)
            self.options_button.draw(self.screen)
            self.exit_button.draw(self.screen)
        elif self.current_page == "options":
            self.screen.blit(options_bg, (0, 0))
            self.draw_options()
            self.increase_sound_button.draw(self.screen)
            self.decrease_sound_button.draw(self.screen)
            self.exit_button.draw(self.screen)
        elif self.current_page == "typing":
            self.screen.fill(black)
            text_surface = self.font.render(self.typing_text[:self.typing_index], True, white)
            self.screen.blit(text_surface, self.text_rect)
        elif self.current_page == "game":
            self.screen.fill((80, 167, 232))
            self.level.run()
            

    def draw_options(self):
        font = pygame.font.SysFont(None, 60)
        sound_text = font.render(f"Sound Volume: {self.sound_volume}", True, white)
        graphics_text = font.render(f"Graphics Quality: {self.graphics_quality}", True, white)
        controls_text = font.render(f"Controls: {self.controls}", True, white)

        self.screen.blit(sound_text, (WIDTH // 2 - sound_text.get_width() // 2, 300))
        self.screen.blit(graphics_text, (WIDTH // 2 - graphics_text.get_width() // 2, 400))
        self.screen.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, 500))

    def set_typing_text_position(self, x, y):
        self.text_rect.center = (x, y)

if __name__ == '__main__':
    game = Game()
    game.set_typing_text_position(WIDTH // 2 - 400, HEIGHT // 2)  # Adjust this to set position
    game.run()