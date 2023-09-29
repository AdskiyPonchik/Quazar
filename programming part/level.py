import pygame
from platforma import Platforma
from config import tile_size, screen_width, level_map
from player import Player
from coin import Coin
from score_counter import Score
class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        self.score = 0
        self.score_group = pygame.sprite.Group()
        self.coin_sound, self.final = pygame.mixer.Sound('../Sounds/coin.wav'), pygame.mixer.Sound('../Sounds/win_sound.wav')
        self.coin_sound.set_volume(0.1)
        self.final.set_volume(0.5)

    def setup_level(self,layout):
        self.platforms = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.coins = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = (row_index * tile_size)
                if col =='x':
                    tile = Platforma((x, y), tile_size)
                    self.platforms.add(tile)
                if col == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if col == 'c':
                    coin = Coin((x, y))
                    self.coins.add(coin)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < (screen_width/4) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width/4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horisontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right >self.current_x or player.direction.x <=0):
            player.on_right = False

        #coin collision. I think it will be better if i write coin collision here.
        # It have no sense make an a complicated collision for coin. When I touch the coin it only delete))))
        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player.rect):
                self.score+=1
                if self.score == 10:
                    self.final.play()
                    sprite.kill()
                    self.score_count = Score(self.score, (50, 50))
                    self.score_group.empty()
                    self.score_group.add(self.score_count)
                else:
                    self.coin_sound.play()
                    sprite.kill()
                    self.score_count = Score(self.score, (50, 50))
                    self.score_group.empty()
                    self.score_group.add(self.score_count)
            else:
                if not self.score_group:
                    self.score_count = Score(self.score, (50, 50))
                    self.score_group.add(self.score_count)

    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_roof = True

        if player.on_ground and player.direction.y<0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_roof and player.direction.y > 0:
            player.on_roof = False

    def go(self):
        #tales
        self.platforms.update(self.world_shift)
        self.platforms.draw(self.display_surface)
        self.scroll_x()
        #player
        self.player.update()
        self.horisontal_collision()
        self.vertical_collision()
        self.player.draw(self.display_surface)
        #coin
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        #score
        self.score_group.draw(self.display_surface)