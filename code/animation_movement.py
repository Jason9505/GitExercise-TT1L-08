import pygame
import sys
import math

# Constants
TILESIZE = 50  # Set to the same size as your character frame
PLAYER_LAYER = 1

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Load sprite sheets
        self.sprite_sheet_up = pygame.image.load("img/character_sheet_up.png")
        self.sprite_sheet_down = pygame.image.load("img/character_sheet_down.png")
        self.sprite_sheet_left = pygame.image.load("img/character_sheet_left.png")
        self.sprite_sheet_right = pygame.image.load("img/character_sheet_right.png")
        self.attack_spritesheet_up = Spritesheet('img/mc attack spritesheet up.png')
        self.attack_spritesheet_down = Spritesheet('img/mc attack spritesheet down.png')
        self.attack_spritesheet_left = Spritesheet('img/mc attack spritesheet left.png')
        self.attack_spritesheet_right = Spritesheet('img/mc attack spritesheet right.png')

        # Extract frames for animations
        self.frames_up = self.extract_frames(self.sprite_sheet_up)
        self.frames_down = self.extract_frames(self.sprite_sheet_down)
        self.frames_left = self.extract_frames(self.sprite_sheet_left)
        self.frames_right = self.extract_frames(self.sprite_sheet_right)

        self.attack_frames_up = self.extract_frames(self.attack_spritesheet_up.sheet)
        self.attack_frames_down = self.extract_frames(self.attack_spritesheet_down.sheet)
        self.attack_frames_left = self.extract_frames(self.attack_spritesheet_left.sheet)
        self.attack_frames_right = self.extract_frames(self.attack_spritesheet_right.sheet)

        self.player = Player(self)
        self.all_sprites.add(self.player)

    def extract_frames(self, sheet):
        frames = []
        frame_width = 50
        frame_height = 50
        for i in range(8):
            frame = sheet.subsurface((i * frame_width, 0), (frame_width, frame_height))
            frame.set_colorkey((255, 0, 255))  # Assuming (255, 0, 255) is the transparent color
            frames.append(frame)
        return frames

    def new(self):
        # Start a new game
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
                self.player.attack()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 0, 255))  # Assuming (255, 0, 255) is the transparent color
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = self.game.frames_down[0]
        self.rect = self.image.get_rect()
        self.rect.x = (1280 - 50) // 2
        self.rect.y = (720 - 50) // 2
        self.speed = 5
        self.facing = 'down'
        self.current_frames = self.game.frames_down
        self.is_moving = False

    def update(self):
        self.handle_keys()
        self.animate()

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.current_frames = self.game.frames_left
            self.facing = 'left'
            self.is_moving = True
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.current_frames = self.game.frames_right
            self.facing = 'right'
            self.is_moving = True
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.current_frames = self.game.frames_up
            self.facing = 'up'
            self.is_moving = True
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.current_frames = self.game.frames_down
            self.facing = 'down'
            self.is_moving = True

    def animate(self):
        if self.is_moving:
            self.image = self.current_frames[int(pygame.time.get_ticks() / 100) % len(self.current_frames)]
        else:
            self.image = self.current_frames[0]

    def attack(self):
        # Pass player's current position to the attack
        Attack(self.game, self.rect.x, self.rect.y, self.facing)

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites, game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        self.direction = direction

        self.animation_loop = 0

        if direction == 'up':
            self.current_frames = self.game.attack_frames_up
        elif direction == 'down':
            self.current_frames = self.game.attack_frames_down
        elif direction == 'left':
            self.current_frames = self.game.attack_frames_left
        elif direction == 'right':
            self.current_frames = self.game.attack_frames_right

        self.image = self.current_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

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

# Main execution
game = Game()
game.new()
pygame.quit()
sys.exit()
