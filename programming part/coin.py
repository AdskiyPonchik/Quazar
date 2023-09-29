import pygame
from support import coin_importer
class Coin(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.coin_image()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['Coin'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

    def coin_image(self):
        coin_path = '../'
        self.animations = {'Coin':[]}
        for animation in self.animations.keys():
            full_path = coin_path + animation
            self.animations[animation] = coin_importer(full_path)

    def animate(self):
        animation = self.animations['Coin']
        self.frame_index+=self.animation_speed
        if self.frame_index>=len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        self.image = image

    def update(self,dx):
        self.animate()
        self.rect.x+=dx
