import pygame
pygame.init()

#create screen size
width = 1920
height = 1080
screen = pygame.display.set_mode((width,height))    
pygame.display.set_caption("Realm Redeemers: The Last Stand")

#load background image
background = pygame.image.load("background.png")

#load button image
start = pygame.image.load("start_btn.png")
exit = pygame.image.load("exit_btn.png")
options = pygame.image.load("options_btn.png")

#button class
class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#create button
start_button = Button(820,450,start,3)
options_button = Button(820,570,options,3)
exit_button = Button(820,690,exit,3)

#manage page
current_page = "menu"

#game loop
run = True
while run:

    screen.blit(background, (0,0))

    start_button.draw()
    options_button.draw()
    exit_button.draw()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_page == "menu":
                if start_button.rect.collidepoint(event.pos):
                    current_page = "game"  # Switch to the game page when start button clicked
                elif options_button.rect.collidepoint(event.pos):
                    print("Options button clicked")
                elif exit_button.rect.collidepoint(event.pos):
                    run = False

    pygame.display.update()

pygame.quit()