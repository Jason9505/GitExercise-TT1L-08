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

# Create main screen in full screen mode
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

# Load option button images
option1_image = pygame.image.load('../graphics/img/sword1.png').convert_alpha()
option1_image = pygame.transform.scale(option1_image, (150, 100))  # Increase size
option2_image = pygame.image.load('../graphics/img/spear.png').convert_alpha()
option2_image = pygame.transform.scale(option2_image, (150, 100))  # Increase size
option3_image = pygame.image.load('../graphics/img/scythe.png').convert_alpha()
option3_image = pygame.transform.scale(option3_image, (150, 100))  # Increase size
option4_image = pygame.image.load('../graphics/img/catalyst.png').convert_alpha()
option4_image = pygame.transform.scale(option4_image, (150, 100))  # Increase size

# Load attack options images (Example images)
attack1_image = pygame.image.load('../graphics/img/sword.png').convert_alpha()
attack1_image = pygame.transform.scale(attack1_image, (100, 50))  # Adjust size
attack2_image = pygame.image.load('../graphics/img/shield.png').convert_alpha()
attack2_image = pygame.transform.scale(attack2_image, (100, 50))  # Adjust size

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
TUTORIAL = 3
current_state = NORMAL

# Selected attack type
selected_option = None

# Function for enemy attack
def enemy_attack():
    global player_hp
    damage = random.randint(5, 15)
    player_hp -= damage
    print(f"Enemy attacks! Player takes {damage} damage.")

# Function to end the game
def end_game():
    pygame.quit()
    sys.exit()

# Function to display tutorial window
def show_tutorial():
    tutorial_screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Tutorial")
    running_tutorial = True
    while running_tutorial:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_tutorial = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running_tutorial = False

        tutorial_screen.fill(WHITE)
        font = pygame.font.SysFont(None, 36)
        tutorial_text = font.render('Use the attack options to defeat the enemy!', True, BLACK)
        tutorial_screen.blit(tutorial_text, (30, 180))
        pygame.display.flip()

    pygame.display.quit()
    pygame.display.init()

# Define button areas outside the main loop
attack1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150, 150, 100)
attack2_rect = pygame.Rect(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150, 150, 100)
attack3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150, 150, 100)
attack4_rect = pygame.Rect(SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150, 150, 100)
tutorial_button_rect = pygame.Rect(10, 10, 150, 50)

# Main game loop with interactions
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if tutorial_button_rect.collidepoint(x, y):
                current_state = TUTORIAL
                show_tutorial()
                current_state = NORMAL
            if current_state == NORMAL:
                # Check if buttons are clicked
                if attack1_rect.collidepoint(x, y):
                    selected_option = 1
                    current_state = ATTACK_SELECTION
                elif attack2_rect.collidepoint(x, y):
                    selected_option = 2
                    current_state = ATTACK_SELECTION
                elif attack3_rect.collidepoint(x, y):
                    selected_option = 3
                    current_state = ATTACK_SELECTION
                elif attack4_rect.collidepoint(x, y):
                    selected_option = 4
                    current_state = ATTACK_SELECTION
            elif current_state == ATTACK_SELECTION:
                # Define attack options areas
                option1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 100, 50)
                option2_rect = pygame.Rect(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 25, 100, 50)
                
                # Check if options are clicked
                if option1_rect.collidepoint(x, y):
                    if selected_option == 1:
                        enemy_hp -= 10  # Option 1 attack 1 effect
                    elif selected_option == 2:
                        enemy_hp -= 20  # Option 1 attack 2 effect
                    elif selected_option == 3:
                        enemy_hp -= 15  # Option 1 attack 3 effect
                    elif selected_option == 4:
                        enemy_hp -= 5   # Option 1 attack 4 effect
                    current_state = ENEMY_TURN
                elif option2_rect.collidepoint(x, y):
                    if selected_option == 1:
                        enemy_hp -= 15  # Option 2 attack 1 effect
                    elif selected_option == 2:
                        enemy_hp -= 25  # Option 2 attack 2 effect
                    elif selected_option == 3:
                        enemy_hp -= 20  # Option 2 attack 3 effect
                    elif selected_option == 4:
                        enemy_hp -= 10  # Option 2 attack 4 effect
                    current_state = ENEMY_TURN

    if current_state == ENEMY_TURN:
        enemy_attack()
        current_state = NORMAL

    # Check for game over
    if player_hp <= 0 or enemy_hp <= 0:
        print("Game Over")
        end_game()

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

    # Action buttons
    screen.blit(option1_image, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150))
    screen.blit(option2_image, (SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150))
    screen.blit(option3_image, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150))
    screen.blit(option4_image, (SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150))
    
    if current_state == ATTACK_SELECTION:
        # Attack options
        screen.blit(attack1_image, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25))
        screen.blit(attack2_image, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 25))

    # Tutorial button
    pygame.draw.rect(screen, BLUE, tutorial_button_rect)
    font = pygame.font.SysFont(None, 36)
    tutorial_button_text = font.render('Tutorial', True, WHITE)
    screen.blit(tutorial_button_text, (20, 20))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
