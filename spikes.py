import pygame
import os

DAMAGE = 10

class spike(pygame.sprite.Sprite):
    def __init__(self, x, y, l, height, rotation, screen): # rotation 1-4(N,E,S,W)
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.rotation = rotation
        if rotation == 1:
            self.image = pygame.Surface([l, height])
        elif rotation == 2:
            self.image = pygame.Surface([height, l])
        elif rotation == 3:
            self.image = pygame.Surface([l, height])
        elif rotation == 4:
            self.image = pygame.Surface([height, l])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0,120,0))
        self.damage = DAMAGE
    def draw(self):
        self.screen.blit(pygame.transform.rotate(self.image, (self.rotation-1)*90), self.rect)

    def update(self):
        self.draw()