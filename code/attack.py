import pygame
import math
import sys
import os
import subprocess

# Constants
TILESIZE = 128
PLAYER_LAYER = 1

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Ensure the correct path to the spritesheet
        self.attack_spritesheet = Spritesheet('img/mc spritesheet.png')

        self.player = Player(self)  # Assuming there is a Player class

    def new(self):
        # Create a new game instance
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                Attack(self, x, y)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def transition_to_battle(self):
        battle_screen = BattleScreen(self)
        battle_screen.run()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 0, 255))  # Assuming (255, 0, 255) is the transparent color
        return sprite

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y 
        self.width = TILESIZE
        self.height = TILESIZE

        self.animation_loop = 0

        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.right_animations = [
            self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(256, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(384, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(512, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(640, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(768, 0, self.width, self.height)
        ]

        self.down_animations = [
            self.game.attack_spritesheet.get_sprite(0, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(256, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(384, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(512, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(640, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(768, 128, self.width, self.height)
        ]

        self.left_animations = [
            self.game.attack_spritesheet.get_sprite(0, 256, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 256, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(256, 256, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(384, 256, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(512, 256, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(640, 256, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(768, 256, self.width, self.height)
        ]

        self.up_animations = [
            self.game.attack_spritesheet.get_sprite(0, 384, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 384, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(256, 384, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(384, 384, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(512, 384, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(640, 384, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(768, 384, self.width, self.height)
        ]

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
        if hits:
            self.game.transition_to_battle()
            subprocess.call(["python", "battle_screen.py"])

    def animate(self):
        direction = self.game.player.facing

        if direction == 'up':
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 7:
                self.kill()

        if direction == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 7:
                self.kill()

        if direction == 'left':
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 7:
                self.kill()

        if direction == 'right':
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 7:
                self.kill()

# Assuming there is a Player class with a facing attribute
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.facing = 'down'  # default facing direction

# Main execution
game = Game()
game.new()
pygame.quit()
sys.exit()
