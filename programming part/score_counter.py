import pygame
from support import coin_importer
class Score(pygame.sprite.Sprite):
    def __init__(self,score,pos):
        super().__init__()
        self.pos = (50,50)
        self.image = pygame.image.load(self.score_image(score))
        self.rect = self.image.get_rect(topleft = self.pos)

    def score_image(self,score):
        self.score = score
        stack = {0:'0.png', 1:'1.png', 2:'2.png', 3:'3.png', 4:'4.png', 5:'5.png', 6:'6.png', 7:'7.png', 8:'8.png', 9:'9.png','winner':'Trophy.png'}
        full_path = '../Score/'
        if 0<=self.score<=9:
            image = full_path+stack.get(self.score)
        else:
            image = full_path+stack.get('winner')

        return image