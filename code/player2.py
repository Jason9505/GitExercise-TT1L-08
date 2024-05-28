import pygame
from settings import *

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 0, 255))  # Assuming (255, 0, 255) is the transparent color
        sprite = pygame.transform.scale(sprite, (TILESIZE, TILESIZE))
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, game):
        super().__init__(groups)
        self.game = game
        self.image = self.game.frames_down[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -4)

        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.facing = 'down'
        self.current_frames = self.game.frames_down
        self.is_moving = False

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.current_frames = self.game.frames_up
            self.facing = 'up'
            self.is_moving = True
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.current_frames = self.game.frames_down
            self.facing = 'down'
            self.is_moving = True
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.current_frames = self.game.frames_right
            self.facing = 'right'
            self.is_moving = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.current_frames = self.game.frames_left
            self.facing = 'left'
            self.is_moving = True
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)
        self.animate()

    def animate(self):
        if self.is_moving:
            self.image = self.current_frames[int(pygame.time.get_ticks() / 100) % len(self.current_frames)]
        else:
            self.image = self.current_frames[0]

    def attack(self):
        Attack(self.game, self.rect.x, self.rect.y, self.facing)

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction):
        super().__init__(game.all_sprites, game.attacks)
        self.game = game
        self.x = x
        self.y = y
        self.direction = direction

        if direction == 'up':
            self.current_frames = self.game.attack_frames_up
        elif direction == 'down':
            self.current_frames = self.game.attack_frames_down
        elif direction == 'left':
            self.current_frames = self.game.attack_frames_left
        elif direction == 'right':
            self.current_frames = self.game.attack_frames_right

        self.image = self.current_frames[0]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.animation_loop = 0

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
        if hits:
            self.game.transition_to_battle()

    def animate(self):
        self.image = self.current_frames[int(self.animation_loop) % len(self.current_frames)]
        self.animation_loop += 0.5
        if self.animation_loop >= len(self.current_frames):
            self.kill()
