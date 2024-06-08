import pygame

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dialogue")

black = (0, 0, 0)

map = pygame.image.load("map.png")
sprite_sheet_up = pygame.image.load("character_sheet_up.png")
sprite_sheet_down = pygame.image.load("character_sheet_down.png")
sprite_sheet_left = pygame.image.load("character_sheet_left.png")
sprite_sheet_right = pygame.image.load("character_sheet_right.png")

# Define frames
frames_up = []
frames_down = []
frames_left = []
frames_right = []

frame_width = 64
frame_height = 64

def extract_frames(sheet, frame_list):
    for i in range(9):
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
current_frame_index = 0
is_moving = False

# Set up camera
camera_x = screen_width
camera_y = screen_height
camera = pygame.Rect(0, 0, camera_x, camera_y)

# Define NPC with multiple dialogues
class NPC:
    def __init__(self, x, y, dialogues,image,name):
        self.rect = pygame.Rect(x, y, character_width, character_height)
        self.dialogues = dialogues
        self.current_dialogue_index = 0
        self.dialogue_index = 0
        self.image = image
        self.name = name

geopard = pygame.image.load("../GitExercise/character/geo.png")
nurse = pygame.image.load("../GitExercise/character/nurse1.png")
angel = pygame.image.load("../GitExercise/character/angel1.png")


geopard = NPC(600, 400, [
    ["", "There used to be almost an infinite amount village through out this world.", "Everything changes when the Demon Lord, Zoltraak arise from the underworld.", 
     "And so began the age of chaos. He and his army sweep the land.", "Burning down villages and basically destroying every land he steps on.",
     "Some try to fight the demon lord but never return.", "Many choose to run away to seek for a safer place to hide but it’s no use.", 
     "And now we’re the last ones standing but we’re not safe either.", "Cause it’s only a matter of time before the demon lord found us and claim this realm once."],
    ["", "Unfortunately, I have no clue also.", "It could be a couple of days, to a couple of months.", "But everything is alright now. Now that you are here. "]
],geopard,"Geopard")

nurse = NPC(800, 400, [
    ["", "Tobe fly, fly! Ase to chi to namida de! Hikaru tsubasade! Ima zenbu zenbu okisate, tobe fly!", "I'm Nigga!"]
],nurse,"Nurse")

angel = NPC(600,500,[
    ["", "Follow the path to the village to seek your purpose of this realm.", "Press w to go forward, press a to go left, press d to go right and press s to go backward."]
],angel,"???")

def draw_text(surface, text, position, font, color, max_length):
    text_surface = font.render(text[:max_length], True, color)
    surface.blit(text_surface, position)

running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
show_dialogue = False
show_press_e = False
e_key_pressed = False
mouse_clicked = False

scroll_speed = 1  # Speed of text scrolling
text_position = 0  # Current position in the text
active_npc = None  # Currently active NPC

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_clicked = True
                if show_dialogue and active_npc:
                    if active_npc.dialogue_index < len(active_npc.dialogues[active_npc.current_dialogue_index]) - 1:
                        active_npc.dialogue_index += 1
                        text_position = 0  # Reset text position for new dialogue
                    else:
                        show_dialogue = False
                        active_npc.dialogue_index = 0
                        # Switch to the next dialogue sequence
                        active_npc.current_dialogue_index = (active_npc.current_dialogue_index + 1) % len(active_npc.dialogues)
                        text_position = 0  # Reset text position for new dialogue

    keys = pygame.key.get_pressed()

    if not show_dialogue:  # Only allow character movement when not showing dialogue
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
        else:
            is_moving = False

    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

    if geopard.rect.colliderect(character_rect):
        active_npc = geopard
    elif nurse.rect.colliderect(character_rect):
        active_npc = nurse
    elif angel.rect.colliderect(character_rect):
        active_npc = angel
    else:
        active_npc = None

    show_press_e = active_npc is not None

    if show_press_e and keys[pygame.K_e]:
        if not e_key_pressed:
            e_key_pressed = True
            if not show_dialogue:
                show_dialogue = True
                active_npc.dialogue_index = 1  # Start from the second dialogue
                text_position = 0  # Reset text position for new dialogue
            else:
                if active_npc.dialogue_index < len(active_npc.dialogues[active_npc.current_dialogue_index]) - 1:
                    active_npc.dialogue_index += 1
                    text_position = 0  # Reset text position for new dialogue
                else:
                    active_npc.dialogue_index = 0
                    # Switch to the next dialogue sequence
                    active_npc.current_dialogue_index = (active_npc.current_dialogue_index + 1) % len(active_npc.dialogues)
                    text_position = 0  # Reset text position for new dialogue

    if not keys[pygame.K_e]:
        e_key_pressed = False

    # Adjust camera position according to the character
    camera.centerx = character_x
    camera.centery = character_y
    camera.clamp_ip(pygame.Rect(0, 0, map.get_width(), map.get_height()))

    # Update frame index if moving
    if is_moving:
        current_frame_index = int(pygame.time.get_ticks() / 100) % len(current_frames)

    # Draw the map
    screen.fill(black)
    screen.blit(map, (-camera.x, -camera.y))

    # Draw the NPCs
    for npc in [geopard, nurse, angel]:
        npc_screen_x = npc.rect.x - camera.x
        npc_screen_y = npc.rect.y - camera.y
        screen.blit(npc.image, (npc_screen_x, npc_screen_y))

    # Draw the character
    current_frame = current_frames[current_frame_index]
    screen.blit(current_frame, (screen_width // 2 - character_width // 2, screen_height // 2 - character_height // 2))

    # Display "Press E" prompt
    if show_press_e and not show_dialogue:
        draw_text(screen, "Press E  ", (screen_width // 2, screen_height // 2 - 50), font, (255, 255, 255), len("Press E"))

    # Display dialogue
    if show_dialogue and active_npc:
        dialogue_box_width = 1200
        dialogue_box_height = 100
        dialogue_box_x = 50
        dialogue_box_y = screen_height - dialogue_box_height - 50
        pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
        pygame.draw.rect(screen, (255, 255, 255), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height), 2)

        dialogue_text = active_npc.dialogues[active_npc.current_dialogue_index][active_npc.dialogue_index]

        # Draw NPC image above the dialogue box
        npc_image_x = dialogue_box_x + 5
        npc_image_y = dialogue_box_y - active_npc.image.get_height() - 60
        scaled_npc_image = pygame.transform.scale(active_npc.image, (active_npc.image.get_width() * 2, active_npc.image.get_height() * 2))
        screen.blit(scaled_npc_image, (npc_image_x, npc_image_y))

        # Display NPC name beside the picture
        npc_name_x = npc_image_x + scaled_npc_image.get_width() - 20
        npc_name_y = npc_image_y + 90
        draw_text(screen, active_npc.name, (npc_name_x, npc_name_y), font, (0,0,0), len(active_npc.name))

        # Update text position for scrolling effect
        text_position += scroll_speed
        if text_position > len(dialogue_text):
            text_position = len(dialogue_text)

        draw_text(screen, dialogue_text, (dialogue_box_x + 10, dialogue_box_y + 10), font, (255, 255, 255), text_position)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()