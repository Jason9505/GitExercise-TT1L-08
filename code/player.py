
import pygame
from settings import *
from support import import_folder
from entity import Entity
from battlescreen import BattleScreen
from gameclearscreen import GameClearScreen

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../data/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -18)  # try to figure out this number

        # graphics setup
        self.import_player_assets()
        self.status = 'down'

        # movement
        self.speed = 4
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites
        self.direction = pygame.math.Vector2()

        # battle state
        self.in_battle = False
        self.battle_screen = None
        self.saved_position = None
        self.defeated_boss = False

    def import_player_assets(self):
        character_path = '../data/player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        if not self.attacking and not self.in_battle:
            keys = pygame.key.get_pressed()

            # movement input
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if 'idle' not in self.status and 'attack' not in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if 'attack' not in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Ensure frame index is within bounds
        if 0 <= self.frame_index < len(animation):
            self.image = animation[int(self.frame_index)]
        else:
            # Handle out-of-bounds frame index
            print("Frame index out of bounds:", self.frame_index)

        self.rect = self.image.get_rect(center=self.hitbox.center)

    def check_enemy_collision(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect) and self.attacking and not self.in_battle:
                monster_name = enemy.monster_name  # Corrected to use enemy instead of monster
                self.enter_battle_mode(enemy, monster_name)
                return True
        return False

    def enter_battle_mode(self, enemy, monster_name):
        self.saved_position = self.rect.topleft
        self.in_battle = True
        self.battle_screen = BattleScreen(player=self, enemy=enemy, enemy_name=monster_name)
        self.battle_screen.run()
        if self.battle_screen.enemy_hp <= 0:
            if monster_name == 'boss':
                self.defeated_boss = True
            enemy.kill()
        self.exit_battle_mode()

    def exit_battle_mode(self):
        self.in_battle = False
        self.rect.topleft = self.saved_position
        self.battle_screen = None
        if self.defeated_boss:
            self.defeated_boss = False
            game_clear_screen = GameClearScreen()
            game_clear_screen.run()

    def update(self):
        if not self.in_battle:
            self.input()
            self.cooldowns()
            self.get_status()
            self.animate()
            self.move(self.speed)
        elif self.battle_screen and self.battle_screen.battle_over:
            self.exit_battle_mode()
        if self.battle_screen and self.battle_screen.player_hp <= 0:
            self.game_over()
