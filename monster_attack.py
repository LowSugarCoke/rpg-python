
from ctypes import sizeof
import pygame
from pygame.sprite import Sprite


class MonsterAttack(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.images = []
        self.loadImages()
        self.image = pygame.image.load(
            'img/monster_attack/monster_attack-0.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x + 150
        self.rect.y = y+400
        self.damage = 100

    def blitme(self, num):
        self.screen.blit(self.images[num], self.rect)

    def loadImages(self):
        for i in range(0, 12):
            self.images.append(pygame.image.load(
                'img/monster_attack/monster_attack-'+str(i)+'.jpg').convert_alpha())
            self.images[i] = pygame.transform.rotozoom(
                self.images[i], 0, 1)

        print(len(self.images))