import pygame
import os

LASER_WIDTH = 10
BASE_WIDTH = 100
BASE_HEIGHT = 100

class laser(pygame.sprite.Sprite):
    def __init__(self, l, x, y, rotation, screen):#rotation 1-4(N,E,S,W)
        pygame.sprite.Sprite.__init__(self)
        if rotation == 1 or rotation == 3:
            self.surface = pygame.Surface(LASER_WIDTH, l)
            self.base = pygame.Surface(BASE_WIDTH, BASE_HEIGHT)
        else:
            self.surface = pygame.Surface(l, LASER_WIDTH)
            self.base = pygame.Surface(BASE_HEIGHT, BASE_WIDTH)
        self.surface.fill((255, 0, 0))
        self.base.fill((100,100,100))
        self.base_rect = self.base.get_rect()
        self.laser_rect = self.surface.get_rect()
        self.screen = screen
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.base, self.rect)
        self.screen.blit(self.base, self.rect)

    def update(self):
        self.draw()
    #use animation to make laser look like it moves
