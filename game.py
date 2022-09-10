import pygame
from monster import Monster
from adventurer import Adventurer
from attack import Attack


class RPGGame:
    def __init__(self, w=800, h=600):
        pygame.init()
        self.w = w
        self.h = h

        # init display
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('RPG Game')
        clock = pygame.time.Clock()
        crashed = False

        print(pygame.display.get_surface().get_size())

        self.monster = Monster(self)
        self.adventorer = Adventurer(self)
        a_x, a_y = self.adventorer.getPosition()
        self.attack = Attack(self, a_x, a_y)
        i = 0
        while not crashed:

            clock.tick(10)
            pygame.display.flip()

            self.attack.blitme(i)
            self.adventorer.blitme()
            self.monster.blitme()
            i = i+1
            if(i == 12):
                i = 0

            crash_result = pygame.sprite.collide_rect(
                self.attack, self.monster)
            if crash_result == 1:
                print("collision")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    print(event)
                    pygame.display.update()

                    pygame.quit()
                    quit()
