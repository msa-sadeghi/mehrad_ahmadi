from pygame.sprite import Sprite
import pygame

class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.idle_images = []
        self.run_images = []
        for i in range(1, 10):
            img = pygame.image.load(f"assets/boy/Idle ({i}).png")
            img_w = img.get_width()
            img_h = img.get_height()
            img = pygame.transform.scale(img, (img_w * 0.2, img_h * 0.2))
            self.idle_images.append(img)
        for i in range(1, 9):
            img = pygame.image.load(f"assets/boy/Run ({i}).png")
            img_w = img.get_width()
            img_h = img.get_height()
            img = pygame.transform.scale(img, (img_w * 0.2, img_h * 0.2))
            self.run_images.append(img)
            
        self.image = self.idle_images[0]
        self.rect = self.image.get_rect()
        
        self.rect.topleft = (x,y)
        self.image_number = 0
        self.last_update_time = 0
        self.action = "idle"
        self.flip = False
        self.y_vel = 0
        self.alive = True
        self.score = 0
        self.ghost_image = pygame.image.load("assets/img/ghost.png")
    
    def draw(self, screen):
        pygame.draw.rect(screen,(255,0,0), self.rect, 3)
        if not self.alive:
            self.image = self.ghost_image
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        
    def move(self, tiles, enemy_group, coin_group):
        if self.alive:
            if pygame.sprite.spritecollide(self, enemy_group, True):
                self.alive = False
            if pygame.sprite.spritecollide(self, coin_group, True):
                self.score += 1
            
            dx = 0
            dy = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] :
                self.change_action("run")
                self.flip = True
                dx -= 5
            if keys[pygame.K_RIGHT] :
                self.change_action("run")
                self.flip = False
                dx += 5
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.change_action("idle")
            if keys[pygame.K_SPACE]:
                self.y_vel = -12
                
            self.y_vel += 1
            dy += self.y_vel            
            
            for t in tiles:
                if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                    self.y_vel = 0
                    dy = t[1].top - self.rect.bottom
                    
                if t[1].colliderect(self.rect.x + dx, self.rect.y , self.rect.size[0], self.rect.size[1]):
                    dx =0
                    
            
            
            self.rect.x += dx
            self.rect.y += dy
            
    def change_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.image_number = 0
    def animation(self):
        if self.action == "idle":
            self.image = self.idle_images[self.image_number]
            if pygame.time.get_ticks() - self.last_update_time > 100:
                self.last_update_time = pygame.time.get_ticks()
                self.image_number += 1
                if self.image_number >= len(self.idle_images):
                    self.image_number = 0
        elif self.action == "run":
            self.image = self.run_images[self.image_number]
            if pygame.time.get_ticks() - self.last_update_time > 100:
                self.last_update_time = pygame.time.get_ticks()
                self.image_number += 1
                if self.image_number >= len(self.run_images):
                    self.image_number = 0
            