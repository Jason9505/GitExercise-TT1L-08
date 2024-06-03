import pygame
import random
from settings import *
from tile import Tile
from player import Player
from support import *
from random import choice
from debug import debug
from monster import Monster

character_width = 50
character_height = 50

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, dialogues, image, name, scale_factor=0.5):
        super().__init__()  
        self.original_image = image
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dialogues = dialogues
        self.current_dialogue_index = 0
        self.dialogue_index = 0
        self.name = name

class Level:
    def __init__(self):
        # self.game = game  # Reference to the main game object

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        # self.attacks = pygame.sprite.Group()  # Add this line


        # sprite setup
        self.create_map()

        # NPC setup
        self.npcs = pygame.sprite.Group()
        geopard_image = pygame.image.load("../GitExercise/character/geo.png")
        nurse_image = pygame.image.load("../GitExercise/character/nurse1.png")
        angel_image = pygame.image.load("../GitExercise/character/angel1.png")
        
        scale_factor = 0.5
        self.npcs.add(NPC(600, 400, [
            ["", "There used to be almost an infinite amount village through out this world.", "Everything changes when the Demon Lord, Zoltraak arise from the underworld.", 
            "And so began the age of chaos. He and his army sweep the land.", "Burning down villages and basically destroying every land he steps on.",
            "Some try to fight the demon lord but never return.", "Many choose to run away to seek for a safer place to hide but it’s no use.", 
            "And now we’re the last ones standing but we’re not safe either.", "Cause it’s only a matter of time before the demon lord found us and claim this realm once."],
            ["", "Unfortunately, I have no clue also.", "It could be a couple of days, to a couple of months.", "But everything is alright now. Now that you are here. "]
        ], geopard_image, "Geopard", scale_factor))

        self.npcs.add(NPC(800, 400, [
            ["", "You should know better than to face Zoltraak when you’re not even at your full potential."]
        ], nurse_image, "Nurse", scale_factor))

        self.npcs.add(NPC(600, 500, [
            ["", "Follow the path to the village to seek your purpose of this realm.", "Press w to go forward, press a to go left, press d to go right and press s to go backward."]
        ], angel_image, "???", scale_factor))

        self.font = pygame.font.Font(None, 36)
        self.show_dialogue = False
        self.show_press_e = False
        self.e_key_pressed = False
        self.text_position = 0
        self.active_npc = None

    def load_monster_frames(self):
        def load_frames(sheet, count, scale):
            frames = [sheet.subsurface((i * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT)) for i in range(count)]
            return [pygame.transform.scale(frame, (FRAME_WIDTH // scale, FRAME_HEIGHT // scale)) for frame in frames]
        
        scale_factor = 2  # Adjust this factor to scale the monsters smaller

        self.monster_frames = {
            'monster1': {
                'up': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/monster_up.png"), 9,scale_factor),
                'down': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/monster_down.png"), 9,scale_factor),
                'left': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/monster_left.png"), 9,scale_factor),
                'right': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/monster_right.png"), 9,scale_factor)
            },
            'monster2': {
                'up': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/mon2_up.png"), 9,scale_factor),
                'down': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/mon2_down.png"), 9,scale_factor),
                'left': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/mon2_left.png"), 9,scale_factor),
                'right': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/mon2_right.png"), 9,scale_factor)
            },
            'monster3': {
                'up': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/mon3_up.png"), 9,scale_factor),
                'down': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/mon3_down.png"), 9,scale_factor),
                'left': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/mon3_left.png"), 9,scale_factor),
                'right': load_frames(pygame.image.load("C:/Users/User/Projects/GitExercise-TT1L-08/graphics/monster/mon3_right.png"), 9,scale_factor)
            }
        }

    def create_monsters(self):
        monsters = []
        for i, spawn_area in enumerate(self.spawn_areas):
            monster_type = f'monster{i + 1}'
            frames = self.monster_frames[monster_type]
            for _ in range(self.max_monsters):
                x = random.randint(spawn_area.left, spawn_area.right - FRAME_WIDTH)
                y = random.randint(spawn_area.top, spawn_area.bottom - FRAME_HEIGHT)
                monsters.append(Monster(x, y, spawn_area, frames))
        return monsters

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
            'boundary': import_csv_layout('C:/Users/User/Projects/GitExercise-TT1L-08/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('C:/Users/User/Projects/GitExercise-TT1L-08/map/map_Grass.csv'),
            'object': import_csv_layout('C:/Users/User/Projects/GitExercise-TT1L-08/map/map_Objects.csv'),
        }
        graphics = {
            'grass': import_folder('C:/Users/User/Projects/GitExercise-TT1L-08/graphics/Grass'),
            'objects': import_folder('C:/Users/User/Projects/GitExercise-TT1L-08/graphics/objects')
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

        self.player = Player((1320,2190),[self.visible_sprites],self.obstacle_sprites)
        
    def draw_text(self, surface, text, position, font, color, max_length):
        text_surface = font.render(text[:max_length], True, color)
        surface.blit(text_surface, position)
        return text_surface

    def check_collision(self):
        if self.active_npc is None:
            for npc in self.npcs:
                if self.player.rect.colliderect(npc.rect):
                    self.active_npc = npc
                    self.show_press_e = True
                    break
        else:
            if not self.player.rect.colliderect(self.active_npc.rect):
                self.show_dialogue = False
                self.show_press_e = False
                self.e_key_pressed = False
                self.text_position = 0
                self.active_npc = None

    def handle_dialogue(self):
        if self.active_npc and self.e_key_pressed and not self.show_dialogue:
            self.show_dialogue = True

        if self.show_dialogue and self.active_npc:
            npc = self.active_npc
            dialogue = npc.dialogues[npc.current_dialogue_index][self.text_position]
            self.draw_text(self.display_surface, dialogue, (100, 100), self.font, (255, 255, 255), 100)       


    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.status)

        for npc in self.npcs:
            self.display_surface.blit(npc.image, npc.rect.topleft)

        if self.show_press_e:
            self.draw_text(self.display_surface, "Press E to talk", (100, 50), self.font, (255, 255, 255), 50)
        
        self.handle_dialogue()

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            self.e_key_pressed = True
            if self.active_npc:
                if self.show_dialogue:
                    self.text_position += 1
                    if self.text_position >= len(self.active_npc.dialogues[self.active_npc.current_dialogue_index]):
                        self.text_position = 0
                        self.active_npc.current_dialogue_index += 1
                        self.show_dialogue = False
                        self.e_key_pressed = False
                else:
                    self.show_dialogue = True

        # Update monsters
        for monster in self.monsters:
            monster.move()
            monster.animate()
            if random.random() < 0.01:
                monster.direction = random.choice(['left', 'right', 'up', 'down'])

        # Draw monsters
        for monster in self.monsters:
            monster.draw(self.display_surface, self.camera)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('C:/Users/User/Projects/GitExercise-TT1L-08/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):

        # Getting the offset
        if player:
            self.offset.x = player.rect.centerx - self.half_width
            self.offset.y = player.rect.centery - self.half_height
        else:
            self.offset = pygame.math.Vector2(0, 0)  # Centered view

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        # draw sprites
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)



