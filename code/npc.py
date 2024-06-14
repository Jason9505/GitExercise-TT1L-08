import pygame
from settings import *
from entity import Entity
from support import *

class Npc(Entity):
    def __init__(self, npc_name, pos, groups, dialogues, image, name):
        # general setup
        super().__init__(groups)
        self.sprite_type = 'npc'

        # graphics setup
        self.import_graphics(npc_name)
        self.status = 'idle'
        self.image = image
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # dialogue setup
        self.dialogues = dialogues
        self.current_dialogue_index = 0
        self.dialogue_index = 0
        self.name = npc_name
        self.name = name

    def import_graphics(self, name):
        self.animations = {'idle': []}
        main_path = f'../GitExercise-TT1L-08/graphics/npc/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_current_dialogue(self):
        return self.dialogues[self.current_dialogue_index][self.dialogue_index]

    def advance_dialogue(self):
        if self.dialogue_index < len(self.dialogues[self.current_dialogue_index]) - 1:
            self.dialogue_index += 1
        else:
            self.dialogue_index = 0
            self.current_dialogue_index = (self.current_dialogue_index + 1) % len(self.dialogues)