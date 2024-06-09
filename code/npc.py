import pygame
from settings import *
from entity import Entity
from support import *

class Npc(Entity):
    def __init__(self,npc_name,pos,groups):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'npc'

        # graphics setup
        self.import_graphics(npc_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

    def import_graphics(self,name):
        self.animations = {'idle':[]}
        main_path = f'../graphics/npc/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation) # + animation