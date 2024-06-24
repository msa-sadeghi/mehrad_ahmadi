import pygame
from player import Player
from world import World
from level_creator import world_data
from button import Button
p = Player(100, 400)
pygame.init()

restart_btn = pygame.image.load("assets/img/restart_btn.png")
restart_button = Button(restart_btn, 100, 300)


f = pygame.font.SysFont("arial", 24)
score_text = f.render(f"Score: {p.score}", True, (255,0,0))
score_rect = score_text.get_rect(topleft = (0,0))


screen_width = 800
screen_height = 600

FPS = 60
clock = pygame.time.Clock()
enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
w = World(world_data, enemy_group, coin_group)


screen = pygame.display.set_mode((800, 600))

running = True
while running:
    score_text = f.render(f"Score: {p.score}", True, (255,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    w.draw(screen)
    p.draw(screen) 
    if p.alive:
        p.animation() 
            
        enemy_group.update()
    else:
        if restart_button.draw(screen):
            enemy_group.empty()
            coin_group.empty()
            p.__init__(100, 200)
            w = World(world_data, enemy_group, coin_group)
            
    p.move(w.tiles, enemy_group, coin_group)  
    enemy_group.draw(screen)
    coin_group.draw(screen)
    screen.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(FPS)