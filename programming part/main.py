import pygame,sys
import config
from level import Level
pygame.init()
bg = pygame.image.load('../hinterground.png')
screen = pygame.display.set_mode((config.screen_width,config.screen_height))
clock = pygame.time.Clock()
level = Level(config.level_map,screen)
music = pygame.mixer.music.load('../Sounds/main_theme.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0,0))
    level.go()

    pygame.display.update()
    clock.tick(120)