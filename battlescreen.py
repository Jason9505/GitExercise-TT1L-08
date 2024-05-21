import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create screen in full screen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("Battle Screen")

# Load background image
background_image = pygame.image.load('img/forest.jpeg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Character and Enemy placeholders
character = pygame.Surface((100, 150))
character.fill(BLACK)

enemy = pygame.Surface((100, 150))
enemy.fill(BLACK)

# Player and Enemy HP
player_hp = 100
enemy_hp = 100

# Function to draw health bars
def draw_health_bar(screen, x, y, current_hp, max_hp):
    BAR_WIDTH = 100
    BAR_HEIGHT = 10
    fill = (current_hp / max_hp) * BAR_WIDTH
    border = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(screen, (255, 0, 0), fill)
    pygame.draw.rect(screen, BLACK, border, 2)

# Main game loop with interactions
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if mid_screen_x - 150 < x < mid_screen_x - 50 and mid_screen_y < y < mid_screen_y + 50:
                enemy_hp -= 10
            elif mid_screen_x + 50 < x < mid_screen_x + 150 and mid_screen_y < y < mid_screen_y + 50:
                player_hp += 10
        


    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw enemy at the top right
    screen.blit(enemy, (SCREEN_WIDTH - 150, 50))
    draw_health_bar(screen, SCREEN_WIDTH - 150, 30, enemy_hp, 100)

    # Draw character at the bottom left
    screen.blit(character, (50, SCREEN_HEIGHT - 200))
    draw_health_bar(screen, 50, SCREEN_HEIGHT - 220, player_hp, 100)

# Action buttons (placeholders)
# Action buttons (placeholders)
    mid_screen_x = SCREEN_WIDTH // 2
    mid_screen_y = SCREEN_HEIGHT // 2
    pygame.draw.rect(screen, (0, 0, 255), (mid_screen_x - 150, mid_screen_y, 100, 50))  # Attack button
    pygame.draw.rect(screen, (0, 255, 0), (mid_screen_x + 50, mid_screen_y, 100, 50))  # Defend button


# Update display
pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
