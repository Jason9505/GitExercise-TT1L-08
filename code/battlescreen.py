import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Create screen in full screen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("Battle Screen")

# Load background image
background_image = pygame.image.load('../graphics/img/forest.jpeg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Character and Enemy placeholders
character_image = pygame.image.load('../graphics/img/mc.png').convert_alpha()
character_image = pygame.transform.scale(character_image, (100, 150))  # Adjust the size as needed

enemy = pygame.Surface((100, 150))
enemy.fill(BLACK)

# Player and Enemy HP
player_hp = 100
enemy_hp = 100

# Function to draw player health bar
def draw_player_health_bar(screen, x, y, current_hp, max_hp):
    BAR_WIDTH = 100
    BAR_HEIGHT = 10
    fill = (current_hp / max_hp) * BAR_WIDTH
    border = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(screen, GREEN, fill)  # Red for player health bar
    pygame.draw.rect(screen, BLACK, border, 2)

# Function to draw enemy health bar
def draw_enemy_health_bar(screen, x, y, current_hp, max_hp):
    BAR_WIDTH = 100
    BAR_HEIGHT = 10
    fill = (current_hp / max_hp) * BAR_WIDTH
    border = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(screen, RED, fill)  # Red for enemy health bar
    pygame.draw.rect(screen, BLACK, border, 2)

# Main game loop with interactions
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if SCREEN_WIDTH // 2 - 150 < x < SCREEN_WIDTH // 2 - 50 and SCREEN_HEIGHT - 100 < y < SCREEN_HEIGHT - 50:
                # Attack button clicked
                enemy_hp -= 10
            elif SCREEN_WIDTH // 2 + 50 < x < SCREEN_WIDTH // 2 + 150 and SCREEN_HEIGHT - 100 < y < SCREEN_HEIGHT - 50:
                if player_hp == 100:
                    player_hp += 0
                    # Defend button clicked
                else:
                    player_hp += 10
            # Add your custom button logic here (e.g., empty functions for extra buttons)

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw enemy at the top right
    screen.blit(enemy, (SCREEN_WIDTH - 150, 50))
    draw_enemy_health_bar(screen, SCREEN_WIDTH - 150, 30, enemy_hp, 100)

    # Draw character at the bottom left
    screen.blit(character_image, (50, SCREEN_HEIGHT - 200))
    draw_player_health_bar(screen, 50, SCREEN_HEIGHT - 220, player_hp, 100)

    # Action buttons (placeholders)
    pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 100, 100, 50))  # Attack button
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 100, 100, 50))  # Defend button
    # Add your custom buttons here (e.g., empty buttons)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
