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
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'C:/Users/GF66/pygame_project/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'C:/Users/GF66/pygame_project/audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 1, 'notice_radius': 1},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'C:/Users/GF66/pygame_project/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'C:/Users/GF66/pygame_project/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}