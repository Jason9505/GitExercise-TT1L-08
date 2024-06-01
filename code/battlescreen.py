import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Create screen in full screen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("Battle Screen")

# Load background image
background_image = pygame.image.load('../graphics/img/forest.jpeg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Character and Enemy images
character_image = pygame.image.load('../graphics/img/mc.png').convert_alpha()
character_image = pygame.transform.scale(character_image, (200, 300))  # Increase size

enemy_image = pygame.image.load('../graphics/img/monster lvl 1 solo.png').convert_alpha()  # Adjust the path
enemy_image = pygame.transform.scale(enemy_image, (200, 300))  # Increase size

# Load attack button images
attack1_image = pygame.image.load('../graphics/img/sword1.png').convert_alpha()
attack1_image = pygame.transform.scale(attack1_image, (150, 100))  # Increase size
attack2_image = pygame.image.load('../graphics/img/spear.png').convert_alpha()
attack2_image = pygame.transform.scale(attack2_image, (150, 100))  # Increase size
attack3_image = pygame.image.load('../graphics/img/scythe.png').convert_alpha()
attack3_image = pygame.transform.scale(attack3_image, (150, 100))  # Increase size
attack4_image = pygame.image.load('../graphics/img/catalyst.png').convert_alpha()
attack4_image = pygame.transform.scale(attack4_image, (150, 100))  # Increase size

# Load attack options images (Example images)
option1_image = pygame.image.load('../graphics/img/sword.png').convert_alpha()
option1_image = pygame.transform.scale(option1_image, (100, 50))  # Adjust size
option2_image = pygame.image.load('../graphics/img/shield.png').convert_alpha()
option2_image = pygame.transform.scale(option2_image, (100, 50))  # Adjust size

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
    pygame.draw.rect(screen, GREEN, fill)  # Green for player health bar
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

# Game states
NORMAL = 0
ATTACK_SELECTION = 1
ENEMY_TURN = 2
current_state = NORMAL

# Selected attack type
selected_attack = None

# Function for enemy attack
def enemy_attack():
    global player_hp
    damage = random.randint(5, 15)
    player_hp -= damage
    print(f"Enemy attacks! Player takes {damage} damage.")

# Main game loop with interactions
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Define button areas
            attack1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150, 150, 100)
            attack2_rect = pygame.Rect(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150, 150, 100)
            attack3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150, 150, 100)
            attack4_rect = pygame.Rect(SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150, 150, 100)

            if current_state == NORMAL:
                # Check if buttons are clicked
                if attack1_rect.collidepoint(x, y):
                    selected_attack = 1
                    current_state = ATTACK_SELECTION
                elif attack2_rect.collidepoint(x, y):
                    selected_attack = 2
                    current_state = ATTACK_SELECTION
                elif attack3_rect.collidepoint(x, y):
                    selected_attack = 3
                    current_state = ATTACK_SELECTION
                elif attack4_rect.collidepoint(x, y):
                    selected_attack = 4
                    current_state = ATTACK_SELECTION
            elif current_state == ATTACK_SELECTION:
                # Define attack options areas
                option1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 100, 50)
                option2_rect = pygame.Rect(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 25, 100, 50)
                
                # Check if options are clicked
                if option1_rect.collidepoint(x, y):
                    if selected_attack == 1:
                        enemy_hp -= 10  # Attack 1 option 1 effect
                    elif selected_attack == 2:
                        enemy_hp -= 20  # Attack 2 option 1 effect
                    elif selected_attack == 3:
                        enemy_hp -= 15  # Attack 3 option 1 effect
                    elif selected_attack == 4:
                        enemy_hp -= 5   # Attack 4 option 1 effect
                    current_state = ENEMY_TURN
                elif option2_rect.collidepoint(x, y):
                    if selected_attack == 1:
                        enemy_hp -= 15  # Attack 1 option 2 effect
                    elif selected_attack == 2:
                        enemy_hp -= 25  # Attack 2 option 2 effect
                    elif selected_attack == 3:
                        enemy_hp -= 20  # Attack 3 option 2 effect
                    elif selected_attack == 4:
                        enemy_hp -= 10  # Attack 4 option 2 effect
                    current_state = ENEMY_TURN

    if current_state == ENEMY_TURN:
        enemy_attack()
        current_state = NORMAL

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw enemy at the top right
    enemy_x = SCREEN_WIDTH - 250
    enemy_y = 50
    screen.blit(enemy_image, (enemy_x, enemy_y))
    draw_enemy_health_bar(screen, enemy_x + 50, enemy_y - 20, enemy_hp, 100)  # Centered above the enemy

    # Draw character at the bottom left
    character_x = 50
    character_y = SCREEN_HEIGHT - 350
    screen.blit(character_image, (character_x, character_y))
    draw_player_health_bar(screen, character_x + 50, character_y - 20, player_hp, 100)  # Centered above the player

    if current_state == NORMAL:
        # Action buttons
        screen.blit(attack1_image, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150))
        screen.blit(attack2_image, (SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150))
        screen.blit(attack3_image, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150))
        screen.blit(attack4_image, (SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150))
    elif current_state == ATTACK_SELECTION:
        # Attack options
        screen.blit(option1_image, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25))
        screen.blit(option2_image, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 25))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
