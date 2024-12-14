import pygame
import os
import math

class moving_platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, distance, time_to_move, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h])
        self.image.fill((0,100,255))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.far_target = distance + x
        self.close_target = x
        self.time = time_to_move
        self.direction = 1
        self.speed = math.ceil((self.far_target - self.close_target)/self.time)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.speed * self.direction
        if self.rect.x >= self.far_target or self.rect.x <= self.close_target:
            self.direction *= -1

    def update(self):
        self.move()
        self.draw()