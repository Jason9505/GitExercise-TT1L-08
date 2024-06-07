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
<<<<<<< HEAD
background_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/forest.jpeg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Character and Enemy images
character_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/mc.png').convert_alpha()
character_image = pygame.transform.scale(character_image, (200, 300))  # Increase size

enemy_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/monster lvl 1 solo.png').convert_alpha()  # Adjust the path
enemy_image = pygame.transform.scale(enemy_image, (200, 300))  # Increase size

# Load attack button images
attack1_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/sword1.png').convert_alpha()
attack1_image = pygame.transform.scale(attack1_image, (150, 100))  # Increase size
attack2_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/spear.png').convert_alpha()
attack2_image = pygame.transform.scale(attack2_image, (150, 100))  # Increase size
attack3_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/scythe.png').convert_alpha()
attack3_image = pygame.transform.scale(attack3_image, (150, 100))  # Increase size
attack4_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/catalyst.png').convert_alpha()
attack4_image = pygame.transform.scale(attack4_image, (150, 100))  # Increase size

# Load attack option images for each attack type and make them square
option_size = 100  # Size of square buttons
attack1_option1_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/sword basic.png').convert_alpha()
attack1_option1_image = pygame.transform.scale(attack1_option1_image, (option_size, option_size))  # Adjust size
attack1_option2_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/sword ult.png').convert_alpha()
attack1_option2_image = pygame.transform.scale(attack1_option2_image, (option_size, option_size))  # Adjust size
attack1_option3_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/sword skill.png').convert_alpha()  # New option button
attack1_option3_image = pygame.transform.scale(attack1_option3_image, (option_size, option_size))  # Adjust size

attack2_option1_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/spear basic.png').convert_alpha()
attack2_option1_image = pygame.transform.scale(attack2_option1_image, (option_size, option_size))  # Adjust size
attack2_option2_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/spear ult.png').convert_alpha()
attack2_option2_image = pygame.transform.scale(attack2_option2_image, (option_size, option_size))  # Adjust size
attack2_option3_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/spear skill.png').convert_alpha()  # New option button
attack2_option3_image = pygame.transform.scale(attack2_option3_image, (option_size, option_size))  # Adjust size

attack3_option1_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/scythe basic.png').convert_alpha()
attack3_option1_image = pygame.transform.scale(attack3_option1_image, (option_size, option_size))  # Adjust size
attack3_option2_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/scythe ult.png').convert_alpha()
attack3_option2_image = pygame.transform.scale(attack3_option2_image, (option_size, option_size))  # Adjust size
attack3_option3_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/scythe skill.png').convert_alpha()  # New option button
attack3_option3_image = pygame.transform.scale(attack3_option3_image, (option_size, option_size))  # Adjust size

attack4_option1_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/catalyst basic.png').convert_alpha()
attack4_option1_image = pygame.transform.scale(attack4_option1_image, (option_size, option_size))  # Adjust size
attack4_option2_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/catalyst ult.png').convert_alpha()
attack4_option2_image = pygame.transform.scale(attack4_option2_image, (option_size, option_size))  # Adjust size
attack4_option3_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/weapon/catalyst skill.png').convert_alpha()  # New option button
attack4_option3_image = pygame.transform.scale(attack4_option3_image, (option_size, option_size))  # Adjust size

# Load tutorial image
tutorial_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/tutorial.jpg').convert_alpha()  # Adjust the path
tutorial_image = pygame.transform.scale(tutorial_image, (600, 400))  # Adjust size as needed

# Load tutorial button image
tutorial_button_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/tutorial button.png').convert_alpha()  # Adjust the path
tutorial_button_image = pygame.transform.scale(tutorial_button_image, (150, 150))  # Adjust size as needed

# Load exit tutorial button image
exit_tutorial_button_image = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/return game.png').convert_alpha()  # Adjust the path
exit_tutorial_button_image = pygame.transform.scale(exit_tutorial_button_image, (100, 100))  # Adjust size as needed

# Player and Enemy HP
player_hp = 100
enemy_hp = 100

# Font for displaying damage
=======
background_image = pygame.image.load('../graphics/img/forest.jpeg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Character and Enemy images
character_image = pygame.image.load('../graphics/img/mc.png').convert_alpha()
character_image = pygame.transform.scale(character_image, (200, 300))  # Increase size

enemy_image = pygame.image.load('../graphics/img/monster lvl 1 solo.png').convert_alpha()  # Adjust the path
enemy_image = pygame.transform.scale(enemy_image, (200, 300))  # Increase size
enemylvl2_image = pygame.image.load('../graphics/img/monster lvl 3 solo.png').convert_alpha()  # Adjust the path
enemylvl2_image = pygame.transform.scale(enemy_image, (200, 300))  # Increase size
enemylvl3_image = pygame.image.load('../graphics/img/monster lvl 4 solo.png').convert_alpha()  # Adjust the path
enemylvl3_image = pygame.transform.scale(enemy_image, (200, 300))  # Increase size
enemyboss_image = pygame.image.load('../graphics/img/final boss.png').convert_alpha()  # Adjust the path
enemyboss_image = pygame.transform.scale(enemy_image, (200, 300))  # Increase size

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
>>>>>>> 9b5facad412aa665d519353824cb37cb6f624886
font = pygame.font.SysFont(None, 36)

# Damage display variables
player_damage_text = ""
player_damage_time = 0
enemy_damage_text = ""
enemy_damage_time = 0

<<<<<<< HEAD
# Function to draw player health bar
def draw_player_health_bar(screen, x, y, current_hp, max_hp):
=======
# Function to draw health bar
def draw_health_bar(screen, x, y, current_hp, max_hp):
>>>>>>> 9b5facad412aa665d519353824cb37cb6f624886
    BAR_WIDTH = 100
    BAR_HEIGHT = 10
    fill = (current_hp / max_hp) * BAR_WIDTH
    border = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
<<<<<<< HEAD
    pygame.draw.rect(screen, GREEN, fill)  # Green for player health bar
=======
    pygame.draw.rect(screen, GREEN, fill)  # Green for health bar
>>>>>>> 9b5facad412aa665d519353824cb37cb6f624886
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

<<<<<<< HEAD
=======
# Timers for delaying enemy attack
enemy_attack_timer = 0
enemy_attack_delay = 2000  # 3 seconds delay

# Points system
points = 3
max_points = 5

>>>>>>> 9b5facad412aa665d519353824cb37cb6f624886
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

<<<<<<< HEAD
=======
# Load and play background music
pygame.mixer.music.load('../graphics/img/battle-music.mp3')  # Adjust the path to your music file
pygame.mixer.music.play(-1)  # The -1 argument makes the music loop indefinitely

>>>>>>> 9b5facad412aa665d519353824cb37cb6f624886
# Define button areas outside the main loop
attack1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 150, 150, 100)
attack2_rect = pygame.Rect(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 150, 150, 100)
attack3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 150, 150, 100)
attack4_rect = pygame.Rect(SCREEN_WIDTH // 2 + 225, SCREEN_HEIGHT - 150, 150, 100)
<<<<<<< HEAD
tutorial_button_rect = pygame.Rect(10, 10, 150, 50)
exit_tutorial_button_rect = pygame.Rect(350, 350, 100, 50)

# Load and play background music
pygame.mixer.music.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/battle-music.mp3')  # Adjust the path to your music file
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
                    current_state = ATTACK_SELECTION
                    selected_attack = 1
                elif attack2_rect.collidepoint(x, y):
                    current_state = ATTACK_SELECTION
                    selected_attack = 2
                elif attack3_rect.collidepoint(x, y):
                    current_state = ATTACK_SELECTION
                    selected_attack = 3
                elif attack4_rect.collidepoint(x, y):
                    current_state = ATTACK_SELECTION
                    selected_attack = 4
            elif current_state == ATTACK_SELECTION:
                option1_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 150, option_size, option_size)
                option2_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150, option_size, option_size)
                option3_rect = pygame.Rect(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 - 150, option_size, option_size)
                if option1_rect.collidepoint(x, y):
                    if selected_attack == 1:
                        enemy_hp -= 10
                        enemy_damage_text = "-10"
                    elif selected_attack == 2:
                        enemy_hp -= 15
                        enemy_damage_text = "-15"
                    elif selected_attack == 3:
                        enemy_hp -= 20
                        enemy_damage_text = "-20"
                    elif selected_attack == 4:
                        enemy_hp -= 25
                        enemy_damage_text = "-25"
                    enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                    current_state = ENEMY_TURN
                elif option2_rect.collidepoint(x, y):
                    if selected_attack == 1:
                        enemy_hp -= 20
                        enemy_damage_text = "-20"
                    elif selected_attack == 2:
                        enemy_hp -= 25
                        enemy_damage_text = "-25"
                    elif selected_attack == 3:
                        enemy_hp -= 30
                        enemy_damage_text = "-30"
                    elif selected_attack == 4:
                        enemy_hp -= 35
                        enemy_damage_text = "-35"
                    enemy_damage_time = pygame.time.get_ticks()  # Record the time when damage is dealt
                    current_state = ENEMY_TURN
                elif option3_rect.collidepoint(x, y):
                    if selected_attack == 1:
                        enemy_hp -= 25
                        enemy_damage_text = "-25"
                    elif selected_attack == 2:
                        enemy_hp -= 30
                        enemy_damage_text = "-30"
                    elif selected_attack == 3:
                        enemy_hp -= 35
                        enemy_damage_text = "-35"
                    elif selected_attack == 4:
                        enemy_hp -= 40
                        enemy_damage_text = "-40"
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
        # Draw specific attack options based on selected attack
        if selected_attack == 1:
            screen.blit(attack1_option1_image, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 150))
            screen.blit(attack1_option2_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
            screen.blit(attack1_option3_image, (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 - 150))  # Draw new option button
        elif selected_attack == 2:
            screen.blit(attack2_option1_image, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 150))
            screen.blit(attack2_option2_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
            screen.blit(attack2_option3_image, (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 - 150))  # Draw new option button
        elif selected_attack == 3:
            screen.blit(attack3_option1_image, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 150))
            screen.blit(attack3_option2_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
            screen.blit(attack3_option3_image, (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 - 150))  # Draw new option button
        elif selected_attack == 4:
            screen.blit(attack4_option1_image, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 150))
            screen.blit(attack4_option2_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
            screen.blit(attack4_option3_image, (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 - 150))  # Draw new option button

    # Tutorial button
    screen.blit(tutorial_button_image, (10, 10))

    if current_state == TUTORIAL:
        # Draw tutorial image
        screen.blit(tutorial_image, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 200))
        # Draw exit tutorial button
        screen.blit(exit_tutorial_button_image, (350, 350))

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
=======

basic_rect = pygame.Rect(
    SCREEN_WIDTH // 2 - (basic_size + ult_size + skill_size + 10) // 2,
    SCREEN_HEIGHT - 250, basic_size, basic_size)
ult_rect = pygame.Rect(
    SCREEN_WIDTH // 2 - (ult_size + skill_size + 10) // 2 + basic_size + 5,
    SCREEN_HEIGHT - 250, ult_size, ult_size)
skill_rect = pygame.Rect(
    SCREEN_WIDTH // 2 + (ult_size - skill_size) // 2 + 5,
    SCREEN_HEIGHT - 250, skill_size, skill_size)
    
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
    draw_health_bar(screen, 50, SCREEN_HEIGHT - character_image.get_height() - 60, player_hp, max_player_hp)  # Adjusted for positioning
    draw_enemy_health_bar(screen, SCREEN_WIDTH - enemy_image.get_width() - 50, 30, enemy_hp, 100)  # Adjusted for positioning

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
>>>>>>> 9b5facad412aa665d519353824cb37cb6f624886
