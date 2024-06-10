import pygame

class DialogueManager:
    def __init__(self, font):
        self.font = font
        self.active = False
        self.text = ""
        self.text_position = 0
        self.scroll_speed = 1  # Speed of text scrolling

    def start_dialogue(self, text):
        self.active = True
        self.text = text
        self.text_position = 0

    def advance_text(self):
        self.text_position += self.scroll_speed
        if self.text_position > len(self.text):
            self.text_position = len(self.text)

    def draw(self, screen):
        if self.active:
            dialogue_box_width = 1200
            dialogue_box_height = 100
            dialogue_box_x = 50
            dialogue_box_y = screen.get_height() - dialogue_box_height - 50
            pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
            pygame.draw.rect(screen, (255, 255, 255), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height), 2)
            
            # Draw the dialogue text
            text_surface = self.font.render(self.text[:self.text_position], True, (255, 255, 255))
            screen.blit(text_surface, (dialogue_box_x + 10, dialogue_box_y + 10))