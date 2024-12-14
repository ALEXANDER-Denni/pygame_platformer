import pygame
import os

SPEED = 25
WIDTH = 5
HEIGHT = 5

class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, direction, fired_by_player, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.damage = damage
        self.speed = SPEED
        self.direction = direction
        self.fired_by_player = fired_by_player

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.direction==1, False), self.rect)

    def move(self):
        self.rect.x += self.speed * self.direction

    def update(self):
        self.move()
        self.draw()

