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

# Load attack button images
attack1_image = pygame.image.load('../graphics/img/weapon/sword1.png').convert_alpha()
attack1_image = pygame.transform.scale(attack1_image, (150, 100))  # Increase size
attack2_image = pygame.image.load('../graphics/img/weapon/spear.png').convert_alpha()
attack2_image = pygame.transform.scale(attack2_image, (150, 100))  # Increase size
attack3_image = pygame.image.load('../graphics/img/weapon/scythe.png').convert_alpha()
attack3_image = pygame.transform.scale(attack3_image, (150, 100))  # Increase size
attack4_image = pygame.image.load('../graphics/img/weapon/catalyst.png').convert_alpha()
attack4_image = pygame.transform.scale(attack4_image, (150, 100))  # Increase size

# Define sizes for buttons
basic_size = 100  # Size of basic buttons
skill_size = 150  # Size of skill buttons
ult_size = 200  # Size of ult buttons

# Load attack option images for each attack type with different sizes
attack1_basic_image = pygame.image.load('../graphics/img/weapon/sword basic.png').convert_alpha()
attack1_basic_image = pygame.transform.scale(attack1_basic_image, (basic_size, basic_size))
attack1_ult_image = pygame.image.load('../graphics/img/weapon/sword ult.png').convert_alpha()
attack1_ult_image = pygame.transform.scale(attack1_ult_image, (ult_size, ult_size))
attack1_skill_image = pygame.image.load('../graphics/img/weapon/sword skill.png').convert_alpha()
attack1_skill_image = pygame.transform.scale(attack1_skill_image, (skill_size, skill_size))

attack2_basic_image = pygame.image.load('../graphics/img/weapon/spear basic.png').convert_alpha()
attack2_basic_image = pygame.transform.scale(attack2_basic_image, (basic_size, basic_size))
attack2_ult_image = pygame.image.load('../graphics/img/weapon/spear ult.png').convert_alpha()
attack2_ult_image = pygame.transform.scale(attack2_ult_image, (ult_size, ult_size))
attack2_skill_image = pygame.image.load('../graphics/img/weapon/spear skill.png').convert_alpha()
attack2_skill_image = pygame.transform.scale(attack2_skill_image, (skill_size, skill_size))

attack3_basic_image = pygame.image.load('../graphics/img/weapon/scythe basic.png').convert_alpha()
attack3_basic_image = pygame.transform.scale(attack3_basic_image, (basic_size, basic_size))
attack3_ult_image = pygame.image.load('../graphics/img/weapon/scythe ult.png').convert_alpha()
attack3_ult_image = pygame.transform.scale(attack3_ult_image, (ult_size, ult_size))
attack3_skill_image = pygame.image.load('../graphics/img/weapon/scythe skill.png').convert_alpha()
attack3_skill_image = pygame.transform.scale(attack3_skill_image, (skill_size, skill_size))

attack4_basic_image = pygame.image.load('../graphics/img/weapon/catalyst basic.png').convert_alpha()
attack4_basic_image = pygame.transform.scale(attack4_basic_image, (basic_size, basic_size))
attack4_ult_image = pygame.image.load('../graphics/img/weapon/catalyst ult.png').convert_alpha()
attack4_ult_image = pygame.transform.scale(attack4_ult_image, (ult_size, ult_size))
attack4_skill_image = pygame.image.load('../graphics/img/weapon/catalyst skill.png').convert_alpha()
attack4_skill_image = pygame.transform.scale(attack4_skill_image, (skill_size, skill_size))

# Load tutorial image
tutorial_image = pygame.image.load('../graphics/img/tutorial.jpg').convert_alpha()  # Adjust the path
tutorial_image = pygame.transform.scale(tutorial_image, (600, 400))  # Adjust size as needed

# Load tutorial button image
tutorial_button_image = pygame.image.load('../graphics/img/tutorial button.png').convert_alpha()  # Adjust the path
tutorial_button_image = pygame.transform.scale(tutorial_button_image, (150, 150))  # Adjust size as needed

# Load exit tutorial button image
exit_tutorial_button_image = pygame.image.load('../graphics/img/return game.png').convert_alpha()  # Adjust the path
exit_tutorial_button_image = pygame.transform.scale(exit_tutorial_button_image, (100, 100))  # Adjust size as needed

# Player and Enemy HP
player_hp = 100  # Overall health for player
enemy_hp = 100
max_player_hp = 100  # Maximum HP for player

# Font for displaying damage and points
font = pygame.font.SysFont(None, 36)

# Damage display variables
player_damage_text = ""
player_damage_time = 0
enemy_damage_text = ""
enemy_damage_time = 0

# Function to draw health bar
def draw_health_bar(screen, x, y, current_hp, max_hp):
    BAR_WIDTH = 100
    BAR_HEIGHT = 10
    fill = (current_hp / max_hp) * BAR_WIDTH
    border = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(screen, GREEN, fill)  # Green for health bar
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
selected_attack = None

# Timers for delaying enemy attack
enemy_attack_timer = 0
enemy_attack_delay = 3000  # 3 seconds delay

# Points system
points = 3
max_points = 5

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

# Load and play background music
pygame.mixer.music.load('../graphics/img/battle-music.mp3')  # Adjust the path to your music file
pygame.mixer.music.play(-1)  # The -1 argument makes the music loop indefinitely

# Define button areas outside the main loop
attack1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150, 150, 100)
attack2_rect = pygame.Rect(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150, 150, 100)
attack3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150, 150, 100)
attack4_rect = pygame.Rect(SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150, 150, 100)
tutorial_button_rect = pygame.Rect(10, 10, 150, 150)  # Updated to match the image size
exit_tutorial_button_rect = pygame.Rect(350, 350, 100, 100)  # Updated to match the image size

# Attack damage ranges for each type of attack
attack_damage = {
    0: {'basic': (5, 10), 'ult': (20, 30), 'skill': (10, 20)},
    1: {'basic': (6, 12), 'ult': (18, 28), 'skill': (12, 22)},
    2: {'basic': (7, 14), 'ult': (22, 32), 'skill': (14, 24)},
    3: {'basic': (8, 16), 'ult': (24, 34), 'skill': (16, 26)},
}

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_state == NORMAL:
                if attack1_rect.collidepoint(mouse_pos):
                    current_state = ATTACK_SELECTION
                    selected_attack = 0
                elif attack2_rect.collidepoint(mouse_pos):
                    current_state = ATTACK_SELECTION
                    selected_attack = 1
                elif attack3_rect.collidepoint(mouse_pos):
                    current_state = ATTACK_SELECTION
                    selected_attack = 2
                elif attack4_rect.collidepoint(mouse_pos):
                    current_state = ATTACK_SELECTION
                    selected_attack = 3
                elif tutorial_button_rect.collidepoint(mouse_pos):
                    current_state = TUTORIAL

            elif current_state == ATTACK_SELECTION:
                basic_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, basic_size, basic_size)
                ult_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50 + basic_size + 5, SCREEN_HEIGHT // 2 - 50, ult_size, ult_size)
                skill_rect = pygame.Rect(SCREEN_WIDTH // 2 + 100 + basic_size + ult_size + 10, SCREEN_HEIGHT // 2 - 50, skill_size, skill_size)

                if basic_rect.collidepoint(mouse_pos):
                    damage = random.randint(*attack_damage[selected_attack]['basic'])
                    if selected_attack == 3:
                        player_hp = min(player_hp + damage, max_player_hp)  # Heal the player
                        player_damage_text = f"+{damage}"
                    else:
                        enemy_hp -= damage
                        enemy_damage_text = f"-{damage}"
                    points = min(points + 1, max_points)  # Gain 1 point
                    enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                    current_state = ENEMY_TURN
                    enemy_attack_timer = pygame.time.get_ticks()  # Start enemy attack timer

                elif ult_rect.collidepoint(mouse_pos) and points >= 3:
                    if selected_attack == 3:
                        heal = random.randint(*attack_damage[selected_attack]['ult'])
                        player_hp = min(player_hp + heal, max_player_hp)
                        player_damage_text = f"+{heal}"
                    else:
                        damage = random.randint(*attack_damage[selected_attack]['ult'])
                        enemy_hp -= damage
                        enemy_damage_text = f"-{damage}"
                    points -= 3  # Consume 3 points
                    enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                    current_state = ENEMY_TURN
                    enemy_attack_timer = pygame.time.get_ticks()  # Start enemy attack timer

                elif skill_rect.collidepoint(mouse_pos) and points >= 2:
                    if selected_attack == 3:
                        heal = random.randint(*attack_damage[selected_attack]['skill'])
                        player_hp = min(player_hp + heal, max_player_hp)
                        player_damage_text = f"+{heal}"
                    else:
                        damage = random.randint(*attack_damage[selected_attack]['skill'])
                        enemy_hp -= damage
                        enemy_damage_text = f"-{damage}"
                    points -= 2  # Consume 2 points
                    enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                    current_state = ENEMY_TURN
                    enemy_attack_timer = pygame.time.get_ticks()  # Start enemy attack timer

                elif tutorial_button_rect.collidepoint(mouse_pos):
                    current_state = TUTORIAL

            elif current_state == TUTORIAL:
                if exit_tutorial_button_rect.collidepoint(mouse_pos):
                    current_state = NORMAL

    screen.blit(background_image, (0, 0))

    # Draw tutorial button in the top-left corner
    screen.blit(tutorial_button_image, tutorial_button_rect)

    # Display tutorial screen
    if current_state == TUTORIAL:
        screen.blit(tutorial_image, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 200))  # Adjust position as needed
        screen.blit(exit_tutorial_button_image, exit_tutorial_button_rect)  # Draw exit tutorial button
    else:
        # Draw characters
        screen.blit(character_image, (50, SCREEN_HEIGHT - 350))
        screen.blit(enemy_image, (SCREEN_WIDTH - 250, 50))

        # Draw player health bar aligned in the middle of the character
        draw_health_bar(screen, 50 + character_image.get_width() // 2 - 50, SCREEN_HEIGHT - 380, player_hp, max_player_hp)

        # Draw buttons without health bars
        screen.blit(attack1_image, attack1_rect)
        screen.blit(attack2_image, attack2_rect)
        screen.blit(attack3_image, attack3_rect)
        screen.blit(attack4_image, attack4_rect)

        # Draw enemy health bar aligned in the middle of the enemy
        draw_enemy_health_bar(screen, SCREEN_WIDTH - 250 + enemy_image.get_width() // 2 - 50, 20, enemy_hp, 100)

        if current_state == ATTACK_SELECTION:
            basic_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, basic_size, basic_size)
            ult_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50 + basic_size + 5, SCREEN_HEIGHT // 2 - 50, ult_size, ult_size)
            skill_rect = pygame.Rect(SCREEN_WIDTH // 2 + 100 + basic_size + ult_size + 10, SCREEN_HEIGHT // 2 - 50, skill_size, skill_size)
            if selected_attack == 0:
                screen.blit(attack1_basic_image, basic_rect)
                screen.blit(attack1_ult_image, ult_rect)
                screen.blit(attack1_skill_image, skill_rect)
            elif selected_attack == 1:
                screen.blit(attack2_basic_image, basic_rect)
                screen.blit(attack2_ult_image, ult_rect)
                screen.blit(attack2_skill_image, skill_rect)
            elif selected_attack == 2:
                screen.blit(attack3_basic_image, basic_rect)
                screen.blit(attack3_ult_image, ult_rect)
                screen.blit(attack3_skill_image, skill_rect)
            elif selected_attack == 3:
                screen.blit(attack4_basic_image, basic_rect)
                screen.blit(attack4_ult_image, ult_rect)
                screen.blit(attack4_skill_image, skill_rect)

        # Display damage text for player
        if player_damage_text:
            screen.blit(font.render(player_damage_text, True, RED), (50, SCREEN_HEIGHT - 400))
            if pygame.time.get_ticks() - player_damage_time > 1000:  # Display damage for 1 second
                player_damage_text = ""

        # Display damage text for enemy
        if enemy_damage_text:
            screen.blit(font.render(enemy_damage_text, True, RED), (SCREEN_WIDTH - 250, 30))
            if pygame.time.get_ticks() - enemy_damage_time > 1000:  # Display damage for 1 second
                enemy_damage_text = ""

        # Check for enemy attack after delay
        if current_state == ENEMY_TURN and pygame.time.get_ticks() - enemy_attack_timer > enemy_attack_delay:
            enemy_attack()
            current_state = NORMAL

    # Check for game over conditions
    if player_hp <= 0:
        end_game()
    elif enemy_hp <= 0:
        end_game()

    # Update points and display
    screen.blit(font.render(f"Points: {int(points)}", True, YELLOW), (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 50))

    pygame.display.flip()

# Quit the game
pygame.quit()
