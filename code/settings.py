import pygame
from button import *
# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILESIZE = 16
PLAYER_LAYER = 1
FPS = 60
WIDTH = SCREEN_WIDTH
HEIGHT = SCREEN_HEIGHT
FRAME_WIDTH = 64
FRAME_HEIGHT = 64

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# enemy
monster_data = {
	'monster lvl 1': {'health': 100,'exp':100,'damage':(10, 20),'image': '../data/monsters/monster lvl 1/monster lvl 1 solo.png', 'attack_type': 'slash', 'music': '../data/audio/battle-music.mp3', 'background_image': '../data/background/forest.jpeg', 'attack_sound':'../GitExercise-TT1L-08/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 30},
	'monster lvl 2': {'health': 300,'exp':250,'damage':(20, 30),'image': '../data/monsters/monster lvl 2/monster lvl 2 solo.png','attack_type': 'claw','music': '../data/audio/battle-music.mp3', 'background_image': '../data/background/forest.jpeg','attack_sound':'../GitExercise-TT1L-08/audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 1, 'notice_radius': 1},
	'boss': {'health': 800,'exp':110,'damage':(50, 70),'image': '../data/monsters/boss/final boss.png','attack_type': 'thunder', 'music': '../data/audio/boss theme.mp3', 'background_image': '../data/background/desert.jpeg', 'attack_sound':'../GitExercise-TT1L-08/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 30},
	'monster lvl 3': {'health': 700,'exp':120,'damage':(30, 50),'image': '../data/monsters/monster lvl 3/monster lvl 3 solo.png','attack_type': 'leaf_attack', 'music': '../data/audio/battle-music.mp3', 'background_image': '../data/background/forest.jpeg', 'attack_sound':'../GitExercise-TT1L-08/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 30}
    }


background_music_path = "../data/audio/background_music.mp3"
sound_effect_path = "../data/audio/sound_effect.wav"
options_bg_img_path = "../data/background/options_bg.png"
game_title_img_path = "../data/graphics text/game_title.png"
start_btn_img_path = "../data/button/start_btn.png"
exit_btn_img_path = "../data/button/exit_btn.png"
options_btn_img_path = "../data/button/options_btn.png"
start_an_btn_img_path = "../data/button/start_an_btn.png"
exit_an_btn_img_path = "../data/button/exit_an_btn.png"
options_an_btn_img_path = "../data/button/options_an_btn.png"
volume_up_img_path = "../data/button/volume_up.png"
volume_down_img_path = "../data/button/volume_down.png"

start = pygame.image.load(start_btn_img_path)
exit = pygame.image.load(exit_btn_img_path)
options = pygame.image.load(options_btn_img_path)
start_animation = pygame.image.load(start_an_btn_img_path)
exit_animation = pygame.image.load(exit_an_btn_img_path)
options_animation = pygame.image.load(options_an_btn_img_path)
start_button = Button(700,430,start,start_animation,1)
options_button = Button(700,550,options,options_animation,1)
exit_button = Button(700,670,exit,exit_animation,1)

title = pygame.image.load(game_title_img_path)
title_width = int(WIDTH * 0.6)
title_height = int(HEIGHT * 0.4)
title = pygame.transform.scale(title, (title_width, title_height))