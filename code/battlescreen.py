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
attack1_image = pygame.image.load('../graphics/img/weapon/sword1.png').convert_alpha()
attack1_image = pygame.transform.scale(attack1_image, (150, 100))  # Increase size
attack2_image = pygame.image.load('../graphics/img/weapon/spear.png').convert_alpha()
attack2_image = pygame.transform.scale(attack2_image, (150, 100))  # Increase size
attack3_image = pygame.image.load('../graphics/img/weapon/scythe.png').convert_alpha()
attack3_image = pygame.transform.scale(attack3_image, (150, 100))  # Increase size
attack4_image = pygame.image.load('../graphics/img/weapon/catalyst.png').convert_alpha()
attack4_image = pygame.transform.scale(attack4_image, (150, 100))  # Increase size

# Load attack options images (Example images)
option1_image = pygame.image.load('../graphics/img/sword.png').convert_alpha()
option1_image = pygame.transform.scale(option1_image, (100, 50))  # Adjust size
option2_image = pygame.image.load('../graphics/img/shield.png').convert_alpha()
option2_image = pygame.transform.scale(option2_image, (100, 50))  # Adjust size

# Load tutorial image
tutorial_image = pygame.image.load('../graphics/img/tutorial.jpg').convert_alpha()  # Adjust the path
tutorial_image = pygame.transform.scale(tutorial_image, (600, 400))  # Adjust size as needed

# Player and Enemy HP
player_hp = 100
enemy_hp = 100

# Font for displaying damage
font = pygame.font.SysFont(None, 36)

# Damage display variables
player_damage_text = ""
player_damage_time = 0
enemy_damage_text = ""
enemy_damage_time = 0

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
    global player_hp, player_damage_text, player_damage_time
    damage = random.randint(5, 15)
    player_hp -= damage
    player_damage_text = f"-{damage}"
    player_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt

# Function to end the game
def end_game():
    pygame.quit()
    sys.exit()

# Define button areas outside the main loop
attack1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150, 150, 100)
attack2_rect = pygame.Rect(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150, 150, 100)
attack3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150, 150, 100)
attack4_rect = pygame.Rect(SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150, 150, 100)
tutorial_button_rect = pygame.Rect(10, 10, 150, 50)
exit_tutorial_button_rect = pygame.Rect(350, 350, 100, 50)

# Load and play background music
pygame.mixer.music.load('../graphics/img/battle music.mp3')  # Adjust the path to your music file
pygame.mixer.music.play(-1)  # The -1 argument makes the music loop indefinitely

# Main game loop with interactions
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if current_state == NORMAL:
                if tutorial_button_rect.collidepoint(x, y):
                    current_state = TUTORIAL
                elif attack1_rect.collidepoint(x, y):
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
                        enemy_damage_text = "-10"
                    elif selected_option == 2:
                        enemy_hp -= 20  # Option 1 attack 2 effect
                        enemy_damage_text = "-20"
                    elif selected_option == 3:
                        enemy_hp -= 15  # Option 1 attack 3 effect
                        enemy_damage_text = "-15"
                    elif selected_option == 4:
                        enemy_hp -= 5   # Option 1 attack 4 effect
                        enemy_damage_text = "-5"
                    enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                    current_state = ENEMY_TURN
                elif option2_rect.collidepoint(x, y):
                    if selected_option == 1:
                        enemy_hp -= 15  # Option 2 attack 1 effect
                        enemy_damage_text = "-15"
                    elif selected_option == 2:
                        enemy_hp -= 25  # Option 2 attack 2 effect
                        enemy_damage_text = "-25"
                    elif selected_option == 3:
                        enemy_hp -= 20  # Option 2 attack 3 effect
                        enemy_damage_text = "-20"
                    elif selected_option == 4:
                        enemy_hp -= 10  # Option 2 attack 4 effect
                        enemy_damage_text = "-10"
                    enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                    current_state = ENEMY_TURN
            elif current_state == TUTORIAL:
                if exit_tutorial_button_rect.collidepoint(x, y):
                    current_state = NORMAL

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
    screen.blit(attack1_image, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150))
    screen.blit(attack2_image, (SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150))
    screen.blit(attack3_image, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150))
    screen.blit(attack4_image, (SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150))
    
    if current_state == ATTACK_SELECTION:
        # Attack options
        screen.blit(option1_image, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25))
        screen.blit(option2_image, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 25))

    # Tutorial button
    pygame.draw.rect(screen, BLUE, tutorial_button_rect)
    tutorial_button_text = font.render('Tutorial', True, WHITE)
    screen.blit(tutorial_button_text, (20, 20))

    if current_state == TUTORIAL:
        # Draw tutorial image
        screen.blit(tutorial_image, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 200))
        # Draw exit tutorial button
        pygame.draw.rect(screen, RED, exit_tutorial_button_rect)
        exit_text = font.render('Exit', True, WHITE)
        screen.blit(exit_text, (360, 360))

    # Display damage numbers
    current_time = pygame.time.get_ticks()
    if player_damage_text and current_time - player_damage_time < 1000:  # Display for 1 second
        player_damage_surface = font.render(player_damage_text, True, RED)
        screen.blit(player_damage_surface, (character_x + 100, character_y - 50))
    if enemy_damage_text and current_time - enemy_damage_time < 1000:  # Display for 1 second
        enemy_damage_surface = font.render(enemy_damage_text, True, RED)
        screen.blit(enemy_damage_surface, (enemy_x + 100, enemy_y - 50))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
