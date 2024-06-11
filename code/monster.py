import pygame
import random
from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, spawn_area, frames):
        super().__init__()
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames['down'][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.spawn_area = spawn_area
        self.direction = 'down'
        self.speed = 2
        self.last_update = pygame.time.get_ticks()
        self.animation_interval = 200  # Example interval in milliseconds

    def move(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

        if self.rect.x < self.spawn_area.left:
            self.rect.x = self.spawn_area.left
            self.direction = 'right'
        elif self.rect.x > self.spawn_area.right - self.rect.width:
            self.rect.x = self.spawn_area.right - self.rect.width
            self.direction = 'left'
        if self.rect.y < self.spawn_area.top:
            self.rect.y = self.spawn_area.top
            self.direction = 'down'
        elif self.rect.y > self.spawn_area.bottom - self.rect.height:
            self.rect.y = self.spawn_area.bottom - self.rect.height
            self.direction = 'up'

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_interval:
            self.frame_index = (self.frame_index + 1) % len(self.frames[self.direction])
            self.image = self.frames[self.direction][self.frame_index]
            self.last_update = now

    def draw(self, surface, camera):
        surface.blit(self.image, (self.rect.x - camera.left, self.rect.y - camera.top))
