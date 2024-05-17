import pygame
import math
import random
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILESIZE = 64
PLAYER_LAYER = 2

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((0, 0, 0))
        return sprite

class Game: 
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()  # Define enemies group for collision detection
        self.attack_spritesheet = Spritesheet('img/mc spritesheet.png')
        self.player = Player(self)  # Create a player instance for facing direction

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    attack = Attack(self, x, y)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        screen.fill((0, 0, 0))
        self.all_sprites.draw(screen)
        pygame.display.flip()

class Player:
    def __init__(self, game):
        self.game = game
        self.facing = 'down'  # Initial facing direction

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y 
        self.width = 64
        self.height = 64

        self.animation_loop = 0

        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.right_animations = [
            self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(192, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(256, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(320, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(384, 0, self.width, self.height)
        ]

        self.down_animations = [
            self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(192, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(256, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(320, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(384, 64, self.width, self.height)
        ]

        self.left_animations = [
            self.game.attack_spritesheet.get_sprite(0, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(192, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(256, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(320, 128, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(384, 128, self.width, self.height)
        ]

        self.up_animations = [
            self.game.attack_spritesheet.get_sprite(0, 192, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 192, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 192, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(192, 192, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(256, 192, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(320, 192, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(384, 192, self.width, self.height)
        ]

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)

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


# Main execution
game = Game()
game.run()
pygame.quit()
sys.exit()
