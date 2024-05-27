import pygame
pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Movement")
clock = pygame.time.Clock()

black = (0,0,0)

sprite_sheet_up = pygame.image.load("img/character_sheet_up.png")
sprite_sheet_down = pygame.image.load("img/character_sheet_down.png")
sprite_sheet_left = pygame.image.load("img/character_sheet_left.png")
sprite_sheet_right = pygame.image.load("img/character_sheet_right.png")

#define frame
frames_up = []
frames_down = []
frames_left = []
frames_right = []
 
frame_width = 50
frame_height = 50

def extract_frames(sheet, frame_list):
    for i in range(8): 
        frame = sheet.subsurface((i * frame_width, 0), (frame_width, frame_height))
        frame_list.append(frame)

extract_frames(sprite_sheet_up, frames_up)
extract_frames(sprite_sheet_down, frames_down)
extract_frames(sprite_sheet_left, frames_left)
extract_frames(sprite_sheet_right, frames_right)

character_width = 50
character_height = 50
character_x = (screen_width - character_width) // 2
character_y = (screen_height - character_height) // 2
character_speed = 5
current_frames = frames_down
is_moving = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        character_x -= character_speed
        current_frames = frames_left
        is_moving = True
    elif keys[pygame.K_d]:
        character_x += character_speed
        current_frames = frames_right
        is_moving = True
    elif keys[pygame.K_w]:
        character_y -= character_speed
        current_frames = frames_up
        is_moving = True
    elif keys[pygame.K_s]:
        character_y += character_speed
        current_frames = frames_down
        is_moving = True
    else :
        is_moving = False

    screen.fill(black)
    if is_moving:
        screen.blit(current_frames[int(pygame.time.get_ticks() / 100) % len(current_frames)], (character_x, character_y))
    else:
        if current_frames == frames_left:
            screen.blit(current_frames[0], (character_x, character_y))
        elif current_frames == frames_right:
            screen.blit(current_frames[0], (character_x, character_y))
        elif current_frames == frames_up:
            screen.blit(current_frames[0], (character_x, character_y))
        elif current_frames == frames_down:
            screen.blit(current_frames[0], (character_x, character_y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
