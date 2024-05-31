import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from random import choice
from debug import debug

class Level:
    def __init__(self):
        # self.game = game  # Reference to the main game object

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        # self.attacks = pygame.sprite.Group()  # Add this line


        # Load sprite sheets
        # self.sprite_sheet_up = self.load_image("../graphics/img/character_sheet_up.png")
        # self.sprite_sheet_down = self.load_image("../graphics/img/character_sheet_down.png")
        # self.sprite_sheet_left = self.load_image("../graphics/img/character_sheet_left.png")
        # self.sprite_sheet_right = self.load_image("../graphics/img/character_sheet_right.png")
        # self.attack_spritesheet_up = self.load_image('../graphics/img/mc attack spritesheet up.png')
        # self.attack_spritesheet_down = self.load_image('../graphics/img/mc attack spritesheet down.png')
        # self.attack_spritesheet_left = self.load_image('../graphics/img/mc attack spritesheet left.png')
        # self.attack_spritesheet_right = self.load_image('../graphics/img/mc attack spritesheet right.png')

        # # Extract frames for animations without scaling
        # self.frames_up = self.extract_frames(self.sprite_sheet_up)
        # self.frames_down = self.extract_frames(self.sprite_sheet_down)
        # self.frames_left = self.extract_frames(self.sprite_sheet_left)
        # self.frames_right = self.extract_frames(self.sprite_sheet_right)
        # self.attack_frames_up = self.extract_frames(self.attack_spritesheet_up)
        # self.attack_frames_down = self.extract_frames(self.attack_spritesheet_down)
        # self.attack_frames_left = self.extract_frames(self.attack_spritesheet_left)
        # self.attack_frames_right = self.extract_frames(self.attack_spritesheet_right)

        # sprite setup
        self.create_map()

    # def load_image(self, path):
    #     return pygame.image.load(path).convert_alpha()  # Use convert_alpha to keep transparency

    # def extract_and_scale_frames(self, sheet):
    #     frames = []
    #     frame_width, frame_height = 50, 50  # Original frame size
    #     for i in range(8):
    #         frame = sheet.subsurface((i * frame_width, 0), (frame_width, frame_height))
    #         frame = pygame.transform.scale(frame, (TILESIZE, TILESIZE))
    #         frame.set_colorkey((255, 0, 255))  # Assuming (255, 0, 255) is the transparent color
    #         frames.append(frame)
    #     return frames

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/map/map_Grass.csv'),
            'object': import_csv_layout('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/map/map_Objects.csv'),
        }
        graphics = {
            'grass': import_folder('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/Grass'),
            'objects': import_folder('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/objects')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

        self.player = Player((1320,2180),[self.visible_sprites],self.obstacle_sprites)


    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.status)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        # draw sprites
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
