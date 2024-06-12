import pygame
import sys
import random
from settings import *



class BattleScreen:
    def __init__(self, player, enemy, enemy_name):
        pygame.init()
        # Create main screen in full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.screen.get_size()
        pygame.display.set_caption("Battle Screen")

        # Load background image
        self.background_image = pygame.image.load('../graphics/img/forest.jpeg').convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Character and Enemy images
        self.character_image = pygame.image.load('../graphics/img/mc.png').convert_alpha()
        self.character_image = pygame.transform.scale(self.character_image, (300, 300))

        # Load enemy data
        self.enemy_name = enemy_name
        self.enemy_data = monster_data[self.enemy_name]
        self.enemy_image = pygame.image.load(self.enemy_data['image']).convert_alpha()
        self.enemy_image = pygame.transform.scale(self.enemy_image, (300, 300))
        self.enemy_hp = self.enemy_data['health']
        self.max_enemy_hp = self.enemy_data['health']
        self.enemy_damage_range = self.enemy_data['damage']

        # Load attack button images
        self.attack1_image = pygame.image.load('../graphics/img/weapon/sword1.png').convert_alpha()
        self.attack1_image = pygame.transform.scale(self.attack1_image, (200, 200))
        self.attack2_image = pygame.image.load('../graphics/img/weapon/scythe.png').convert_alpha()
        self.attack2_image = pygame.transform.scale(self.attack2_image, (200, 200))
        self.attack3_image = pygame.image.load('../graphics/img/weapon/spear.png').convert_alpha()
        self.attack3_image = pygame.transform.scale(self.attack3_image, (200, 200))
        self.attack4_image = pygame.image.load('../graphics/img/weapon/catalyst.png').convert_alpha()
        self.attack4_image = pygame.transform.scale(self.attack4_image, (200, 200))

        # Define sizes for buttons
        self.basic_size = 200
        self.skill_size = 300
        self.ult_size = 400

        # Load attack option images for each attack type with different sizes
        self.load_attack_images()

        # Load tutorial image
        self.tutorial_image = pygame.image.load('../graphics/img/tutorial.png').convert_alpha()
        self.tutorial_image = pygame.transform.scale(self.tutorial_image, (600, 600))

        # Load tutorial button image
        self.tutorial_button_image = pygame.image.load('../graphics/img/tutorial button.png').convert_alpha()
        self.tutorial_button_image = pygame.transform.scale(self.tutorial_button_image, (150, 150))

        # Load exit tutorial button image
        self.exit_tutorial_button_image = pygame.image.load('../graphics/img/return game.png').convert_alpha()
        self.exit_tutorial_button_image = pygame.transform.scale(self.exit_tutorial_button_image, (100, 100))

        # Player and Enemy HP
        self.player = player
        self.enemy = enemy
        self.player_hp = 300
        self.max_player_hp = 300

        # Font for displaying damage and points
        self.font = pygame.font.SysFont(None, 36)

        # Damage display variables
        self.player_damage_text = ""
        self.player_damage_time = 0
        self.player_healing_text = ""
        self.player_healing_time = 0
        self.enemy_damage_text = ""
        self.enemy_damage_time = 0
        self.attack1_buff = 0
        self.attack2_buff = 0

        # Game states
        self.NORMAL = 0
        self.ATTACK_SELECTION = 1
        self.ENEMY_TURN = 2
        self.TUTORIAL = 3
        self.current_state = self.NORMAL
        self.attack_state = ""
        self.skill_state = ""

        # Selected attack type
        self.selected_attack = None

        # Timers for delaying enemy attack
        self.enemy_attack_timer = 0
        self.enemy_attack_delay = 2000  # 2 seconds delay

        # Points system
        self.points = 3
        self.max_points = 5

        # Define button areas outside the main loop
        self.define_button_areas()

        # Battle state
        self.battle_over = False

        # Load and play background music
        pygame.mixer.music.load(self.enemy_data['music'])
        pygame.mixer.music.play(-1)

        # Load sound effects
        self.damage_sound = pygame.mixer.Sound('../audio/oof.mp3')
        self.enemy_damage_sound = pygame.mixer.Sound('../audio/slash.mp3')
        self.healing_sound = pygame.mixer.Sound('../audio/heal.mp3')

        # Shaking effect variables
        self.shake_duration = 300  # Shake duration in milliseconds
        self.shake_magnitude = 10  # Shake magnitude in pixels
        self.shake_start_time = 0
        self.shaking = False
        self.shaking_entity = None

    def load_attack_images(self):
        self.attack1_basic_image = pygame.image.load('../graphics/img/weapon/sword basic.png').convert_alpha()
        self.attack1_basic_image = pygame.transform.scale(self.attack1_basic_image, (self.basic_size, self.basic_size))
        self.attack1_ult_image = pygame.image.load('../graphics/img/weapon/sword ult.png').convert_alpha()
        self.attack1_ult_image = pygame.transform.scale(self.attack1_ult_image, (self.ult_size, self.ult_size))
        self.attack1_skill_image = pygame.image.load('../graphics/img/weapon/sword skill.png').convert_alpha()
        self.attack1_skill_image = pygame.transform.scale(self.attack1_skill_image, (self.skill_size, self.skill_size))

        self.attack2_basic_image = pygame.image.load('../graphics/img/weapon/scythe basic.png').convert_alpha()
        self.attack2_basic_image = pygame.transform.scale(self.attack2_basic_image, (self.basic_size, self.basic_size))
        self.attack2_ult_image = pygame.image.load('../graphics/img/weapon/scythe ult.png').convert_alpha()
        self.attack2_ult_image = pygame.transform.scale(self.attack2_ult_image, (self.ult_size, self.ult_size))
        self.attack2_skill_image = pygame.image.load('../graphics/img/weapon/scythe skill.png').convert_alpha()
        self.attack2_skill_image = pygame.transform.scale(self.attack2_skill_image, (self.skill_size, self.skill_size))

        self.attack3_basic_image = pygame.image.load('../graphics/img/weapon/spear basic.png').convert_alpha()
        self.attack3_basic_image = pygame.transform.scale(self.attack3_basic_image, (self.basic_size, self.basic_size))
        self.attack3_ult_image = pygame.image.load('../graphics/img/weapon/spear ult.png').convert_alpha()
        self.attack3_ult_image = pygame.transform.scale(self.attack3_ult_image, (self.ult_size, self.ult_size))
        self.attack3_skill_image = pygame.image.load('../graphics/img/weapon/spear skill.png').convert_alpha()
        self.attack3_skill_image = pygame.transform.scale(self.attack3_skill_image, (self.skill_size, self.skill_size))

        self.attack4_basic_image = pygame.image.load('../graphics/img/weapon/catalyst basic.png').convert_alpha()
        self.attack4_basic_image = pygame.transform.scale(self.attack4_basic_image, (self.basic_size, self.basic_size))
        self.attack4_ult_image = pygame.image.load('../graphics/img/weapon/catalyst ult.png').convert_alpha()
        self.attack4_ult_image = pygame.transform.scale(self.attack4_ult_image, (self.ult_size, self.ult_size))
        self.attack4_skill_image = pygame.image.load('../graphics/img/weapon/catalyst skill.png').convert_alpha()
        self.attack4_skill_image = pygame.transform.scale(self.attack4_skill_image, (self.skill_size, self.skill_size))

    def define_button_areas(self):
        self.attack1_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 300, self.SCREEN_HEIGHT - 150, 200, 200)
        self.attack2_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 125, self.SCREEN_HEIGHT - 150, 200, 200)
        self.attack3_rect = pygame.Rect(self.SCREEN_WIDTH // 2 + 50, self.SCREEN_HEIGHT - 150, 200, 200)
        self.attack4_rect = pygame.Rect(self.SCREEN_WIDTH // 2 + 225, self.SCREEN_HEIGHT - 150, 200, 200)

        self.basic_rect = pygame.Rect(
            self.SCREEN_WIDTH // 2 - (self.basic_size + self.skill_size + self.ult_size + 10) // 2,
            self.SCREEN_HEIGHT // 2 - self.basic_size // 2, self.basic_size, self.basic_size
        )
        self.ult_rect = pygame.Rect(self.basic_rect.right + 5, self.SCREEN_HEIGHT // 2 - self.ult_size // 2, self.ult_size, self.ult_size)
        self.skill_rect = pygame.Rect(self.ult_rect.right + 5, self.SCREEN_HEIGHT // 2 - self.skill_size // 2, self.skill_size, self.skill_size)

        self.tutorial_button_rect = pygame.Rect(20, 20, 150, 150)
        
    def draw_background(self):
        self.screen.blit(self.background_image, (0, 0))

    def draw_player(self):
        # Position the player at the bottom left corner
        self.player_rect = self.character_image.get_rect(bottomleft=(0, self.SCREEN_HEIGHT))
        if self.shaking and self.shaking_entity == 'player':
            shake_offset_x = random.randint(-self.shake_magnitude, self.shake_magnitude)
            shake_offset_y = random.randint(-self.shake_magnitude, self.shake_magnitude)
            self.player_rect.move_ip(shake_offset_x, shake_offset_y)
        self.screen.blit(self.character_image, self.player_rect)
        return self.player_rect

    def draw_enemy(self):
        # Position the enemy at the top right corner
        self.enemy_rect = self.enemy_image.get_rect(topright=(self.SCREEN_WIDTH, 20))
        if self.shaking and self.shaking_entity == 'enemy':
            shake_offset_x = random.randint(-self.shake_magnitude, self.shake_magnitude)
            shake_offset_y = random.randint(-self.shake_magnitude, self.shake_magnitude)
            self.enemy_rect.move_ip(shake_offset_x, shake_offset_y)
        self.screen.blit(self.enemy_image, self.enemy_rect)
        return self.enemy_rect

    def draw_attack_buttons(self):
        self.screen.blit(self.attack1_image, self.attack1_rect.topleft)
        self.screen.blit(self.attack2_image, self.attack2_rect.topleft)
        self.screen.blit(self.attack3_image, self.attack3_rect.topleft)
        self.screen.blit(self.attack4_image, self.attack4_rect.topleft)

    def draw_tutorial_button(self):
        self.screen.blit(self.tutorial_button_image, self.tutorial_button_rect.topleft)

    def draw_tutorial_screen(self):
        # Center the tutorial image
        tutorial_width = 600  # Width of the tutorial image
        tutorial_height = 400  # Height of the tutorial image
        tutorial_x = (self.SCREEN_WIDTH - tutorial_width) // 2
        tutorial_y = (self.SCREEN_HEIGHT - tutorial_height) // 2

        # Draw the tutorial image
        self.screen.blit(self.tutorial_image, (tutorial_x, tutorial_y))

        # Calculate the position for the "Exit Tutorial" button
        button_width = 100
        button_height = 100
        button_x = tutorial_x + (tutorial_width - button_width) // 2
        button_y = tutorial_y + tutorial_height + 20  # 20 pixels below the tutorial image

        # Update the button rect
        self.exit_tutorial_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        # Draw the "Exit Tutorial" button
        self.screen.blit(self.exit_tutorial_button_image, self.exit_tutorial_button_rect.topleft)

    def draw_health_bar(self):
        # Constants for health bar dimensions
        HEALTH_BAR_WIDTH = 300
        HEALTH_BAR_HEIGHT = 25

        # Calculate the health bar position centered above the player image
        HEALTH_BAR_X = self.player_rect.centerx - HEALTH_BAR_WIDTH // 2
        HEALTH_BAR_Y = self.player_rect.top - HEALTH_BAR_HEIGHT + 1

        # Draw the background of the health bar
        pygame.draw.rect(self.screen, YELLOW, (HEALTH_BAR_X, HEALTH_BAR_Y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        
        # Draw the current health
        current_health_width = HEALTH_BAR_WIDTH * (self.player_hp / self.max_player_hp)
        pygame.draw.rect(self.screen, GREEN, (HEALTH_BAR_X, HEALTH_BAR_Y, current_health_width, HEALTH_BAR_HEIGHT))

    def draw_enemy_health_bar(self):
        # Constants for health bar dimensions
        HEALTH_BAR_WIDTH = 300
        HEALTH_BAR_HEIGHT = 25

        # Calculate the health bar position centered above the enemy image
        HEALTH_BAR_X = self.enemy_rect.centerx - HEALTH_BAR_WIDTH // 2
        HEALTH_BAR_Y = self.enemy_rect.top + 1  # Adjust this value to lower the health bar

        # Draw the background of the health bar
        pygame.draw.rect(self.screen, YELLOW, (HEALTH_BAR_X, HEALTH_BAR_Y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        
        # Draw the current health
        current_health_width = HEALTH_BAR_WIDTH * (self.enemy_hp / self.max_enemy_hp)
        pygame.draw.rect(self.screen, RED, (HEALTH_BAR_X, HEALTH_BAR_Y, current_health_width, HEALTH_BAR_HEIGHT))


    def draw_points_indicator(self):
        points_text = self.font.render(f"Points: {self.points}", True, YELLOW)
        self.screen.blit(points_text, (self.SCREEN_WIDTH - 200, self.SCREEN_HEIGHT - 50))

    def display_damage_text(self, text, x, y):
        damage_surface = self.font.render(text, True, RED)
        self.screen.blit(damage_surface, (x, y))

    def display_healing_text(self, text, x, y):
        healing_surface = self.font.render(text, True, GREEN)
        self.screen.blit(healing_surface, (x, y))

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.battle_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                if self.skill_state != "basic":
                    self.skill_state = "basic"
            elif event.key == pygame.K_i:
                if self.skill_state!= "ult":
                    self.skill_state = "ult"
            elif event.key == pygame.K_u:
                if self.skill_state!= "skill":
                    self.skill_state = "skill"
            if self.skill_state != "":
                self.attack(self.skill_state)
            elif event.key == pygame.K_1:
                if self.attack_state != 1:
                    self.attack_state = 1
                    self.current_state = self.ATTACK_SELECTION
            elif event.key == pygame.K_2:
                if self.attack_state != 2:
                    self.attack_state = 2
                    self.current_state = self.ATTACK_SELECTION
            elif event.key == pygame.K_3:
                if self.attack_state != 3:
                    self.attack_state = 3
                    self.current_state = self.ATTACK_SELECTION
            elif event.key == pygame.K_4:
                if self.attack_state != 4:
                    self.attack_state = 4
                    self.current_state = self.ATTACK_SELECTION
            if self.attack_state != "":
                self.selected_attack = self.attack_state
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_j:
                self.skill_state = ""
            elif event.key == pygame.K_i:
                self.skill_state = ""
            elif event.key == pygame.K_u:
                self.skill_state = ""
            elif event.key == pygame.K_1:
                self.attack_state = ""
            elif event.key == pygame.K_2:
                self.attack_state = ""
            elif event.key == pygame.K_3:
                self.attack_state = ""
            elif event.key == pygame.K_4:
                self.attack_state = ""
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.current_state == self.NORMAL:
                if self.attack1_rect.collidepoint(mouse_pos):
                    self.selected_attack = 1
                    self.current_state = self.ATTACK_SELECTION
                elif self.attack2_rect.collidepoint(mouse_pos):
                    self.selected_attack = 2
                    self.current_state = self.ATTACK_SELECTION
                elif self.attack3_rect.collidepoint(mouse_pos):
                    self.selected_attack = 3
                    self.current_state = self.ATTACK_SELECTION
                elif self.attack4_rect.collidepoint(mouse_pos):
                    self.selected_attack = 4
                    self.current_state = self.ATTACK_SELECTION
                elif self.tutorial_button_rect.collidepoint(mouse_pos):
                    self.current_state = self.TUTORIAL
            elif self.current_state == self.ATTACK_SELECTION:
                if self.basic_rect.collidepoint(mouse_pos):
                    self.attack('basic')
                elif self.ult_rect.collidepoint(mouse_pos):
                    self.attack('ult')
                elif self.skill_rect.collidepoint(mouse_pos):
                    self.attack('skill')
            elif self.current_state == self.TUTORIAL:
                if self.exit_tutorial_button_rect.collidepoint(mouse_pos):
                    self.current_state = self.NORMAL

    def attack(self, attack_type):
        self.calculate_damage(attack_type)

    def calculate_damage(self, attack_type):
        if attack_type == "basic":
            if self.selected_attack == 1:
                damage = random.randint(10, 20) + self.attack1_buff
            elif self.selected_attack == 2:
                damage = random.randint(15, 25) + self.attack2_buff
            elif self.selected_attack == 3:
                damage = random.randint(10, 20)
            elif self.selected_attack == 4:
                damage = random.randint(5, 15)
            self.enemy_hp -= damage
            self.enemy_damage_text = f"-{damage}"
            self.shake_screen('enemy')
            self.enemy_damage_time = pygame.time.get_ticks()
            pygame.mixer.Sound.play(self.enemy_damage_sound)  # Play enemy damage sound
            self.points = min(self.points + 1, self.max_points)
            self.current_state = self.ENEMY_TURN
            self.enemy_attack_timer = pygame.time.get_ticks() + self.enemy_attack_delay

        elif attack_type == "skill":
            if self.points >= 1:
                if self.selected_attack == 1:
                    damage = random.randint(30, 50) + self.attack1_buff
                    self.enemy_hp -= damage
                    self.enemy_damage_text = f"-{damage}"
                    self.enemy_damage_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(self.enemy_damage_sound)  # Play enemy damage sound
                elif self.selected_attack == 2:
                    damage = random.randint(35, 60) + self.attack2_buff
                    self.enemy_hp -= damage
                    self.enemy_damage_text = f"-{damage}"
                    self.enemy_damage_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(self.enemy_damage_sound)  # Play enemy damage sound
                elif self.selected_attack == 3:
                    self.attack1_buff += random.randint(10, 20)
                    self.attack2_buff += random.randint(10, 20)
                    damage = 0
                    self.enemy_hp -= damage
                    self.enemy_damage_text = f"-{damage}"
                    self.enemy_damage_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(self.enemy_damage_sound)  # Play enemy damage sound
                elif self.selected_attack == 4:
                    heal = random.randint(10, 30)
                    self.player_hp = min(self.player_hp + heal, self.max_player_hp)
                    self.player_healing_text = f"+{heal}"
                    self.player_healing_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(self.healing_sound)  # Play healing sound
                self.points -= 1
                self.shake_screen('enemy')
                self.current_state = self.ENEMY_TURN
                self.enemy_attack_timer = pygame.time.get_ticks() + self.enemy_attack_delay

        elif attack_type == "ult":
            if self.points >= 3:
                if self.selected_attack == 1:
                    damage = random.randint(50, 70) + self.attack1_buff
                    self.enemy_hp -= damage
                    self.enemy_damage_text = f"-{damage}"
                    self.enemy_damage_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(self.enemy_damage_sound)  # Play enemy damage sound
                elif self.selected_attack == 2:
                    damage = random.randint(60, 80) + self.attack2_buff
                    self.enemy_hp -= damage
                    self.enemy_damage_text = f"-{damage}"
                    self.enemy_damage_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(self.enemy_damage_sound)  # Play enemy damage sound
                elif self.selected_attack == 3:
                    self.attack1_buff += random.randint(5, 10)
                    self.attack2_buff += random.randint(5, 10)
                    damage = 0
                    self.enemy_hp -= damage
                    self.enemy_damage_text = f"-{damage}"
                    self.enemy_damage_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(self.enemy_damage_sound)  # Play enemy damage sound
                elif self.selected_attack == 4:
                    heal = random.randint(30, 70)
                    self.player_hp = min(self.player_hp + heal, self.max_player_hp)
                    self.player_healing_text = f"+{heal}"
                    self.player_healing_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(self.healing_sound)  # Play healing sound
                self.points -= 3
                self.shake_screen('enemy')
                self.current_state = self.ENEMY_TURN
                self.enemy_attack_timer = pygame.time.get_ticks() + self.enemy_attack_delay

        if self.enemy_hp <= 0:
            self.enemy_hp = 0
            self.battle_over = True
        elif self.player_hp <= 0:
            self.player_hp = 0
            self.battle_over = True

    def shake_screen(self, entity):
        self.shaking = True
        self.shaking_entity = entity
        self.shake_start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.current_state == self.ENEMY_TURN:
            if current_time - self.enemy_attack_timer > self.enemy_attack_delay:
                damage = random.randint(self.enemy_damage_range[0], self.enemy_damage_range[1])
                pygame.mixer.Sound.play(self.damage_sound)  # Play player damage sound
                self.shake_screen('player')
                self.player_hp -= damage
                self.player_damage_text = f"-{damage}"
                self.player_damage_time = current_time
                self.enemy_attack_timer = current_time
                self.current_state = self.NORMAL

        if self.shaking and current_time - self.shake_start_time > self.shake_duration:
            self.shaking = False
            self.shaking_entity = None

        if self.player_hp <= 0 or self.enemy_hp <= 0:
            self.battle_over = True

    def draw(self):
        # Draw the background first to keep it unchanged
        self.draw_background()
        
        # Draw other elements on top of the background
        self.draw_player()
        self.draw_enemy()
        self.draw_health_bar()
        self.draw_enemy_health_bar()
        self.draw_points_indicator()
        self.draw_tutorial_button()

        # Display damage texts if applicable
        if self.player_damage_text and pygame.time.get_ticks() - self.player_damage_time < 1000:
            self.display_damage_text(self.player_damage_text, 150, 400)
        if self.player_healing_text and pygame.time.get_ticks() - self.player_healing_time < 1000:
            self.display_healing_text(self.player_healing_text, 150, 400)
        if self.enemy_damage_text and pygame.time.get_ticks() - self.enemy_damage_time < 1000:
            self.display_damage_text(self.enemy_damage_text, self.SCREEN_WIDTH - 400, 50)

        # Depending on the current state, draw different elements
        if self.current_state == self.NORMAL:
            self.draw_attack_buttons()
        elif self.current_state == self.ATTACK_SELECTION:
            # Instead of filling the screen with black, just keep the existing background
            if self.selected_attack == 1:
                self.screen.blit(self.attack1_basic_image, self.basic_rect.topleft)
                self.screen.blit(self.attack1_ult_image, self.ult_rect.topleft)
                self.screen.blit(self.attack1_skill_image, self.skill_rect.topleft)
            elif self.selected_attack == 2:
                self.screen.blit(self.attack2_basic_image, self.basic_rect.topleft)
                self.screen.blit(self.attack2_ult_image, self.ult_rect.topleft)
                self.screen.blit(self.attack2_skill_image, self.skill_rect.topleft)
            elif self.selected_attack == 3:
                self.screen.blit(self.attack3_basic_image, self.basic_rect.topleft)
                self.screen.blit(self.attack3_ult_image, self.ult_rect.topleft)
                self.screen.blit(self.attack3_skill_image, self.skill_rect.topleft)
            elif self.selected_attack == 4:
                self.screen.blit(self.attack4_basic_image, self.basic_rect.topleft)
                self.screen.blit(self.attack4_ult_image, self.ult_rect.topleft)
                self.screen.blit(self.attack4_skill_image, self.skill_rect.topleft)
        elif self.current_state == self.TUTORIAL:
            self.draw_tutorial_screen()


    def run(self):
        while not self.battle_over:
            for event in pygame.event.get():
                self.handle_event(event)

            self.update()
            self.draw()
            
            pygame.display.flip()  # Update the display
            
            # Add a small delay to control the frame rate
            pygame.time.delay(30)

        # Stop music and quit Pygame
        pygame.mixer.music.stop()
        

