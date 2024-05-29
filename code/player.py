import pygame
from settings import *

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()  # Use convert_alpha to keep transparency

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)  # Use SRCALPHA for transparency
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 0, 255))  # Assuming (255, 0, 255) is the transparent color
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, pos, groups, obstacle_sprites, frames):
        super().__init__(groups)
        self.game = game  # Store the game instance
        self.frames_up, self.frames_down, self.frames_left, self.frames_right = frames
        self.image = self.frames_down[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -4)

        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.facing = 'down'
        self.current_frames = self.frames_down
        self.is_moving = False

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False

        if keys[pygame.K_w]:  # W key for up
            self.direction.y = -1
            self.current_frames = self.frames_up
            self.facing = 'up'
            self.is_moving = True
        elif keys[pygame.K_s]:  # S key for down
            self.direction.y = 1
            self.current_frames = self.frames_down
            self.facing = 'down'
            self.is_moving = True
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:  # D key for right
            self.direction.x = 1
            self.current_frames = self.frames_right
            self.facing = 'right'
            self.is_moving = True
        elif keys[pygame.K_a]:  # A key for left
            self.direction.x = -1
            self.current_frames = self.frames_left
            self.facing = 'left'
            self.is_moving = True
        else:
            self.direction.x = 0

        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            self.attack()

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
        super().update()  # Ensure the parent class update method is called

    def animate(self):
        if self.is_moving:
            self.image = self.current_frames[int(pygame.time.get_ticks() / 100) % len(self.current_frames)]
        else:
            self.image = self.current_frames[0]

    def attack(self):
        Attack(self.game, self.rect.x, self.rect.y, self.facing, [self.game.visible_sprites, self.game.attacks], self.get_attack_frames())

    def get_attack_frames(self):
        if self.facing == 'up':
            return self.game.attack_frames_up
        elif self.facing == 'down':
            return self.game.attack_frames_down
        elif self.facing == 'left':
            return self.game.attack_frames_left
        elif self.facing == 'right':
            return self.game.attack_frames_right

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction, groups, frames):
        super().__init__(groups)
        self.game = game  # Store the game instance
        self.direction = direction
        self.frames = frames

        if direction == 'up':
            self.current_frames = self.frames[0]
        elif direction == 'down':
            self.current_frames = self.frames[1]
        elif direction == 'left':
            self.current_frames = self.frames[2]
        elif direction == 'right':
            self.current_frames = self.frames[3]

        self.image = self.current_frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

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
