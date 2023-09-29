import pygame
from support import player_importer
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.character_image()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['right_fixed'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6
        self.gravity = 0.8
        self.jump_speed = -16
        self.dirright= 1
        self.on_ground = False
        self.on_roof = False
        self.on_left = False
        self.on_right = False

    def character_image(self):
        character_path = '../Character_tools/'
        self.animations = {'right_fixed':[]}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = player_importer(full_path)

    def animate(self):
        animation = self.animations['right_fixed']
        self.frame_index +=self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.dirright:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True, False)
            self.image = flipped_image
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_roof and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_roof and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_roof:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.dirright = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.dirright = 0
        else:
            self.direction.x = 0
        if keys[pygame.K_UP] and self.on_ground:
                self.jump()
    def apply_gravity(self):
        self.direction.y+=self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.animate()