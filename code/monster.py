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

    def move(self):
        # Update the monster's position based on its own logic, not the character's position
        if self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed

        # Ensure the monster stays within the designated area
        if self.x < self.area.left:
            self.x = self.area.left
            self.direction = 'right'
        elif self.x > self.area.right - FRAME_WIDTH:
            self.x = self.area.right - FRAME_WIDTH
            self.direction = 'left'
        if self.y < self.area.top:
            self.y = self.area.top
            self.direction = 'down'
        elif self.y > self.area.bottom - FRAME_HEIGHT:
            self.y = self.area.bottom - FRAME_HEIGHT
            self.direction = 'up'

    def animate(self):
        # Update animation frame
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_interval:
            self.frame_index = (self.frame_index + 1) % len(self.frames[self.direction])
            self.last_update = now

    def draw(self, surface, camera):
        # Draw the monster on the screen
        surface.blit(self.frames[self.direction][self.frame_index], (self.x - camera.left, self.y - camera.top))