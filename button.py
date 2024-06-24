import pygame
class Button:
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        
        
    def draw(self, screen):
        click = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                click = True
                
                
        screen.blit(self.image, self.rect)
        return click