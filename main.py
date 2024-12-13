import time
import pygame
import os

import collision
import player

os.environ['SDL_AUDIODRIVER'] = 'directx'

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Platformer")

FPS = 60
clock = pygame.time.Clock()


player_object = player.player(0, 100, 10, 10)

move_left = False
move_right = False
jump = False


def draw_background():
    screen.fill((0, 255, 0))

class TEMP:
    def __init__(self,x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h)

run = True
while run:
    draw_background()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_w:
                jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                jump = False
    
    pygame.draw.rect(screen, (0, 0, 0), TEMP(60,10,100,100))
    player_object.move(move_left, move_right, jump, False)
    collision.collision(player_object, TEMP(60,10,100,100))
    player_object.draw(screen)
    
    pygame.display.update()
