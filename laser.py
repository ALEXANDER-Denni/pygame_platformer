import pygame
import os

LASER_WIDTH = 10
BASE_WIDTH = 20
BASE_HEIGHT = 10
DAMAGE = 10

class laser(pygame.sprite.Sprite):
    def __init__(self, l, x, y, rotation, screen):  # rotation 1-4(N,E,S,W)
        pygame.sprite.Sprite.__init__(self)
        if rotation == 1 or rotation == 3:
            self.surface = pygame.Surface((LASER_WIDTH, l))
            self.base = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
        else:
            self.surface = pygame.Surface((l, LASER_WIDTH))
            self.base = pygame.Surface((BASE_HEIGHT, BASE_WIDTH))
        self.surface.fill((255, 0, 0))
        self.base.fill((100, 100, 100))
        self.base_rect = self.base.get_rect()
        self.laser_rect = self.surface.get_rect()
        self.screen = screen
        self.base_rect.x = x
        self.base_rect.y = y
        self.laser_rect.x = x - LASER_WIDTH/2 + BASE_WIDTH/2
        self.laser_rect.y = y

        self.damage = DAMAGE
    def draw(self):
        self.screen.blit(self.surface, self.laser_rect)
        self.screen.blit(self.base, self.base_rect)

    def update(self):
        self.draw()
    #use animation to make laser look like it moves
