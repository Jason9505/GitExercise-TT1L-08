import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from enemy import Enemy
from npc import Npc
from battlescreen import BattleScreen

class Level:
    def __init__(self): 
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.npcs = []

        # sprite setup
        self.create_map()

        # dialogue variables
        self.show_dialogue = False
        self.active_npc = None
        self.text_position = 0
        self.scroll_speed = 1
        self.font = pygame.font.Font(None, 36)
        self.mouse_clicked = False
        self.e_key_pressed = False
        
    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../GitExercise-TT1L-08/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('../GitExercise-TT1L-08/map/map_Grass.csv'),
            'object': import_csv_layout('../GitExercise-TT1L-08/map/map_Objects.csv'),
            'entities': import_csv_layout('../GitExercise-TT1L-08/map/map_Entities.csv'),
            'npc': import_csv_layout('../GitExercise-TT1L-08/map/map_Npc.csv')
        }
        graphics = {
            'grass': import_folder('../GitExercise-TT1L-08/graphics/Grass'),
            'objects': import_folder('../GitExercise-TT1L-08/graphics/objects')
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

                        if style == 'entities':
                            if col == '72':
                                self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
                            else:
                                if col == '54':
                                    monster_name = 'monster lvl 1'
                                elif col == '56':
                                    monster_name = 'monster lvl 2'
                                elif col == '100':
                                    monster_name = 'boss'
                                else:
                                    monster_name = 'monster lvl 3'
                                Enemy(monster_name, (x, y), [self.visible_sprites], self.obstacle_sprites)

                        if style == 'npc':
                            if col == '997':
                                npc_name = 'angel_one'
                                dialogues = [["Follow the path to the village to seek your purpose of this realm.", "Press w to go forward, press a to go left, press d to go right and press s to go backward.", 
                                              "There are a lot skill u can use, every skill have different effect.", "Left-top have a tutorial to guide how to use the skill when you fighting", "HINT: Fourth skill can heal youself.", 
                                              "Now, there is a monster in front of you.", "Press SPACE to fight with thr monster!"]]
                                image = pygame.image.load("../GitExercise-TT1L-08/graphics/npc/angel_one/idle/0.png")
                                name = 'Angel'
                            elif col == '998':
                                npc_name = 'nurse'
                                dialogues = [["You should know better than to face Zoltraak when you’re not even at your full potential.", "Try your best and defeat it!"]]
                                image = pygame.image.load("../GitExercise-TT1L-08/graphics/npc/nurse/idle/0.png")
                                name = 'Nurse'
                            elif col == '999':
                                npc_name = 'geo'
                                dialogues = [["There used to be almost an infinite amount village throughout this world.", "Everything changes when the Demon Lord, Zoltraak arise from the underworld. ", 
                                              "And so began the age of chaos. He and his army sweep the land.", "Burning down villages and basically destroying every land he steps on.", 
                                              "Some try to fight the demon lord but never return. Many choose to run away to seek for a safer place to hide but it’s no use.", "And now we’re the last ones standing but we’re not safe either.", 
                                              "Cause it’s only a matter of time before the demon lord found us and claim this realm once and for all."], ["You are the one can be defeat the Demon.",
                                              "Please save the world. We will never forgive you, traveller."]]
                                image = pygame.image.load("../GitExercise-TT1L-08/graphics/npc/geo/idle/0.png")
                                name = 'Geopard'
                            else:
                                npc_name = 'angel_two'
                                dialogues = [["Are you ready?", "It's time to fight", "Use your skill wisely to kill it!", "Lets defeat the final boss, Zoltraak!"], ["Congraturation!!", "You defeat the boss and save the world!"]]
                                image = pygame.image.load("../GitExercise-TT1L-08/graphics/npc/angel_two/idle/0.png")
                                name = 'Angel'
                            npc = Npc(npc_name, (x, y), [self.visible_sprites], dialogues, image, name)
                            self.npcs.append(npc)
                              
    def run(self):
        # update and draw the game
        if not self.player.in_battle:
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            debug(self.player.status)
            self.player.check_enemy_collision([sprite for sprite in self.visible_sprites if isinstance(sprite, Enemy)])
        else:
            self.player.battle_screen.run()
            if self.player.battle_screen.battle_over:
                self.player.exit_battle_mode()

        # Handle dialogue
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e] and not self.e_key_pressed:
            self.e_key_pressed = True
            if not self.show_dialogue:
                for npc in self.npcs:
                    if npc.rect.colliderect(self.player.rect):
                        self.active_npc = npc
                        self.show_dialogue = True
                        self.active_npc.dialogue_index = 0
                        self.text_position = 0
                        break
            else:
                self.next_dialogue_text()
        elif not keys[pygame.K_e]:
            self.e_key_pressed = False

        self.handle_dialogue()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.next_dialogue_text()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.e_key_pressed = True
                else:
                    self.e_key_pressed = False
    
    def next_dialogue_text(self):
        if self.show_dialogue and self.active_npc:
            if self.active_npc.dialogue_index < len(self.active_npc.dialogues[self.active_npc.current_dialogue_index]) - 1:
                self.active_npc.dialogue_index += 1
                self.text_position = 0  # Reset text position for new dialogue
            else:
                self.show_dialogue = False
                self.active_npc.dialogue_index = 0
                # Switch to the next dialogue sequence
                self.active_npc.current_dialogue_index = (self.active_npc.current_dialogue_index + 1) % len(self.active_npc.dialogues)
                self.text_position = 0  # Reset text position for new dialogue

    def handle_dialogue(self):
        if self.show_dialogue and self.active_npc:
            if not self.mouse_clicked:  
                self.text_position += self.scroll_speed
                if self.text_position >= len(self.active_npc.get_current_dialogue()):
                    self.text_position = len(self.active_npc.get_current_dialogue())
            else:
                self.active_npc.advance_dialogue()
                self.text_position = 0
                self.mouse_clicked = False

            self.draw_dialogue(self.active_npc.get_current_dialogue())

    def draw_dialogue(self, dialogue_text):
        dialogue_box_width = 1500
        dialogue_box_height = 100
        dialogue_box_x = 50
        dialogue_box_y = self.display_surface.get_height() - dialogue_box_height - 50
        pygame.draw.rect(self.display_surface, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
        pygame.draw.rect(self.display_surface, (255, 255, 255), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height), 2)

        npc_image_x = dialogue_box_x + 5
        npc_image_y = dialogue_box_y - self.active_npc.image.get_height() - 30
        scaled_npc_image = pygame.transform.scale(self.active_npc.image, (self.active_npc.image.get_width() * 2, self.active_npc.image.get_height() * 2))
        self.display_surface.blit(scaled_npc_image, (npc_image_x, npc_image_y))

        npc_name_x = npc_image_x + scaled_npc_image.get_width() - 5
        npc_name_y = npc_image_y + 30
        self.draw_text(self.display_surface, self.active_npc.name, (npc_name_x, npc_name_y), self.font, (0, 0, 0), len(self.active_npc.name))

        draw_text = dialogue_text[:self.text_position]
        self.draw_text(self.display_surface, draw_text, (dialogue_box_x + 10, dialogue_box_y + 10), self.font, (255, 255, 255), len(draw_text))

    def draw_text(self, surface, text, position, font, color, max_length):
        text_surface = font.render(text[:max_length], True, color)
        surface.blit(text_surface, position)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('../GitExercise-TT1L-08/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

        # zoom 
        self.zoom_scale = 2
        self.internal_surf_size = (1200,1200)    
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_width,self.half_height))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_width
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_height

    def custom_draw(self, player):

        self.internal_surf.fill((80,167,232))


        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.floor_surf, floor_offset_pos)
        
        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset  + self.internal_offset
            self.internal_surf.blit(sprite.image, offset_pos)

        scaled_surf = pygame.transform.smoothscale(self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_width, self.half_height))
    
        self.display_surface.blit (scaled_surf, scaled_rect)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if isinstance(sprite, Enemy)]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)