import pygame
from settings import *
from support import import_folder

# class Spritesheet:
#     def __init__(self, file):
#         self.sheet = pygame.image.load(file).convert_alpha()  # Use convert_alpha to keep transparency

#     def get_sprite(self, x, y, width, height):
#         sprite = pygame.Surface((width, height), pygame.SRCALPHA)  # Use SRCALPHA for transparency
#         sprite.blit(self.sheet, (0, 0), (x, y, width, height))
#         sprite.set_colorkey((255, 0, 255))  # Assuming (255, 0, 255) is the transparent color
#         sprite = pygame.transform.scale(sprite, (TILESIZE, TILESIZE))
#         return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/User/Projects/GitExercise-TT1L-08/graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-18) #try to figure out this number (dkaljsdlkajlksdjlkjaldjljaljdla)

        # graphics setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # movement
        self.direction = pygame.math.Vector2()
        self.speed = 2
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

    def import_player_assets(self):
        character_path = 'C:/Users/User/Projects/GitExercise-TT1L-08/graphics/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        if not self.attacking:
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
               print('attack')

			# magic input 
            if keys[pygame.K_LCTRL]:
               self.attacking = True
               self.attack_time = pygame.time.get_ticks()
               print('magic')
                    
    def get_status(self):

        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
           if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]

		# loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

		# set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)

# class Attack(pygame.sprite.Sprite):
#     def __init__(self, game, x, y, direction, groups, frames):
#         super().__init__(groups)
#         self.game = game  # Store the game instance
#         self.direction = direction
#         self.frames = frames

#         if direction == 'up':
#             self.current_frames = self.frames[0]
#         elif direction == 'down':
#             self.current_frames = self.frames[1]
#         elif direction == 'left':
#             self.current_frames = self.frames[2]
#         elif direction == 'right':
#             self.current_frames = self.frames[3]

#         self.image = self.current_frames[0]
#         self.rect = self.image.get_rect(topleft=(x, y))

#         self.animation_loop = 0

#     def update(self):
#         self.animate()
#         self.collide()

#     def collide(self):
#         hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
#         if hits:
#             self.game.transition_to_battle()

#     def animate(self):
#         self.image = self.current_frames[int(self.animation_loop) % len(self.current_frames)]
#         self.animation_loop += 0.5
#         if self.animation_loop >= len(self.current_frames):
#             self.kill()
