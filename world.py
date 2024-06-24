import pygame
from enemy import Enemy
from coin import Coin
class World:
    def __init__(self, world_data, enemy_group, coin_group):
        self.tiles = []
        for i in range(len(world_data)):
            for j in range(len(world_data[0])):
                if world_data[i][j] == 1:
                    img = pygame.image.load("assets/dirt.png")
                    img = pygame.transform.scale(img, (50,50))
                    rect = img.get_rect(topleft = (j * 50, i * 50))
                    self.tiles.append((img,rect))
                if world_data[i][j] == 2:
                    img = pygame.image.load("assets/grass.png")
                    img = pygame.transform.scale(img, (50,50))
                    rect = img.get_rect(topleft = (j * 50, i * 50))
                    self.tiles.append((img,rect))
                if world_data[i][j] == 3:
                    Enemy(j * 50, i * 50+ 15, enemy_group)
                if world_data[i][j] == 4:
                    Coin(j * 50, i * 50+ 15, coin_group)
                    
                    
    def draw(self, screen):
        for t in self.tiles:
            screen.blit(t[0], t[1])
            
        