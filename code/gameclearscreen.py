import pygame
import sys
from settings import *

class GameClearScreen:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.screen.get_size()
        pygame.display.set_caption("Game Clear Screen")

        # Load background image
        self.background_image = pygame.image.load('../data/background/options_bg.png').convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Load game clear image
        self.game_clear_image = pygame.image.load('../data/graphics text/game clear.png').convert_alpha()
        self.game_clear_image = pygame.transform.scale(self.game_clear_image, (600, 600))

        # Load exit button images
        self.exit_button = pygame.image.load('../data/button/exit_btn.png').convert_alpha()
        self.exit_button = pygame.transform.scale(self.exit_button, (400, 200))
        self.exit_animation_button = pygame.image.load('../data/button/exit_an_btn.png').convert_alpha()
        self.exit_animation_button = pygame.transform.scale(self.exit_animation_button, (400, 200))

        # Calculate positions
        self.game_clear_rect = self.game_clear_image.get_rect(midtop=(self.SCREEN_WIDTH // 2, 50))
        self.exit_button_rect = self.exit_button.get_rect(midtop=(self.SCREEN_WIDTH // 2, self.game_clear_rect.bottom - 20))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.exit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            # Check for mouse hover
            mouse_pos = pygame.mouse.get_pos()
            if self.exit_button_rect.collidepoint(mouse_pos):
                exit_image = self.exit_animation_button
            else:
                exit_image = self.exit_button

            # Draw everything
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.game_clear_image, self.game_clear_rect.topleft)
            self.screen.blit(exit_image, self.exit_button_rect.topleft)
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game_clear_screen = GameClearScreen()
    game_clear_screen.run()
