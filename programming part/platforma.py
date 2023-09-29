import pygame
from support import platform_importer
class Platforma(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.platform_image()
        self.frame_index = 0
        self.animation_speed = 0.13
        self.image = self.animations['Platforms'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

    def platform_image(self):
        platform_path = '../'
        self.animations = {'Platforms':[]}

        for animation in self.animations.keys():
            full_path = platform_path + animation
            self.animations[animation] = platform_importer(full_path)

    def animate(self):
        animation = self.animations['Platforms']
        self.frame_index+=self.animation_speed
        if self.frame_index>=len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        self.image = image


    def update(self, dx):
        self.animate()
        self.rect.x+=dx