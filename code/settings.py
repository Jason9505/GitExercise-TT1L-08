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
	'monster lvl 2': {'health': 300,'exp':100,'damage':(20, 30),'attack_type': 'slash', 'image': '../graphics/monsters/monster lvl 2/monster lvl 2 solo.png', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'boss': {'health': 900,'exp':250,'damage':(50, 70),'attack_type': 'claw','image': '../graphics/monsters/boss/monster lvl 1 solo.png', 'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'monster lvl 3': {'health': 500,'exp':110,'damage':(30, 40),'attack_type': 'thunder', 'image': '../graphics/monsters/monster lvl 3/monster lvl 3 solo.png','attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'monster lvl 1': {'health': 100,'exp':120,'damage':(5, 15),'attack_type': 'leaf_attack', 'image': '../graphics/monsters/monster lvl 1/monster lvl 1 solo.png', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
