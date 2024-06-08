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
character_image = pygame.transform.scale(character_image, (300, 300))  # Increase size

enemy_image = pygame.image.load('../graphics/img/monster lvl 1 solo.png').convert_alpha()  # Adjust the path
enemy_image = pygame.transform.scale(enemy_image, (300, 300))  # Increase size
enemylvl2_image = pygame.image.load('../graphics/img/monster lvl 3 solo.png').convert_alpha()  # Adjust the path
enemylvl2_image = pygame.transform.scale(enemy_image, (300, 300))  # Increase size
enemylvl3_image = pygame.image.load('../graphics/img/monster lvl 4 solo.png').convert_alpha()  # Adjust the path
enemylvl3_image = pygame.transform.scale(enemy_image, (300, 300))  # Increase size
enemyboss_image = pygame.image.load('../graphics/img/final boss.png').convert_alpha()  # Adjust the path
enemyboss_image = pygame.transform.scale(enemy_image, (300, 300))  # Increase size

# Load attack button images
attack1_image = pygame.image.load('../graphics/img/weapon/sword1.png').convert_alpha()
attack1_image = pygame.transform.scale(attack1_image, (200, 200))  # Increase size
attack2_image = pygame.image.load('../graphics/img/weapon/spear.png').convert_alpha()
attack2_image = pygame.transform.scale(attack2_image, (200, 200))  # Increase size
attack3_image = pygame.image.load('../graphics/img/weapon/scythe.png').convert_alpha()
attack3_image = pygame.transform.scale(attack3_image, (200, 200))  # Increase size
attack4_image = pygame.image.load('../graphics/img/weapon/catalyst.png').convert_alpha()
attack4_image = pygame.transform.scale(attack4_image, (200, 200))  # Increase size

# Define sizes for buttons
basic_size = 200  # Size of basic buttons
skill_size = 300  # Size of skill buttons
ult_size = 400  # Size of ult buttons

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
enemy_attack_delay = 2000  # 3 seconds delay

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
attack1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150, 200, 200)
attack2_rect = pygame.Rect(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150, 200, 200)
attack3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150, 200, 200)
attack4_rect = pygame.Rect(SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150, 200, 200)

basic_rect = pygame.Rect(
    SCREEN_WIDTH // 2 - (basic_size + skill_size + ult_size + 10) // 2,
    SCREEN_HEIGHT // 2 - basic_size // 2, basic_size, basic_size
)
ult_rect = pygame.Rect(basic_rect.right + 5, SCREEN_HEIGHT // 2 - ult_size // 2, ult_size, ult_size)
skill_rect = pygame.Rect(ult_rect.right + 5, SCREEN_HEIGHT // 2 - skill_size // 2, skill_size, skill_size)

    
tutorial_button_rect = pygame.Rect(20, 20, 150, 150)
exit_tutorial_button_rect = pygame.Rect(SCREEN_WIDTH - 120, 20, 100, 100)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = event.pos
                if current_state == NORMAL:
                    if attack1_rect.collidepoint(mouse_pos):
                        selected_attack = "attack1"
                        current_state = ATTACK_SELECTION
                    elif attack2_rect.collidepoint(mouse_pos):
                        selected_attack = "attack2"
                        current_state = ATTACK_SELECTION
                    elif attack3_rect.collidepoint(mouse_pos):
                        selected_attack = "attack3"
                        current_state = ATTACK_SELECTION
                    elif attack4_rect.collidepoint(mouse_pos):
                        selected_attack = "attack4"
                        current_state = ATTACK_SELECTION
                    elif tutorial_button_rect.collidepoint(mouse_pos):
                        current_state = TUTORIAL
                elif current_state == ATTACK_SELECTION:
                    if basic_rect.collidepoint(mouse_pos):
                        if selected_attack == "attack1":
                            damage = random.randint(10, 20)
                        elif selected_attack == "attack2":
                            damage = random.randint(15, 25)
                        elif selected_attack == "attack3":
                            damage = random.randint(20, 30)
                        elif selected_attack == "attack4":
                            damage = random.randint(5, 15)
                        enemy_hp -= damage
                        enemy_damage_text = f"-{damage}"
                        enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                        points = min(points + 1, max_points)  # Increase points, maxing out at max_points
                        current_state = ENEMY_TURN
                        enemy_attack_timer = pygame.time.get_ticks() + enemy_attack_delay  # Set timer for enemy attack
                    elif skill_rect.collidepoint(mouse_pos):
                        if points >= 1:
                            if selected_attack == "attack1":
                                damage = random.randint(30, 50)
                                enemy_hp -= damage
                                enemy_damage_text = f"-{damage}"
                                enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                            elif selected_attack == "attack2":
                                damage = random.randint(35, 55)
                                enemy_hp -= damage
                                enemy_damage_text = f"-{damage}"
                                enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                            elif selected_attack == "attack3":
                                damage = random.randint(40, 60)
                                enemy_hp -= damage
                                enemy_damage_text = f"-{damage}"
                                enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                            elif selected_attack == "attack4":
                                heal = random.randint(10, 20)
                                player_hp = min(player_hp + heal, max_player_hp)
                                player_damage_text = f"+{heal}"
                                player_damage_time = pygame.time.get_ticks()  # Record the time when healed
                            points -= 1  # Decrease points by 1
                            current_state = ENEMY_TURN
                            enemy_attack_timer = pygame.time.get_ticks() + enemy_attack_delay  # Set timer for enemy attack
                    elif ult_rect.collidepoint(mouse_pos):
                        if points >= 3:
                            if selected_attack == "attack1":
                                damage = random.randint(50, 70)
                                enemy_hp -= damage
                                enemy_damage_text = f"-{damage}"
                                enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                            elif selected_attack == "attack2":
                                damage = random.randint(55, 75)
                                enemy_hp -= damage
                                enemy_damage_text = f"-{damage}"
                                enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                            elif selected_attack == "attack3":
                                damage = random.randint(60, 80)
                                enemy_hp -= damage
                                enemy_damage_text = f"-{damage}"
                                enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                            elif selected_attack == "attack4":
                                heal = random.randint(20, 40)
                                player_hp = min(player_hp + heal, max_player_hp)
                                player_damage_text = f"+{heal}"
                                player_damage_time = pygame.time.get_ticks()  # Record the time when healed
                            points -= 3  # Decrease points by 3
                            current_state = ENEMY_TURN
                            enemy_attack_timer = pygame.time.get_ticks() + enemy_attack_delay  # Set timer for enemy attack
                elif current_state == TUTORIAL:
                    if exit_tutorial_button_rect.collidepoint(mouse_pos):
                        current_state = NORMAL

    # Check if player or monster is dead
    if player_hp <= 0 or enemy_hp <= 0:
        end_game()

    # Clear the screen and draw the background
    screen.blit(background_image, (0, 0))

    # Draw the character and enemy images
    screen.blit(character_image, (50, SCREEN_HEIGHT - character_image.get_height() - 50))  # Adjusted for positioning
    screen.blit(enemy_image, (SCREEN_WIDTH - enemy_image.get_width() - 50, 50))  # Adjusted for positioning

    # Draw attack buttons
    screen.blit(attack1_image, attack1_rect)
    screen.blit(attack2_image, attack2_rect)
    screen.blit(attack3_image, attack3_rect)
    screen.blit(attack4_image, attack4_rect)

    # Draw tutorial button
    screen.blit(tutorial_button_image, tutorial_button_rect)

    # Draw player and enemy health bars
    draw_health_bar(screen, 150, SCREEN_HEIGHT - character_image.get_height() - 60, player_hp, max_player_hp)  # Adjusted for positioning
    draw_enemy_health_bar(screen, SCREEN_WIDTH - enemy_image.get_width() - 50, 50, enemy_hp, 100)  # Adjusted for positioning

    # Draw damage text for player and enemy
    current_time = pygame.time.get_ticks()
    if current_time - player_damage_time < 1000:  # Display player damage for 1 second
        player_damage_surface = font.render(player_damage_text, True, RED)
        screen.blit(player_damage_surface, (50, SCREEN_HEIGHT - character_image.get_height() - 90))  # Adjusted for positioning
    if current_time - enemy_damage_time < 1000:  # Display enemy damage for 1 second
        enemy_damage_surface = font.render(enemy_damage_text, True, RED)
        screen.blit(enemy_damage_surface, (SCREEN_WIDTH - enemy_image.get_width() - 50, 10))  # Adjusted for positioning

    # Handle enemy turn
    if current_state == ENEMY_TURN and pygame.time.get_ticks() >= enemy_attack_timer:
        enemy_attack()
        current_state = NORMAL

    # Draw points text
    points_surface = font.render(f"Points: {points}/{max_points}", True, YELLOW)
    screen.blit(points_surface, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 50))

    # Draw attack selection options
    if current_state == ATTACK_SELECTION:
        if selected_attack == "attack1":
            screen.blit(attack1_basic_image, basic_rect)
            screen.blit(attack1_ult_image, ult_rect)
            screen.blit(attack1_skill_image, skill_rect)
        elif selected_attack == "attack2":
            screen.blit(attack2_basic_image, basic_rect)
            screen.blit(attack2_ult_image, ult_rect)
            screen.blit(attack2_skill_image, skill_rect)
        elif selected_attack == "attack3":
            screen.blit(attack3_basic_image, basic_rect)
            screen.blit(attack3_ult_image, ult_rect)
            screen.blit(attack3_skill_image, skill_rect)
        elif selected_attack == "attack4":
            screen.blit(attack4_basic_image, basic_rect)
            screen.blit(attack4_ult_image, ult_rect)
            screen.blit(attack4_skill_image, skill_rect)

    # Draw tutorial screen
    if current_state == TUTORIAL:
        screen.blit(tutorial_image, ((SCREEN_WIDTH - tutorial_image.get_width()) // 2, (SCREEN_HEIGHT - tutorial_image.get_height()) // 2))
        screen.blit(exit_tutorial_button_image, exit_tutorial_button_rect)

    # Update the display
    pygame.display.update()
