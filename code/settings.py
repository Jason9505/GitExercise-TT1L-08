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

# enemy
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 30},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 1, 'notice_radius': 1},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 30},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 30}
    }


background_music_path = "../GitExercise-TT1L-08/audio/background_music.mp3"
sound_effect_path = "../GitExercise-TT1L-08/audio/sound_effect.wav"
options_bg_img_path = "../GitExercise-TT1L-08/graphics/img/options_bg.png"
game_title_img_path = "../GitExercise-TT1L-08/graphics/img/game_title.png"
start_btn_img_path = "../GitExercise-TT1L-08/graphics/img/start_btn.png"
exit_btn_img_path = "../GitExercise-TT1L-08/graphics/img/exit_btn.png"
options_btn_img_path = "../GitExercise-TT1L-08/graphics/img/options_btn.png"
start_an_btn_img_path = "../GitExercise-TT1L-08/graphics/img/start_an_btn.png"
exit_an_btn_img_path = "../GitExercise-TT1L-08/graphics/img/exit_an_btn.png"
options_an_btn_img_path = "../GitExercise-TT1L-08/graphics/img/options_an_btn.png"
volume_up_img_path = "../GitExercise-TT1L-08/graphics/img/volume_up.png"
volume_down_img_path = "../GitExercise-TT1L-08/graphics/img/volume_down.png"

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