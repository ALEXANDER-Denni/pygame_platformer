import pygame
import os

class wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.draw()