import pygame
import sys

class Game: 
    def __init__(self):
        pygame.init()
        self.attack_spritesheet = Spritesheet('img/mc spritesheet.png')