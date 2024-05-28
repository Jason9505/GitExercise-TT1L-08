import pygame
from settings import *

# Constants
TILESIZE = 50  # Set to the same size as your character frame
PLAYER_LAYER = 1

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Load sprite sheets
        self.sprite_sheet_up = self.load_image("img/character_sheet_up.png")
        self.sprite_sheet_down = self.load_image("img/character_sheet_down.png")
        self.sprite_sheet_left = self.load_image("img/character_sheet_left.png")
        self.sprite_sheet_right = self.load_image("img/character_sheet_right.png")
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

        self.player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), self.all_sprites, self.obstacle_sprites, self)
        self.all_sprites.add(self.player)

    def load_image(self, path):
        return pygame.image.load(path).convert()

    def extract_frames(self, sheet):
        frames = []
        frame_width, frame_height = TILESIZE, TILESIZE
        for i in range(8):
            frame = sheet.subsurface((i * frame_width, 0), (frame_width, frame_height))
            frame.set_colorkey((255, 0, 255))  # Assuming (255, 0, 255) is the transparent color
            frames.append(frame)
        return frames

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def handle_events(self):
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
    def __init__(self, pos, groups, obstacle_sprites, game):
        super().__init__(groups)
        self.game = game
        self.image = self.game.frames_down[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -18)

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
game.run()
pygame.quit()
sys.exit()
