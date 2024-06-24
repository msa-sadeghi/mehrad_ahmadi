from pygame.sprite import Sprite
import pygame
class Coin(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/img/coin.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
        self.direction = 1
        self.counter = 0
  