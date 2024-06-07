import pygame
import sys
import time

pygame.init()

#create screen size
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
width, height = pygame.display.get_surface().get_size()    
pygame.display.set_caption("Realm Redeemers: The Last Stand")

black = (0,0,0)
white = (255, 255, 255)
options_bg = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/options_bg.png")
options_bg   = pygame.transform.scale(options_bg, (width, height))

#load background music
pygame.mixer.music.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/audio/background_music.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

#load sound effect
sound_effect = pygame.mixer.Sound("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/audio/sound_effect.wav")
sound_effect.set_volume(0.3)

#load background image
background = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/background.png")
background = pygame.transform.scale(background, (width, height))

#load game title
title = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/game_title.png")
title_width = int(width * 0.6)
title_height = int(height * 0.4)
title = pygame.transform.scale(title, (title_width, title_height))

#load button image
start = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/start_btn.png")
exit = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/exit_btn.png")
options = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/options_btn.png")
start_animation = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/start_an_btn.png")
exit_animation = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/exit_an_btn.png")
options_animation = pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/options_an_btn.png")

#button class
class Button():
    def __init__(self,x,y,image,hover_image,scale):
        self.base_image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(hover_image.get_width() * scale), int(hover_image.get_height() * scale)))
        self.rect = self.base_image.get_rect()
        self.rect.topleft = (x, y)
        self.image = self.base_image
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, pos):
        if self.rect.collidepoint(pos):
            self.image = self.hover_image
        else:
            self.image = self.base_image

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

#create button
start_button = Button(700,430,start,start_animation,1)
options_button = Button(700,550,options,options_animation,1)
exit_button = Button(700,670,exit,exit_animation,1)

#Options variables  
sound_volume = 100
graphics_quality = "High"
controls = "WASD"

# Text page
typing_text = "Eloooooo....."
font = pygame.font.SysFont(None, 60)
text_surface = font.render('', True,white)
text_rect = text_surface.get_rect(center=(500,540))

#game loop
current_page = "menu"
run = True
while run:

    screen.blit(background, (0,0))

    if current_page == "menu":
        screen.blit(title, (width // 2 - title.get_width() // 2, 50))
        start_button.update(pygame.mouse.get_pos())
        options_button.update(pygame.mouse.get_pos())
        exit_button.update(pygame.mouse.get_pos())
        start_button.draw()
        options_button.draw()
        exit_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.clicked(event.pos):
                    current_page = "typing"
                    sound_effect.play()  
                elif options_button.clicked(event.pos):
                    current_page = "options"  
                    sound_effect.play()  
                elif exit_button.clicked(event.pos):
                    run = False
                    sound_effect.play()  

    elif current_page == "typing":
        screen.fill(black)
        for i in range(len(typing_text)):
            text_surface = font.render(typing_text[:i+1], True, white)
            screen.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(100)  # Adjust typing speed    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()

        time.sleep(1)
        current_page = "menu"

    elif current_page == "game":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            current_page = "menu"

    elif current_page == "options":

        screen.blit(options_bg,(0,0))
        # Display options
        font = pygame.font.SysFont(None, 60)

        sound_text = font.render(f"Sound Volume: {sound_volume}", True, (255, 255, 255))
        screen.blit(sound_text, (width // 2 - sound_text.get_width() // 2, 300))

        graphics_text = font.render(f"Graphics Quality: {graphics_quality}", True, (255, 255, 255))
        screen.blit(graphics_text, (width // 2 - graphics_text.get_width() // 2, 400))

        controls_text = font.render(f"Controls: {controls}", True, (255, 255, 255))
        screen.blit(controls_text, (width // 2 - controls_text.get_width() // 2, 500))

        increase_sound_button = Button(width // 2 + 200, 290, pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/volume_up.png"), pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/volume_up.png"), 0.5)
        decrease_sound_button = Button(width // 2 - 270, 290, pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/volume_down.png"), pygame.image.load("C:/Users/GF66/pygame_project/GitExercise-TT1L-08/graphics/img/volume_down.png"), 0.5)

        increase_sound_button.draw()
        decrease_sound_button.draw()

        # Event handling for adjusting options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if increase_sound_button.clicked(event.pos):
                    sound_volume = min(100, sound_volume + 10)  # Increase sound volume
                    pygame.mixer.music.set_volume(sound_volume / 100)
                    sound_effect.play()  
                elif decrease_sound_button.clicked(event.pos):
                    sound_volume = max(0, sound_volume - 10)  # Decrease sound volume
                    pygame.mixer.music.set_volume(sound_volume / 100)
                    sound_effect.play()    
                elif exit_button.clicked(event.pos):
                    current_page = "menu"
                    sound_effect.play()  

        exit_button.update(pygame.mouse.get_pos())
        exit_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.clicked(event.pos):
                    current_page = "menu"
                    sound_effect.play()  

    pygame.display.update()

pygame.quit()