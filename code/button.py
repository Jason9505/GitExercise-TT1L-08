import pygame

class Button:
    def __init__(self, x, y, image, hover_image, scale):
        self.base_image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(hover_image.get_width() * scale), int(hover_image.get_height() * scale)))
        self.rect = self.base_image.get_rect(topleft=(x, y))
        self.image = self.base_image

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, pos):
        if self.rect.collidepoint(pos):
            self.image = self.hover_image
        else:
            self.image = self.base_image

    def clicked(self, pos):
        return self.rect.collidepoint(pos)